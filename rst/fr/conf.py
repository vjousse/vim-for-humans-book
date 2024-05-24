# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Vim pour les humains"
copyright = "2024, Vincent Jousse"
author = "Vincent Jousse"


# The short X.Y version.
version = "2.0"
# The full version, including alpha/beta/rc tags.
release = "2.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "fr"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    "css/custom.css",
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "solarized-light"

highlight_language = "vim"


rst_prolog = """
.. role:: vimcmd
    :class: pre
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
.. |tesc| replace:: ``Esc (Échap)``
.. |tsemicolon| replace:: ``;``
.. |tcolon| replace:: ``:``
.. |tctrl| replace:: ``Control``
.. |tapos| replace:: ``'``
.. |tslash| replace:: ``/``
.. |tshift| replace:: ``Shift``
.. |tenter| replace:: ``Entrée``
.. |tstar| replace:: ``*``
.. |tsharp| replace:: ``#``
.. |tleader| replace:: ``<Leader>``
.. |tcomma| replace:: ``,``
.. |tquestion| replace:: ``?``
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
.. |tq| replace:: ``q``
.. |tu| replace:: ``u``
.. |tr| replace:: ``r``
.. |tv| replace:: ``v``
.. |tV| replace:: ``V``
.. |tw| replace:: ``w``
.. |tx| replace:: ``x``
.. |tX| replace:: ``X``
.. |ty| replace:: ``y``
.. |tyty| replace:: ``yy``
.. |ttreturn| replace:: ``la touche Retour``
.. |ttc| replace:: la touche |tc|
.. |ttd| replace:: la touche |td|
.. |tte| replace:: la touche |te|
.. |tth| replace:: la touche |th|
.. |tti| replace:: la touche |ti|
.. |ttj| replace:: la touche |tj|
.. |ttk| replace:: la touche |tk|
.. |ttl| replace:: la touche |tl|
.. |ttn| replace:: la touche |tn|
.. |ttN| replace:: la touche |tN|
.. |tto| replace:: la touche |to|
.. |ttp| replace:: la touche |tp|
.. |ttP| replace:: la touche |tP|
.. |ttq| replace:: la touche |tq|
.. |ttm| replace:: la touche |tm|
.. |ttu| replace:: la touche |tu|
.. |ttr| replace:: la touche |tr|
.. |ttv| replace:: la touche |tv|
.. |ttV| replace:: la touche |tV|
.. |ttx| replace:: la touche |tx|
.. |tty| replace:: la touche |ty|
.. |ttw| replace:: la touche |tw|
.. |ttsharp| replace:: la touche |tsharp|
.. |ttshift| replace:: la touche |tshift|
.. |ttstar| replace:: la touche |tstar|
.. |ttesc| replace:: la touche |tesc|
.. |ttsemicolon| replace:: la touche |tsemicolon|
.. |ttdollar| replace:: la touche |tdollar|
.. |tthat| replace:: la touche |that|
.. |ttctrl| replace:: la touche |tctrl|
.. |ttslash| replace:: la touche |tslash|
.. |ttenter| replace:: la touche |tenter|
.. |ttquestion| replace:: la touche |tquestion|
"""

latex_engine = "lualatex"
latex_additional_files = ["_templates/vimforhumans.sty"]


# See https://tex.stackexchange.com/questions/616277/how-to-set-an-inline-tcbox-height-to-a-fixed-height-1em
latex_custom = r"""
\usepackage{vimforhumans}
\usepackage[most]{tcolorbox}
\makeatletter
\newcommand\mystrut{\rule[0pt]{0pt}{0.6em}}
\tcbset{on line,
        boxsep=0pt, left=2pt,right=2pt,top=1pt,bottom=1pt,
        colframe=white,colback=gray!20, fontupper={\ttfamily\mystrut}
        }
\let\OldSphinxcode\sphinxcode
\renewcommand{\sphinxcode}[1]{\OldSphinxcode{\tcbox{#1}}}
\makeatother
"""


latex_elements = {
    # Always use A4 paper.
    "papersize": "a4paper",
    # Make sure to use babel instead of polyglossia.
    "babel": r"\usepackage{babel}",
    # Uniformization of chapter style, disable Sphinx default.
    "fncychap": "",
    # Use names for colors.
    "passoptionstopackages": r"\PassOptionsToPackage{svgnames,table}{xcolor}",
    # Clear default font config.
    "fontpkg": "",
    # Add custom preamble after 'hyperref' and 'sphinx'.
    "preamble": latex_custom,
    "sphinxsetup": "verbatimwithframe=true, VerbatimColor={RGB}{253,246,227}",
}
