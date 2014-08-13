.. _plugins:

*****************
Essential plugins
*****************

Let's be clear, using |vim| without plugins is almost useless. It's the usage of plugins that will allow you to boost your productivity. You don't need a lot of them, but you need the good ones.

|vim| can of course be used without any plugin and it can be useful to know how to use it without the need to install additional plugins. Indeed, on most servers, you will have zero plugin installed. That's why, knowing how to open and save a file, knowing how to switch between files just by using default commands is very useful. However, for your writing or coding needs, plugins are mandatory.

.. _seclusty:

Managing and switching between files : *Lusty Explorer*
=======================================================

We've already talked about NerdTree in :ref:`secnerdtree`, we saw that thanks to it, we can have a project explorer in a sidebar. One of the problems of this plugin is that it was not designed to be used with the keyboard. You can for sure use the keyboard, but it will not be as efficient as a plugin developed with keyboard usage in mind.

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

If you did everything right since the beginning, your ``.vim/`` directory should now look like this:

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

The next thing to do is to deactivate *The Nerd Tree* by commenting the corresponding line like I did on the screenshot above. It will not be useful anymore as *Lusty Explorer* is a better replacement when using the keyboard.

You can see on the `lusty`_ screenshot that *Lusty Explorer* is made of two parts. The bottom part is about the current directory you're exploring and the top part is the content of this directory. The current item is highligthed. For example, on the `lusty`_ screenshot above, the current itemis the ``.vim/`` directory, highligthed in yellow (the color could be different, it depends on your theme).

*Lusty Explorer* uses something called *Fuzzy matching* that will allow you to type only a small part of the file you want to select. This part can be anything: the begining of the filename, the middle, the end or just letters composing the file to select. In the example above, if I enter ``.vimi`` in the *Lusty* window, ``.viminfo`` will be selected without the need to specify the full name. Then I just need to press |ttenter| to open the corresponding file in |vim|. You can see this particular example in the screenshot above.

.. _fuzzy:

.. image:: ../book-tex/graphics/vim-lusty-fuzzy.png


Here are some handy handy shortcuts of *Lusty Explorer*:

* |tctrl| + |tn| select the next file/directory
* |tctrl| + |tp| select the previous file/directory
* |tctrl| + |tw| go the the parent directory
* |tctrl| + |te| create a new empty file (unsaved) with the current name entered in *Lusty Explorer*. If you want to save the file, you just have to use :vimcmd:`:w`.

So *Lusty Explorer* can be used for two things: navigate your filesystem with ``,lr`` and ``,lf``, and switch between your opened files (buffers) with ``,lb``. Personally, I don't use the ``,lg`` keys a lot to search in the buffers, but it's up to you.

In order to get familiar with *Lusty Explorer* you should try to open multiple files with ``,lr`` or ``,lf``. Then, try to switch between the opened files with the help of ``,lb``. This is the combination I'm using the most on a day to day basis.

This plugin it totally mandatory and is adding a lot of value to |vim|: not using the mouse to open files. Be sure to take the time to learn how to use it, it's a great time investment.

Recherche dans les fichiers sur le disque : *Ack*
=================================================

Lorsque l'on édite un fichier appartenant à un projet plus gros contenant lui même beaucoup de fichiers, il arrive souvent de vouloir rechercher une occurrence d'une chaîne de caractères dans tous les fichiers du projet. Pour ce faire, |vim| dispose d'un plugin permettant d'utiliser *Ack* pour faire cette recherche.

