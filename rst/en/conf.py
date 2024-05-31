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
version = "2.0"
# The full version, including alpha/beta/rc tags.
release = "2.0"

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
.. |ttreturn| replace:: ``the backspace key``
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
.. |ttq| replace:: the |tq| key
.. |ttm| replace:: the |tm| key
.. |ttu| replace:: the |tu| key
.. |ttr| replace:: the |tr| key
.. |ttv| replace:: the |tv| key
.. |ttV| replace:: the |tV| key
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
.. |ttquestion| replace:: the |tquestion| key
"""


# -- Options for LaTeX output --------------------------------------------------

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
