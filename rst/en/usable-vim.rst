*********************
Having a usable |vim|
*********************

This is maybe a surprising approach for you, but for me, the first thing to do is to have a |vim| usable by a normal human being. It seems that everybody agrees that |vim| is a very **powerful editor**. And I think that you will agree too if I say that, by default, |vim| is totally unusable. Let's be honest, without a decent minimal configuration, using |vim| is **counterproductive**.

In my humble opinion, it's the first obstacle to tackle before anything else. This is what all the trendy editors like TextMate, Sublime Text, Notepad++ or Netbeans are proposing: a default environment usable as it is, even if we don't use its full potential for now.

Here is what a default |vim| is missing (and why **most of people are giving up** before they can really see the power of |vim|):

**Default configuration**
    You can configure |vim| thanks to a file named |vimrc|. This file is, obviously, totally empty by default. The first thing to do will be to have a |vimrc| file with a minimal configuration.

**Syntax highlighting**
    By default, |vim| is white and ugly. To fix that, we will use the `Solarized theme <http://ethanschoonover.com/solarized>`_. If your goal is to be efficient, it's the best theme available out there (across all text editors), period. The beautiful image below will give you an idea of what it looks like (with the dark and the light theme). Personally, I'm using the dark theme.

    |solarized|

.. |solarized| image:: ../book-tex/graphics/solarized-yinyang-mini.png

