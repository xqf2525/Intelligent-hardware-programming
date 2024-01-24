# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sphinx_rtd_theme


project = 'Intelligent hardware programmingV1.0'
copyright = '2024, Taxi Education'
author = 'Taxi Education'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'cn'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'bizstyle'
#html_static_path = ['_static']


# html_theme = 'sphinxdoc'
html_theme = 'sphinx_rtd_theme'

#html_theme_path = []
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]