from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry_page(request, entry_title):

    content = util.get_entry(entry_title)

    return render(request, "encyclopedia/entry_page.html", {
        "title": entry_title,
        "entry": content
    })