**File explorer**
    If your are using |vim| along with a graphical interface (I suppose it's the case for 99% of you) you will by default have a ``File`` menu available. This menu should allow you to open a file. It's, for sure, a good start. But having a file explorer a la Netbeans or Textmate can be very handy. To mimic the same behavior, we will be using `The NERD Tree <http://www.vim.org/scripts/script.php?script_id=1658>`_. Be aware that, once you will have read this guide, you will not need the mouse anymore.


This chapter is mandatory if you have very few (or not at all) experience with |vim|. By the end of the chapter, you will have a |vim| usable on a daily basis. It should be enough to then be able to learn it gradually. Because, of course, there is no magic, you will have to practice to be able to learn |vim|, the sooner, the better.

However, if your are already familiar with |vim| and don't use the mouse anymore, you can skip this chapter. But be sure to give *Solarized* a try, you would be missing something otherwise.


.. _insertmode:

Essential preamble: the insert mode
===================================

Let's be totally crazy. We will try to create the |vimrc| configuration file with |vim| itself. As I said earlier, the sooner you start to use |vim|, the better. I told you it would be totally crazy.

The first thing to do will certainly be to install a |vim| version for your operating system. If you are using a Mac, give `MacVim <http://code.google.com/p/macvim/>`_ a try, it's the best |vim| port for Mac without any doubt. If your are using GNU/Linux or any other "Unix-like" system, you should have *gVim* available, or at least easily installable using your package management system. Be sure to install the __full__ version (ie. with ruby and lua support). For ubuntu, the package is called `vim-nox`. For Mac OS X, MacVim has already all what you need builtin. For Windows, it seems that there is a version available on the official |vim| website (http://www.vim.org/download.php), but I did not test it.

When you will start |vim|, you should see a welcome text asking you to help poor children in Uganda (or something along the lines). 

.. image:: ../book-tex/graphics/en/vim-uganda.png

This text will disappear as soon as we will be writing text in |vim|. 

We will start by adding a comment in the header of the file to specify the author of the document (should be you). To be able to type text, the first thing to do will be to press |tti| (the cursor should have changed). The welcome text should have disappeared and you should have `a blank page`_ looking like the image below:

.. _a blank page:

.. image:: ../book-tex/graphics/en/vim-new.png

**On a side note**: if you don't really understand what you did and |vim| is displaying red messages at the bottom left or doesn't seem to react as it should when your pressing |tti|, don't panic. Pressing multiples times on |ttesc| (two times should be enough) should bring |vim| to its default mode, the *Normal mode*. Then it should behave as you would expect again.

You should know be able to write down `the comment below`_:

.. _the comment below:

::

    " VIM Configuration - Vincent Jousse

You will have noticed that comments in *VimL* (the name of the |vim| programing language) start with a :viml:`"`. Then press |ttesc| to come back to the default mode (the normal mode) of |vim|. That's all, you are done. Here is a screenshot of what your |vim| should look like now:

.. image:: ../book-tex/graphics/en/vim-first-comment.png

I can already hear you: all that fuss for what? Well, yes. And you even don't know how to save a file. But all these things are logical that I'm gonna explain to you. One of the advantages of |vim| is that, usually, it is logical. Once you will have understood the logic behind it, all will be crystal clear for you (at least I hope).

By default, when you start |vim|, you are presented with its default mode. This mode is called the *Normal mode*. The purpose of this mode is not to write text (for that, you will have the *Insert mode*), but only to move the cursor and to manipulate text. The power of |vim| is coming from the combination of these two modes (other modes exist, but it's not the topic for now). You will need some time and some practice to realize the power it's giving to you, so you will just need to trust me in the meantime.

If you are asking yourself why those modes, why by default we can't even write down some text and why we are making things more complicated than they should, the next chapter is for you.

.. _modes:

Modes: the powerful |vim| secrets
=================================

I suppose you will agree if I say that, if you want to learn |vim|, it's to be more efficient when writing/manipulating text or code. To be more efficient when writing text, there is not many solutions. There is only one actually: you need to move your hands as less as you can (even not at all) and only move your fingers.

To do so, of course, you will need to do without your mouse. In addition to being slow, the move keyboard -> mouse and then mouse -> keyboard is really bad for your articulations. It's often the cause of musculoskeletal disorders. Maybe you are still young and don't know what I'm talking about. But believe me, you will have such problems one day or another (often sooner than what you think). If your are in front of your computer all day long, don't neglect those possible troubles, you may regret it someday. `According to Wikipedia <http://en.wikipedia.org/wiki/Musculoskeletal_disorder>`_, it's actually the most common professional disease.

You will need to forget the move of your right hand toward the directional keys (left/right/bottom/top) too. It's a waste of time and it's completely unneeded with |vim|.

So what do you have the right to do? Not a lot to be honest (but it's for your own good), you can only leave your hands on the home row `as you can see on the picture below`_.

.. _as you can see on the picture below:

.. figure:: ../book-tex/graphics/hand-position.png
   
   Home row, QWERTY keyboard

   *Illustration by Cy21 - CC-BY-SA-3.0* (http://www.creativecommons.org/licenses/by-sa/3.0) or GFDL (http://www.gnu.org/copyleft/fdl.html), via Wikimedia Commons http://commons.wikimedia.org/wiki/File:Typing-home-keys-hand-position.svg

You will also find on each keyboard some marks on the letters F and J, the goal of these marks is to give a landmark for the position of your fingers (the indexes) on the home row of the keyboard.

Trying to move as less as possible the hands from the keyboard is the reason for having a *normal* mode and an *insert* mode in |vim|. When switching from one to the other, the keys under your fingers will sometimes allow you to move the cursor and to manipulate text: copy/paste, deletion, … (it's the normal mode), sometimes they will allow you to select some text (it's the *visual mode*) and sometimes to insert some text (it's the *insert* mode). And of course, all of that is possible without the extensive use of keys combinations like *Ctrl + key* that are very bad for your fingers (*Emacs*, this on is for you).

By default, we can switch from the *insert* mode to the *normal* mode by pressing |ttesc|, but it will be one of the first things we will change: |ttesc| is to far from your fingers on actual keyboards.

To switch from *normal* mode to *insert* mode, we can for example press |tti|. We will later learn that there are other ways to do so too. For example, to enter the *insert* mode and to then create a new line below the current one (no matter where is your cursor on the line), we will use |tto| while in *normal* mode.

I will talk again about this subject later in ":ref:`moving`", but if your are not ready, at some point, to do without your mouse and the directional keys to edit text, I would recommend you to stop learning |vim| right now. It's as simple as that. You can leverage the full power of |vim| only by getting rid of the mouse and by moving your hand as little as possible.

If you want to go further, you can buy an orthogonal keyboard like `TypeMatrix <http://www.typematrix.com>`_. It's the keyboard I'm currently using, and my fingers are thanking me everyday.

The ultimate change would be to switch your keyboard layout to a more efficient one like `Colemak <http://colemak.com/>`_. But it's another story.


The lifesaver default configuration
====================================

Let's get serious and try to have a usable |vim|. We will start by editing the default configuration file |vimrc| and by entering default values that any sane guy would love to find in it.

You have to place this file in your home directory. It should be */home/your_user/.vimrc* if your are using Linux, */Users/your_user/.vimrc* if your are using Mac OS X. Generally speaking, it should be in you home directory under *~/.vimrc*. If you are using Windows, you can create a file named *_vimrc* that you have to put in your *%HOME%* directory. This directory is obviously not the same across the different Windows versions. Usually, it's the directory just before your directory *My Documents*. More information is `available on Wikipedia <http://en.wikipedia.org/wiki/Home_directory#Default_Home_Directory_per_Operating_System>`_ if you want.


I've directly commented all the lines in the code itself. Nothing fancy here, you should just be asking yourself why all of this is not available by default.

.. include:: ../../vim-for-humans/en/firstconfig/vimrc
   :code:


For those who did a copy/paste (and you should be one of those), you just have to save your newly created file. We want to put it in our home directory, so you have to save it as `~/.vimrc`. When using Mac OS X and Linux, *~* is the home directory of the current user. But be careful, when using Linux and Mac OS X the files starting with a ``.`` are hidden files. So don't be surprised to not see by default your `~/.vimrc` in your file explorer.

For people using the mouse, you will just have to use the `File` menu and then the `Save as` one. Save the file under the name `.vimrc` in your home directory. For those who want to use the keyboard you will just have to type :vimcmd:`:sav ~/.vimrc` (be sure to be in the *Normal* mode by pressing |ttesc| before). To save your further modifications, just use the menus with the mouse or type :vimcmd:`:w` when in *Normal* mode.

I have uploaded this configuration file directly on *Github*. You can download or copy/paste it directly from: http://vimebook.com/link/en/firstconfig.

Below is a screenshot of |vim| (macvim) `after your first configuration`_.

.. _after your first configuration:

.. figure:: ../book-tex/graphics/en/vim-first-config.png

   |vim| after your first configuration.

Notice the line numbers on the left and the position (coordinates) of the cursor at the bottom right.

Well, it's a good start, but we now need more colors. Let's go!

And now, the color!
===================

First, we need to enable syntax highlighting in the configuration file. Add these lines at the end of your |vimrc| configuration file::

    " Enable syntax highlighting
    syntax enable
    " Enable file specific behavior like syntax highlighting and indentation
    filetype on
    filetype plugin on
    filetype indent on

You should have a |vim| looking like the picture below.


.. figure:: ../book-tex/graphics/vim-syntax-hl.png

   Default syntax highlighting.

For the time being, the easiest way to test the modifications you made to your |vimrc| file is to restart |vim|. If you want to use |vim| like a boss right now, you can type in normal mode :vimcmd:`:so ~/.vimrc` or :vimcmd:`:so $MYVIMRC`. It will reload the configuration without the need to restart |vim|. :vimcmd:`:so` being a shortcut for vimcmd:`:source`. 

This is a good first step, it's time to turn to the use of a theme.

Themes will allow you to have a nicer |vim| than the default one. A theme will change the background color of |vim| and the colors used for the syntax highlighting. As I said earlier, we will use the *Solarized* theme http://ethanschoonover.com/solarized (with dark or light background, it will be up to you).

To install it, you will first need to create a directory called `.vim` in the same directory than your |vimrc| (that is to say, in your home directory). Note that when using Windows, the `.vim` directory is called `vimfiles`. Each time I'll be speaking of the `.vim` directory, it will be the `vimfiles` directory for people using Windows. In this `.vim` directory, create a sub directory named `colors`. Then, download the *Solarized* theme file https://raw.github.com/altercation/vim-colors-solarized/master/colors/solarized.vim (it's the same file for the light and the dark version) and copy it in your `vim/colors/` directory. You `.vim` directory should look like the picture below.

.. figure:: ../book-tex/graphics/solarized-tree.png

   Content of the .vim directory with Solarized.

Then enable the Solarized theme in your |vimrc| like shown in the code below.::

    " Use the dark version of Solarized
    set background=dark
    colorscheme solarized

To test the light theme, you just have to change `dark` with `light` (for the `background` property).

Here is a preview of the two versions (personally, I prefer the dark one).

.. figure:: ../book-tex/graphics/vim-solarized-dark.png

   The dark  *Solarized* theme.


.. figure:: ../book-tex/graphics/vim-solarized-light.png

   The light  *Solarized* theme.


A bonus (if you don't use |vim| directly in your terminal) would be to choose a font that suits your needs a little bit better. This is of course optional, but I suppose that some of you are sensible to such things.

If your are using Mac OS X, I recommend the `Monaco` font that is quite friendly. Add the following lines to your |vimrc| to use it: ::

    set guifont=Monaco:h13
    set antialias

You can of course change `h13` with `h12` if you want a smaller font (or with `h14` if you want a bigger one).

Under Linux I am using the `DejaVu Sans Mono` font: ::

    set guifont=DejaVu\ Sans\ Mono\ 10
    set antialias

You can of course change the font size as you want. To have the list of all the available fonts for your system type :vimcmd:`:set guifont:*` in normal mode.

You will find the full version of the configuration file for this chapter online http://vimebook.com/link/en/syntaxhlconfig. I will not spend more time talking about the fonts as it's dependant of your operating system and not of |vim|.


Our first plugin: the file explorer
===================================

Here we go, we have a nice |vim| that we can actually use with pretty colors. It's a good firt step, but now, it would be cool to be able to open files without having to do `File -> Open` using the menu bar. This is the perfect opportunity to install our first plugin: a file explorer. We will use a two-step approach here: first we will install a plugin manager and then we will install the plugin using this plugin manager. By default |vim| doesn't come with a plugin manager and, believe me, if you don't install one your |.vim| directory will soon be a real mess. So let's get started.

Plugin manager: Pathogen
------------------------

*Pathogen* (https://github.com/tpope/vim-pathogen/) is typically the kind of plugin that you discover after having already configured your |vim|. And then you ask yourself: « Why did I not start this way? ». Fortunately, I have a good news for you: we will start the right way.

First of all, let's start with a little explanation about how to install plugins using |vim|. Plugins are installed by copying files (most of the time with the *\*.vim* extension) in subdirectories of your |.vim| directory. By the way, We've already created a subdirectory called `colors` that contains our first coloration plugin using the Solarize theme.

The main problem with this approach is that the plugins are not isolated. So you will have to copy files from different plugins in the same directory and you will soon not be able to know from what plugin a file is coming from. No need to say that when you will want to remove or update a plugin, it will be a nightmare to know where the files are located.

That's why *Pathogen* is especially useful, it will allow each plugin to be located in a separate directory. Here is an example of a |.vim| directory before and after the usage of *Pathogen*:

.. figure:: ../book-tex/graphics/pathogen-tree.png

   |.vim| before and after Pathogen

You are totally right if you find that the version with *Pathogen* is using more directories. But believe me, those directories will save your life later. You will be able to easily remove and update plugins and you will be able to use *git* (or any other SCM software) to manage your plugins / submodules / dependencies.

Let's start by installing *Pathogen*. Create a directory called `autoload` in your |.vim| directory. Download `pathogen.vim` ( https://raw.github.com/tpope/vim-pathogen/master/autoload/pathogen.vim ) and copy it to your `autoload` directory. For the Unix/Mac OS X/Linux user, here is how to install it (if you don't have `curl`, you can use `wget -O -` instead:

.. code-block:: bash

    # Create the autoload directory
    mkdir -p ~/.vim/autoload 

    # Download and install Pathogen
    curl -so ~/.vim/autoload/pathogen.vim \
        https://raw.github.com/tpope/vim-pathogen/master/autoload/pathogen.vim

From now on, we will install our plugins directly in the `.vim/bundle` directory that you will create right now:

.. code-block:: bash

    # Create the bundle directory used by Pathogen
    mkdir -p ~/.vim/bundle


All you have to do is to activate *Pathogen* in your |vimrc| file and voila. We will put the following lines at the very beginning of the |vimrc| file, right after the `set nocompatible` line. It is mandatory to put the code at the **beginning** of your |vimrc| file, otherwise it will not work.::

    " Activate pathogen
    call pathogen#infect()

Since charity begins at home, we will tidy up our install by using *Pathogen* with our *Solarized* plugin. We just have to create a directory called `solarized` in your newly created `.vim/bundle` directory. You could name it as you want as any subdirectory of the `bundle` directory will be considered as a plugin directory. Then, we will move our previously created `colors` directory in the `solarized` directory as follow:

.. code-block:: bash

    # Create the plugin directory for solarized
    mkdir ~/.vim/bundle/solarized
    # Move solarized to the bundle dir
    mv ~/.vim/colors ~/.vim/bundle/solarized

Currently, *Pathogen* is still the most used plugin manager for |vim|. But recently, a new challenger has arrived, it's called Vundle https://github.com/gmarik/vundle. I chose to use *Pathogen* here because it's the one you will hear about the most often. But you have to know that Vundle is an interesting alternative: it's compatible with Pathogen and you can manage your plugins directly from internet (from github, the vim website, …). For those familiar with Ruby, it's Bundler (http://gembundler.com) for |vim|.

Our |vim| is almost ready to be used on a daily basis. We are just missing an handy way to explore the files of a project. We will use *The NERD Tree* for that.

.. _secnerdtree:

The NERD Tree: a file explorer
------------------------------

The NERD Tree is a plugin that will allow you to display your directory and file tree directly in |vim|, just like in *TextMate*, *Sublime Text* or *Eclipse/NetBeans*. This is not a mandatory plugin if you want to control everything using the keyboard (I don't use it anymore myself), but it's very handy when you are starting with |vim|.

The other solution that we will see in the :ref:`plugins` chapter will be to use the *Ctrl-p* or *Command-t* plugins to find files and to use the *LustyExplorer* and *LustyJuggler* plugins to navigate between the files. Indeed, having to visualize the whole file tree to find a file is a lot slower than to find a file by its name. In the meantime, The NERD Tree will allow us to use |vim| with a *normal* file explorer where you can click with the mouse.

First, we will prepare *Pathogen* in order to install all the files needed by *The NERD Tree*.

.. code-block:: bash

    # Create the directory for The NERD Tree
    mkdir ~/.vim/bundle/nerdtree

Then, download the latest *.zip* available on the plugin page http://www.vim.org/scripts/script.php?script_id=1658. At the time of this writing, the latest version is the 4.2.0 that you can directly download using this url: http://www.vim.org/scripts/download_script.php?src_id=17123.

Unzip the file and copy the content in the newly created ``~/.vim/bundle/nerdtree`` directory. The directory structure of your ``nerdtree`` directory should look like the one below:

.. code-block:: html

    nerdtree
    |-- doc
    |   `-- NERD_tree.txt
    |-- nerdtree_plugin
    |   |-- exec_menuitem.vim
    |   `-- fs_menu.vim
    |-- plugin
    |   `-- NERD_tree.vim
    `-- syntax
        `-- nerdtree.vim

Then, you will need to activate the plugin. You can do it manually by typing :vimcmd:`:NERDTree` in normal mode. If you prefer to activate *The NERD Tree* every time you open your |vim|, add these lines to your |vimrc|: ::

    " Activate the NERDTree when launching vim
    autocmd vimenter * NERDTree

I have to admit that this command is a little bit obscure. Actually it means: every time you open vim (``vimenter``), no matter what is the type of the file (``*``), launch *The NERD Tree*  (``NERDTree``).


Nothing special then, *The NERD Tree* will display the tree of the directory where you've launched |vim| as you can see on the picture below. You can use your mouse and/or your keyboard to move inside *The NERD Tree*.

.. figure:: ../book-tex/graphics/vim-nerdtree.png

   |vim| with *The NERD Tree*.

You can also run commands (create, copy a file) by typing |ttm| when you are inside *The NERD Tree*. To switch between the *NERD Tree* window and your file window with your keyboard, use ``Ctrl + w`` and then ``w``. That is to say, hold the ``Control (Ctrl)`` key and at the same time press the ``w`` key. You can then release everything and press ``w`` again. This shortcut is valid to switch between any |vim| window (it's not a shortcut specific to *The NERD Tree*).


Here we go
==========

Now, you've done the hardest part. Well, almost. We've just covered what is sorely lacking in |vim|: a sensible default configuration. I'm not saying that you now have the best editor out there, but at least, you should be able to use |vim| as any other *normal* text editor that you do not yet know all the possibilities. I recommend, at this stage, to start to use |vim| in your everyday life. Feel free to use the mouse and the menus for now. The primary goal here is to reduce the negative impact that |vim| could have on your daily productivity, if not configured properly. You will gradually learn the keyboard shortcuts when the time will come.

We will now discuss what make the uniqueness of |vim|: the way modes are handle and the commands to manipulate text. The ball is in your court now: either you are willing to change your habits and move to another level of efficiency with |vim|, or else using |vim| as an improved notebook is right for you (in this case, you can stop there). It's up to you !
