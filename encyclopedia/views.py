from django.shortcuts import render

from . import util

import re

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