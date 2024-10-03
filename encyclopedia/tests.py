from django.test import TestCase

# Create your tests here.

from . import util
from . import views
import random
"""
from markdown2 import Markdown

entries = util.list_entries()
css = util.get_entry("CSS")
coffee = util.get_entry("coffee")

print(entries)
print(css)
print(coffee)

markdowner = Markdown()

md = markdowner.convert(css)
#print(markdowner.convert(coffee)) #IMPORTERROR
"""

choice = random.choice(util.list_entries())
print(choice)
print(type(choice))

