import re
from markdown2 import Markdown

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_entries() -> list[str]:
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename) for filename in filenames if filename.endswith(".md")))


def save_entry(title: str, content: str) -> None:
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def get_entry(title: str) -> str | None:
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None
    

def md2html(content: str) -> str:
    """
    Converts a Markdown string to an HTML string.
    """
    return Markdown().convert(content)


def case_insensitive(title: str, entries: list[str]) -> bool:
    """
    Checks if the string 'title' is present in the 'entries' list, case insensitive.
    Returns True if the title is found in the list, ignoring case differences.
    Returns False if the title is not found.
    """
    if title in entries:
        return True
    else: 
        entries_lower: list[str] = [entry.lower() for entry in entries]
        if title.lower() in entries_lower:
            return True
        else:
            return False
