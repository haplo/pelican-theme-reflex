import os
import sys
sys.path.append(os.curdir)

from pelicanconf import *

# this tests the Python package for pelican-theme-reflex
from pelican.themes import reflex
THEME = reflex.path()

SITEURL = "https://haplo.github.io/pelican-theme-reflex"

RELATIVE_URLS = False

USE_LESS = False

PLUGINS = ['pelican.plugins.search']

STORK_INPUT_OPTIONS = {
    "break_on_file_error": True,
    "stemming": "english",
    "url_prefix": SITEURL,
}

SHYNET_URL = (
    "https://shynet.fidelramos.net/ingress/9574b461-0b4e-4e54-adfc-1d49735686f1"
)
