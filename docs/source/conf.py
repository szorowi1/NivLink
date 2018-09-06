# -*- coding: utf-8 -*-

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os, sys
import nivlink
import sphinx_bootstrap_theme
from numpydoc import numpydoc, docscrape
sys.path.insert(0, os.path.abspath(os.path.join('..','..')))

# -- Project information -----------------------------------------------------

project = 'NivLink'
copyright = '2018, Niv Lab'
author = 'Niv Lab'

# The short X.Y version
version = nivlink.__version__
release = version

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'numpydoc'
]

autosummary_generate = True
autodoc_default_flags = ['inherited-members']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['_build', '.DS_Store', '.ipynb_checkpoints']
exclude_trees = ['_build']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

# (Optional) Logo. Should be small enough to fit the navbar (ideally 24x24).
# Path should be relative to the ``_static`` files directory.
# html_logo = "my_logo.png"

# Bootstrap theme options
# https://ryan-roemer.github.io/sphinx-bootstrap-theme/README.html#theme-notes
html_theme_options = {
    
    'navbar_title': "NivLink",
    'navbar_site_name': "Site",
    'navbar_sidebarrel': False,
    'navbar_pagenav': False,
    'navbar_class': "navbar",
    'navbar_fixed_top': True,
    'navbar_links': [
        ("Install", "installation"),
        ("Projects", "projects"),
        ("DataViewer", "dataviewer"),
        ("API", "python_reference"),
        ("Contribute", "contributing")
    ],
    'bootstrap_version': "3",
    'bootswatch_theme': "sandstone",
    'nosidebar': True
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'NivLinkdoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'NivLink.tex', 'NivLink Documentation',
     'Sam Zorowitz', 'manual'),
]

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'nivlink', 'NivLink Documentation',
     [author], 1)
]

# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'NivLink', 'NivLink Documentation',
     author, 'NivLink', 'One line description of project.',
     'Miscellaneous'),
]

# -- Extension configuration -------------------------------------------------