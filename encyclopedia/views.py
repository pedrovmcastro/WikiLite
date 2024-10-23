from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect

from . import util
from .forms import NewPageForm, EditPageForm

import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    content = util.get_entry(title)
    if content:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "entry": util.md2html(content)
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "message": f"Entry '{title}' not found."
        })
    

def random_entry(request):
    choice = random.choice(util.list_entries())
    return HttpResponseRedirect(reverse("encyclopedia:entry", args=[choice]))


def search(request):
    q = request.GET.get('q')
    if q:
        entries = util.list_entries()
        entries_lower = [entry.lower() for entry in entries]

        # same that entry
        if q in entries:
            return HttpResponseRedirect(reverse("encyclopedia:entry", args=[q]))
        
        # case-insensitive 
        if q.lower() in entries_lower:
            i = entries_lower.index(q.lower())
            return HttpResponseRedirect(reverse("encyclopedia:entry", args=[entries[i]]))
        else:
            # sub-strings
            results = [entry for entry in entries if q.lower() in entry.lower()]
            return render(request, "encyclopedia/search.html", {
                "results": results
            })
    else:
        return render(request, "encyclopedia/error.html", {
            "message": "Search Error."
        })


def new_entry(request):
    if request.method == "POST":
        
        form = NewPageForm(request.POST)
        
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']

            # Verify if entry already exists
            if util.case_insensitive_search(title, util.list_entries()):
                return render(request, "encyclopedia/error.html", {
                    "message": "An entry with this title already exists."
                })
            
            util.save_entry(title, content)
            return redirect("encyclopedia:entry", title=title)
    else:
        form = NewPageForm()

    return render(request, "encyclopedia/new.html", {
        "form": form
    })


def edit_entry(request, title):
    if request.method == "POST":
        
        form = EditPageForm(request.POST)
        
        if form.is_valid():
            new_title = form.cleaned_data['title']
            new_content = form.cleaned_data['content']

            if not new_title:
                new_title = title

            if not new_content:
                new_content = util.get_entry(title)

            util.save_entry(new_title, new_content)
            return redirect("encyclopedia:entry", title=new_title)
    else:
        form = EditPageForm(initial={'title': title, 'content': util.get_entry(title)})

    return render(request, "encyclopedia/edit.html", {
        "form": form,
        "title": title
    })
