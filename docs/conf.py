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
    "repository_url": "https://github.com/PylarBear/bear-resume",
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
