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
myst_enable_extensions = ["colon_fence", "substitution", "linkify", "include"]
myst_allow_substitutions = True
myst_heading_anchors = 3
myst_enable_extensions.append("external")

source_suffix = {'.md': 'markdown'}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_context = {
   # ...
   "default_mode": "light"
}
