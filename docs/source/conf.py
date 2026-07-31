# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'bill_sousa_resume'
copyright = 'Bill Sousa'
author = 'Bill Sousa'
release = '0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser'
]

source_suffix = {'.md': 'markdown'}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_theme_options = {
    "repository_url": "https://github.com/BillSousa/bill_sousa_resume",
    "use_repository_button": True,   # adds a GitHub link button
    "use_download_button": False,    # hide “download this page” if you don’t need it
    "use_fullscreen_button": True,   # toggle sidebar fullscreen
    "logo_only": False,              # show site name next to logo if you add one
    "single_page": True,             # collapses left TOC sidebar
}

html_static_path = ['_static']
html_context = {
   # ...
   "default_mode": "light"
}
# html meta is now being handled in /_templates/page.html
# sphinx_book_theme isn't rendering html_meta from conf.py into the actual
# HTML <head> section. Need to put the meta tags directly into page.html
# using Jinja, which bypasses the theme and injects them directly into the
# HTML output. Leave html_meta unhashed --- should the sphinx theme ever
# be changed, won't need to remember to unhash this.
html_meta = {
    "google-site-verification": "Vfm-HV9ibdA4ubmnyo7bO3KJ4LgmB48Lxp634CmYAPI",
    "description": "Bill Sousa resume."
}
html_baseurl = "https://bill-sousa-resume.readthedocs.io/en/latest/"