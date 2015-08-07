.. _plugins:

*****************
Essential plugins
*****************

Let's be clear, using |vim| without plugins is almost useless. It's the usage of plugins that will allow you to boost your productivity. You don't need a lot of them, but you need the good ones.

|vim| can of course be used without any plugin and it can be useful to know how to use it without needing to install additional plugins. Indeed, on most servers, you will have zero plugin installed. That's why, knowing how to open and save a file, knowing how to switch between files just by using default commands is very useful. However, for your writing or coding needs, plugins are mandatory.

.. _seclusty:

Managing and switching between files : *Lusty Explorer*
=======================================================

We've already talked about NerdTree in :ref:`secnerdtree`, we have seen that thanks to it, we can have a project explorer in a sidebar. One of the problems of this plugin is that it was not designed to be used with the keyboard. You can for sure use the keyboard, but it will not be as efficient as a plugin developed with keyboard usage in mind.

The first plugin that I install when I have to use |vim| is *Lusty Explorer* (http://www.vim.org/scripts/script.php?script_id=1890). This plugin will allow you to navigate between the files on you hard drive in order to open files without using the mouse. Moreover, it will allow you to easily switch between you opened files, called buffers in |vim| terms. Let's install it.

First, download the latest version of the script here: http://www.vim.org/scripts/script.php?script_id=1890 (it's currently the 4.3 http://www.vim.org/scripts/download_script.php?src_id=17529). Then put it in your ``.vim/`` folder. It should look like this:

.. code-block:: html

    .vim
    |-- autoload
    |   `-- pathogen.vim
    `-- bundle
        |-- lusty-explorer
        |   `-- plugin
        |       `-- lusty-explorer.vim

If you have done everything right since the beginning, your ``.vim/`` directory should now look like this:

.. code-block:: html

    .vim
    |-- autoload
    |   `-- pathogen.vim
    `-- bundle
        |-- lusty-explorer
        |   `-- plugin
        |       `-- lusty-explorer.vim
        |-- nerdtree
        |   |-- doc
        |   |   `-- NERD_tree.txt
        |   |-- nerdtree_plugin
        |   |   |-- exec_menuitem.vim
        |   |   `-- fs_menu.vim
        |   |-- plugin
        |   |   `-- NERD_tree.vim
        |   `-- syntax
        |       `-- nerdtree.vim
        `-- solarized
            `-- colors
                `-- solarized.vim

Let's see how to use it. If we take a look at the documentation, here is what we find:

.. code-block:: html


    <Leader>lf  - Opens filesystem explorer.
    <Leader>lr  - Opens filesystem explorer at the directory of the current file.
    <Leader>lb  - Opens buffer explorer.
    <Leader>lg  - Opens buffer grep. 

We can see that the documentation is referring to a key named |tleader| that you need to combine with keys like *lf*, *lr*, *lb* et *lg*. The |tleader| key is a special key that we need to define in our |vimrc|. Almost each plugin will need this special key to be defined, so we will use it a lot. This is a good way to avoid collisions with the default shortcuts of |vim|.

So, we need to choose a key to be our |tleader| key. By default, |vim| uses ``\`` as a |tleader| key. I don't know about you, but for me this is not handy at all. I don't love to use my little finger too much. So I always replace the default |tleader| key with the |tcomma| key. You can of course choose another key, but lot of people are using |tcomma|: it's up to you. To tell it to |vim|, you will need to add a line in your |vimrc| as follow: ::

    let mapleader = ","

Once the modification made and taken into account by |vim| (by restarting |vim| or by typing :vimcmd:`:so ~/.vimrc` or :vimcmd:`:so $MYVIMRC` in normal mode), you should be able to do ``,lr`` (if you choosed ``,`` as your |tleader| key) and you should see something like the picture below in your |vim|.

.. _la capture d'écran de lusty: lusty_

.. _lusty:

.. image:: ../book-tex/graphics/vim-lusty.png

The next thing to do is to deactivate *The Nerd Tree* by commenting the corresponding line like I have done on the screenshot above. It will not be useful anymore as *Lusty Explorer* is a better replacement when using the keyboard.

You can see on the `lusty`_ screenshot that *Lusty Explorer* is made of two parts. The bottom part is about the current directory you're exploring and the top part is the content of this directory. The current item is highligthed. For example, on the `lusty`_ screenshot above, the current item is the ``.vim/`` directory, highligthed in yellow (the color could be different, it depends on your theme).

*Lusty Explorer* uses something called *Fuzzy matching* that will allow you to type only a small part of the file you want to select. This part can be everything: the begining of the filename, the middle, the end or just letters composing the file to select. In the example above, if I enter ``.vimi`` in the *Lusty* window, ``.viminfo`` will be selected without needing to specify the full name. Then I just need to press |ttenter| to open the corresponding file in |vim|. You can see this particular example in the screenshot above.

.. _fuzzy:

.. image:: ../book-tex/graphics/vim-lusty-fuzzy.png


Here are some handy handy shortcuts of *Lusty Explorer*:

* |tctrl| + |tn| select the next file/directory
* |tctrl| + |tp| select the previous file/directory
* |tctrl| + |tw| go the the parent directory
* |tctrl| + |te| create a new empty file (unsaved) with the current name entered in *Lusty Explorer*. If you want to save the file, you just have to use :vimcmd:`:w`.

So *Lusty Explorer* can be used for two things: navigate your filesystem with ``,lr`` and ``,lf``, and switch between your opened files (buffers) with ``,lb``. Personally, I don't use the ``,lg`` keys a lot to search in the buffers, but it's up to you.

In order to get familiar with *Lusty Explorer* you should try to open multiple files with ``,lr`` or ``,lf``. Then, try to switch between the opened files with the help of ``,lb``. This is the combination I'm using the most on a day to day basis.

This plugin is totally mandatory and adds a lot of value to |vim|: not using the mouse to open files. Be sure to take the time to learn how to use it, it's a great time investment.

Searching files on disk: *Ack*
==============================

At some point, you will need to search for a particular pattern inside your codebase. |vim| can help help you to do so with a plugin that uses *Ack* under the hood.

*Ack* (http://betterthangrep.com/) is a program written in *perl* that replaces the good old *grep* to search inside files. It's *grep*, but better. But it has one little disadvantage : it's hardly installed by default. So, as you may have guessed, the first thing to do will be to install it. As it depends on the OS you are running, you will have to refer to the installation instructions to know how to intall it for your particular case: http://github.com/mileszs/ack.vim#installation.

For Debian/Ubuntu: ``sudo apt-get install ack-grep``. For Mac OS X, first you will need Homebrew (http://mxcl.github.com/homebrew/) and then you will need to open a terminal and to type ``brew install ack``. For people using MacPorts the command will be: ``sudo port install p5-app-ack``. For Windows, install Strawberry Perl (http://strawberryperl.com/) and in a command shell execute ``C:\>cpan App::Ack``. You should now be able to use the **ack** command in your terminal instead of **grep**.

Now, we're ready for the big thing. Go to the ack plugin page (http://www.vim.org/scripts/script.php?script_id=2572) and download the last version (at the moment, it's the 0.3.1 version). Uncompress it in your ``~/.vim/bundle/`` directory so that you have a structure like the one below:

.. code-block:: html

    bundle
    |-- ack
    |   |-- doc
    |   |   `-- ack.txt
    |   `-- plugin
    |       `-- ack.vim
    …

As always, be sure that your modifications are taken into account by restarting |vim| or by entering :vimcmd:`:source ~/.vimrc` while in normal mode.

Then we will need to add some lines to our |vimrc| file to ease the use of the plugin :::

        " Default params for ack
        let g:ackprg="ack -H --nocolor --nogroup --column"
        " Add a mark and search
        nmap <leader>j mA:Ack<space>
        " Add a mark and search for the word under the cursor
        nmap <leader>ja mA:Ack "<C-r>=expand("<cword>")<cr>"
        nmap <leader>jA mA:Ack "<C-r>=expand("<cWORD>")<cr>"

Ack will start the search from the directory of the file currently opened. Here are some examples (supposing that your |tleader| key is the |tcomma| key):

* ``,j`` *toto* : will search for *toto* starting from the directory of the current file,
* ``,ja`` with your cursor on a word will search for this word.


The results will be displayed in a window called the *Quickfix Window*, as you can see below.

.. image:: ../book-tex/graphics/vim-ack-quickfix.png

Here are some commands available inside this window:

* **o** : open (same as <Enter>)
* **go** : preview display (open the file but keep the focus on the ack.vim results)
* **t** : open in a new tab
* **T** : open in a new background tab
* **h** : open and split the window horizontally
* **v** : open and split the window vertically
* **q** : close the quickfix window

By default, Ack doesn't search in files that are not relevant. For example, it will not search in temp files or in files used by your favorite revision control system. If you want Ack to search into any file, independantly of its type, you need to specify the ``-u`` option in your |vimrc| :::

    " Default params for Ack
    let g:ackprg="ack -H -u --nocolor --nogroup --column"


Searching files on disk: Ctrlp
==============================

Here we will not search inside files like we did with Ack. We will rather search for files to open with |vim|. It can be very handy when you're working on a project where files are everywhere in the directory tree.

As always, we will start by installing the plugin. For once, this plugin has a dedicated page that you will find here: http://kien.github.com/ctrlp.vim/. Scroll to the bottom to download the latest version in the "Direct Downloads" section. For the laziest, here is the direct link: http://github.com/kien/ctrlp.vim/zipball/master. Uncompress the archive in your ``~/.vim/bundle/`` directory, so that you get something like that:

.. code-block:: html

    bundle
    |
    …
    |-- ctrlp
    |   |-- autoload
    |   |   |-- ctrlp
    |   |   |   |-- bookmarkdir.vim
    |   |   |   |-- buffertag.vim
    |   |   |   |-- changes.vim
    |   |   |   |-- dir.vim
    |   |   |   |-- line.vim
    |   |   |   |-- mixed.vim
    |   |   |   |-- mrufiles.vim
    |   |   |   |-- quickfix.vim
    |   |   |   |-- rtscript.vim
    |   |   |   |-- tag.vim
    |   |   |   |-- undo.vim
    |   |   |   `-- utils.vim
    |   |   `-- ctrlp.vim
    |   |-- doc
    |   |   `-- ctrlp.txt
    |   |-- plugin
    |   |   `-- ctrlp.vim
    |   `-- readme.md
    …

As always, be sure that your modifications are taken into account by restarting |vim| or by entering :vimcmd:`:source ~/.vimrc` while in normal mode.

Now we need to add the shortcut to our |vimrc| to invoke CtrlP like in the listing below. Personnaly, I've chosen ``,c``, but you can choose whatever you want.::

    let g:ctrlp_map = '<leader>c'

Here is CtrlP in action.

.. image:: ../book-tex/graphics/vim-ctrlp.png

Launch it with ``,c`` and then type the name of the file you want to search. When the searched file will be selected first, you will just have to press |ttenter| to open it.

CtrlP can be used for navigating through the opened files (like Lusty), but I find Lusty handier for that. You can also use to navigate directly through your code by "following" your functions thanks to something called the tags (like you can do when using Eclipse). It's a too big topic for the scope of this book, but if you're interested you can read this blog article on the topic: http://andrew-stewart.ca/2012/10/31/vim-ctags.


Advanced plugins
================

Writing an entire book about the |vim| plugin is for sure something doable, but I have to admit that I don't have enough courage. So, I will stop here with the plugins thing. However, below is a list of some plugins that may interest you. This list comes from a poll I did on Twitter asking my followers what were the most useful |vim| plugins to them. Here it is:

* **neocomplcache**. It's an automatic completion plugin. It can autocomplete file names, language attributes, snippets and a lot more. The Github repo: https://github.com/Shougo/neocomplcache
* **surround**. With this plugin, you can manage (change, add, delete) everything that "surrounds": parenthesis, brackets, quotes, … For example, you will be able to change "Hello world!" with 'Hello world!' or <q>Hello world!</q> with a simple key combination. The Github repo: https://github.com/tpope/vim-surround
* **fugitive**. If you work with source code, you have to use a version control system. If it's not the case, you can go hide yourself. Otherwise, if you're using Git, fugitive was made for you. It allows you to manage your git command directly inside |vim|. The Github reop:  https://github.com/tpope/vim-fugitive
* **syntastic**. Syntastic will check the syntax of your source code. It will, like Eclipse does it for exemple, directly display your syntax errors in your |vim|. It can be a time saver if you edit a lot of code. Github repo : https://github.com/scrooloose/syntastic
* **ctags + ctrlp**. Ctags is a small external program that will parse your source code and allow you to "follow" your functions calls through your source code. Very useful to navigate into your source code. Used with **ctrlp** described above, it will soon become a must. Everything is explained here: http://andrew-stewart.ca/2012/10/31/vim-ctags.