*Ack* (http://betterthangrep.com/) est un programme écrit en *perl* qui remplace avantageusement le bon vieux *grep* pour effectuer des recherches dans des fichiers. Il a en revanche un désavantage par rapport à *grep* : il est rarement installé par défaut. Nous allons donc commencer par installer *Ack* avant de pouvoir aller plus loin. Cela va bien sûr dépendre de la plateforme sur laquelle vous utilisez |vim|, vous pourrez trouver différentes instructions en fonction de votre plateforme sur la page du plugin : http://github.com/mileszs/ack.vim#installation.

Pour Debian/Ubuntu : ``sudo apt-get install ack-grep``. Pour Mac Os X vous allez avoir besoin de Homebrew (http://mxcl.github.com/homebrew/) en utilisant ``brew install ack``. Pour les utilisateurs de MacPorts ça sera avec la commande ``sudo port install p5-app-ack``. Pour Windows installez Strawberry Perl (http://strawberryperl.com/) et dans le shell de commandes exécutez ``C:\>cpan App::Ack``. Vous devriez ensuite pouvoir utiliser la commande **ack** dans votre terminal de commandes en lieu et place de **grep**.

Rendez-vous sur la page du plugin ack (http://www.vim.org/scripts/script.php?script_id=2572) et téléchargez la dernière version (à l'heure où j'écris ces lignes c'est la version 0.3.1). Décompressez l'archive dan votre répertoire ``~/.vim/bundle/``, de manière à obtenir une structure de ce type :

.. code-block:: html

    bundle
    |-- ack
    |   |-- doc
    |   |   `-- ack.txt
    |   `-- plugin
    |       `-- ack.vim
    …

Comme d'habitude assurez-vous que vos modifications sont bien prises en compte en redémarrant |vim| ou en tapant :vimcmd:`:source ~/.vimrc` en mode normal.

Il va ensuite falloir ajouter quelques lignes à notre fichier |vimrc| pour faciliter d'utilisation du plugin :::

        " Paramètres par défaut pour ack
        let g:ackprg="ack -H --nocolor --nogroup --column"
        " Place un marqueur et cherche
        nmap <leader>j mA:Ack<space>
        " Place un marqueur et cherche le mot sous le curseur
        nmap <leader>ja mA:Ack "<C-r>=expand("<cword>")<cr>"
        nmap <leader>jA mA:Ack "<C-r>=expand("<cWORD>")<cr>"

Ack recherchera alors à partir du répertoire où se trouve votre fichier couramment ouvert. Vous pouvez faire quelques tests si vous le souhaitez (en supposant que votre touche |tleader| est la touche |tcomma| :

* ``,j`` *toto* : recherchera *toto* à partir du répertoire du fichier courant,
* ``,ja`` avec votre curseur sur un mot recherchera ce mot.


Le plugin Ack vous affichera les résultats dans une fenêtre que l'on appelle *Quickfix Window*, cf image suivante.

.. image:: ../book-tex/graphics/vim-ack-quickfix.png

Voici quelques commandes disponibles dans cette fenêtre :

* **o** : ouvrir (idem que <Entrée>
* **go** : voir un aperçu (ouvre le fichier mais mantient le focus sur les résultats de ack.vim)
* **t** : ouvrir dans un nouvel onglet
* **T** : ouvrir dans un nouvel onglet en arrière plan
* **h** : ouvrir en séparant la fenêtre horizontalement
* **v** : ouvrir en séparant la fenêtre verticalement
* **q** : fermer la fenêtre quickfix

À noter que par défaut Ack ne recherche que dans les fichiers qu'il reconnait comme pertinents (il ne fera pas de recherche dans les fichiers temporaires, les fichiers des gestionnaires de version, etc.). Si vous souhaitez que Ack recherche dans tous les fichiers indépendamment de leur type, vous devez spécifier l'option ``-u`` comme ceci dans votre |vimrc| :::


    " Paramètres par défaut pour ack
    let g:ackprg="ack -H -u --nocolor --nogroup --column"


Recherche de fichiers sur le disque : Ctrlp
===========================================

Non ce n'est pas pareil que Ack, relisez bien le titre. Ici nous n'allons pas chercher dans les fichiers, mais nous allons plutôt chercher des fichiers à ouvrir avec |vim|. Ça peut s'avérer très utile lorsque vous avez à travailler sur des projets où les fichiers sont éparpillés dans un grand nombre de répertoires.

Comme d'habitude nous allons commencer par installer le plugin. Une fois n'est pas coutume, le plugin dispose d'une page dédiée plutôt bien réalisée que vous trouverez ici : http://kien.github.com/ctrlp.vim/. Scrollez tout en bas pour télécharger la dernière version en "Direct Downloads". Pour les paresseux, voici un lien direct : http://github.com/kien/ctrlp.vim/zipball/master. Décompressez l'archive dan votre répertoire ``~/.vim/bundle/``, de manière à obtenir une structure de ce type :

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

Comme d'habitude assurez-vous que vos modifications sont bien prises en compte en redémarrant |vim| ou en tapant :vimcmd:`:source ~/.vimrc` en mode normal.

Nous n'avons plus qu'à ajouter un raccourci dans notre |vimrc| pour invoquer CtrlP comme le montre le listing ci-dessous. Dans mon cas j'ai choisi ``,c``, mais vous pouvez choisir ce que vous voulez.::

    let g:ctrlp_map = '<leader>c'

Voici CtrlP en action. 

.. image:: ../book-tex/graphics/vim-ctrlp.png

Il vous suffit de l'invoquer avec ``,c`` et de taper le début du fichier que vous recherchez. Quand le fichier voulu sera sélectionné en premier, il ne vous restera plus qu'à appuyer sur |ttenter| pour l'ouvrir.


À noter que CtrlP peut aussi être utilisé pour naviguer entre les fichiers ouverts (comme Lusty). Mais à l'usage, je le trouve moins pratique que Lusty. Vous pouvez aussi vous en servir pour naviguer automatiquement dans votre code en "suivant" vos fonctions grâce aux tags (comme on peut le faire dans Eclipse). C'est un trop vaste sujet pour être traité dans ce guide, mais si ça vous intéresse vous pouvez déjà consulter cet article de blog sur le sujet : http://andrew-stewart.ca/2012/10/31/vim-ctags (en anglais).

Les plugins avancés
===================

J'aurais pu faire un livre entier qui recense les plugins |vim|, mais je pense que l'intérêt aurait été assez limité. Je ne vais donc pas vous décrire plus en détails d'autres plugins. En revanche je vous donne ci-dessous une liste de plugins qui pourraient vous intéresser. Cette liste est issue d'un sondage que j'avais effectué sur Twitter demandant à mes followers quels étaient les plugins |vim| indispensables selon eux. La voici :



* **neocomplcache**. C'est un plugin de complétion automatique. Il peut compléter les noms de fichiers, les attributs du langage que vous utilisez, les snippets et encore bien d'autres choses. Le repo Github : https://github.com/Shougo/neocomplcache.
* **surround**. Ce plugin permet de gérer (changer, ajouter, supprimer) tout ce qui « entoure » : les parenthèses, les crochets, les guillemets … Par exemple vous pourrez en une combinaison de touches changer "Hello world!" en 'Hello world!' ou <q>Hello world!</q>. Le repo Github : https://github.com/tpope/vim-surround.
* **fugitive**. Si vous travaillez sur du code source vous utilisez forcément un gestionnaire de version de code source. Si ce n'est pas le cas vous pouvez aller vous cacher. Sinon si vous utilisez Git, Le plugin fugitive est pour vous. Il permet de gérer git directement dans |vim|. Le repo Github :  https://github.com/tpope/vim-fugitive
* **syntastic**. Syntastic vérifie pour vous la syntaxe de votre code source. Il va, comme peut le faire Eclipse par exemple, vous afficher vos erreurs de syntaxe directement dans |vim|. Peut vous faire gagner en temps certain si vous éditez souvent du code. Le repo Github est par ici : https://github.com/scrooloose/syntastic
* **ctags + ctrlp**. Ctags est un petit programme externe qui va parcourir votre code source et qui va ensuite vous permettre de « suivre » vos fonctions dans votre code source. Très pratique pour naviguer dans votre code source. Utilisé conjointement avec **ctrlp** décrit plus haut, il s'avère vite indispensable. Tout est expliqué ici : http://andrew-stewart.ca/2012/10/31/vim-ctags.

