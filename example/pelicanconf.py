from datetime import datetime

AUTHOR = "Fidel Ramos"
SITEURL = "http://localhost:8000"
SITENAME = "Reflex"
SITETITLE = "Reflex"
SITESUBTITLE = "Another minimalist Pelican theme"
SITEDESCRIPTION = "Reflex - Another minimalist Pelican theme."
# SITELOGO = ''
# FAVICON = '/images/favicon.ico'
BROWSER_COLOR = "#333333"
PYGMENTS_STYLE = "monokai"
PYGMENTS_STYLE_DARK = "monokai"

ROBOTS = "index, follow"

THEME = ".."
PATH = "content"
OUTPUT_PATH = "blog/"
TIMEZONE = "UTC"

DISABLE_URL_HASH = True

# PLUGIN_PATHS = ['pelican-plugins']

# Search is enabled in publishconf.py for the live site
# To test locally, install stork binary and uncomment:
# PLUGINS = ['pelican.plugins.search']
# STORK_INPUT_OPTIONS = {
#     "html_selector" : ".entry-content"
# }

# JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

MARKDOWN = {
    "extensions": [
        "markdown_captions",
    ],
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.footnotes": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {"title": "Table of Contents"},
    },
    "output_format": "html5",
}

I18N_TEMPLATES_LANG = "en"
DEFAULT_LANG = "en"
OG_LOCALE = "en_US"
LOCALE = "en_US"

DATE_FORMATS = {
    "en": "%B %d, %Y",
}

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

GITHUB_CORNER_URL = "https://github.com/haplo/pelican-theme-reflex"

SOCIAL = (
    ("x-twitter", "https://x.com/ampajaro"),
    ("github", "https://github.com/haplo/pelican-theme-reflex"),
    ("rss", "/blog/feeds/all.atom.xml"),
)

MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike 4.0 International License",
    "version": "4.0",
    "slug": "by-sa",
    "icon": True,
    "language": "en_US",
}

COPYRIGHT_YEAR = datetime.now().year
DEFAULT_PAGINATION = 10

STATIC_PATHS = ["images"]

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

USE_LESS = True
