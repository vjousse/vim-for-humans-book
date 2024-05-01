# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Vim for humans"
copyright = "2024, Vincent Jousse"
author = "Vincent Jousse"


# The short X.Y version.
version = "1.0"
# The full version, including alpha/beta/rc tags.
release = "1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "en"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

highlight_language = "vim"

rst_prolog = """
.. role:: vimcmd
.. role:: viml(code)
   :language: vim
"""

rst_epilog = """
.. |vim| replace:: *Vim*
.. |vimrc| replace:: ``~/.vimrc``
.. |.vim| replace:: *~/.vim*
.. |that| replace:: ``^``
.. |tdollar| replace:: ``$``
.. |tzero| replace:: ``0``
.. |tesc| replace:: ``Esc``
.. |tsemicolon| replace:: ``;``
.. |tcolon| replace:: ``:``
.. |tctrl| replace:: ``Control``
.. |tapos| replace:: ``'``
.. |tslash| replace:: ``/``
.. |tshift| replace:: ``Shift``
.. |tenter| replace:: ``Enter``
.. |tstar| replace:: ``*``
.. |tsharp| replace:: ``#``
.. |tleader| replace:: ``<Leader>``
.. |tcomma| replace:: ``,``
.. |ta| replace:: ``a``
.. |tA| replace:: ``A``
.. |tb| replace:: ``b``
.. |tc| replace:: ``c``
.. |td| replace:: ``d``
.. |tdtd| replace:: ``dd``
.. |te| replace:: ``e``
.. |tf| replace:: ``f``
.. |tG| replace:: ``G``
.. |tgtg| replace:: ``gg``
.. |th| replace:: ``h``
.. |ti| replace:: ``i``
.. |tI| replace:: ``I``
.. |tj| replace:: ``j``
.. |tk| replace:: ``k``
.. |tl| replace:: ``l``
.. |tm| replace:: ``m``
.. |tn| replace:: ``n``
.. |tN| replace:: ``N``
.. |to| replace:: ``o``
.. |tO| replace:: ``O``
.. |tp| replace:: ``p``
.. |tP| replace:: ``P``
.. |tu| replace:: ``u``
.. |tr| replace:: ``r``
.. |tv| replace:: ``v``
.. |tw| replace:: ``w``
.. |tx| replace:: ``x``
.. |tX| replace:: ``X``
.. |ty| replace:: ``y``
.. |tyty| replace:: ``yy``
.. |ttc| replace:: the |tc| key
.. |ttd| replace:: the |td| key
.. |tte| replace:: the |te| key
.. |tth| replace:: the |th| key
.. |tti| replace:: the |ti| key
.. |ttj| replace:: the |tj| key
.. |ttk| replace:: the |tk| key
.. |ttl| replace:: the |tl| key
.. |ttn| replace:: the |tn| key
.. |ttN| replace:: the |tN| key
.. |tto| replace:: the |to| key
.. |ttp| replace:: the |tp| key
.. |ttP| replace:: the |tP| key
.. |ttm| replace:: the |tm| key
.. |ttu| replace:: the |tu| key
.. |ttr| replace:: the |tr| key
.. |ttv| replace:: the |tv| key
.. |ttx| replace:: the |tx| key
.. |tty| replace:: the |ty| key
.. |ttw| replace:: the |tw| key
.. |ttsharp| replace:: the |tsharp| key
.. |ttshift| replace:: the |tshift| key
.. |ttstar| replace:: the |tstar| key
.. |ttesc| replace:: the |tesc| key
.. |ttsemicolon| replace:: the |tsemicolon| key
.. |ttdollar| replace:: the |tdollar| key
.. |tthat| replace:: the |that| key
.. |ttctrl| replace:: the |tctrl| key
.. |ttslash| replace:: the |tslash| key
.. |ttenter| replace:: the |tenter| key
"""


# -- Options for LaTeX output --------------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ("index", "Vimforhumans.tex", "Vim for humans", "Vincent Jousse", "manual"),
]
