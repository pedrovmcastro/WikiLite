from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

from . import util

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
    

def random_page(request):
    choice = random.choice(util.list_entries())
    return HttpResponseRedirect(reverse("encyclopedia:entry", args=[choice]))
