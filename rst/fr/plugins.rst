.. _plugins:

**************************
Les plugins indispensables
**************************

Soyons clair, |vim| sans ses plugins, c'est comme Milan sans Rémo (© François Corbier - Sans ma barbe - http://www.bide-et-musique.com/song/149.html) : ça ne rime à rien. C'est grâce aux plugins que |vim| va pouvoir pleinement exprimer toute sa puissance et vous élever à un autre niveau de productivité. Vous n'avez pas besoin d'en avoir des mille et des cents, mais quelques uns savamment choisis devraient faire l'affaire.

Qu'on ne se méprenne pas, |vim| peut bien sûr s'utiliser sans plugins. Il peut d'ailleurs s'avérer utile de savoir faire les manipulations de base sans avoir besoin d'installer de plugin, car c'est souvent le cas sur des serveurs : il n'y a aucun plugin d'installé. Dans ce cas là, savoir ouvrir, sauvegarder sous, passer d'un fichier à l'autre avec les commandes de |vim| par défaut peut vous sauver la mise. En revanche, dans votre travail quotidien de rédaction ou de code, les plugins sont indispensables pour pleinement tirer partie de |vim|.

.. _seclusty:

Naviguer sur le disque et entre les fichiers : *Lusty Explorer*
===============================================================

Nous avons déjà vu NerdTree dans :ref:`secnerdtree` qui permettait d'avoir un explorateur de projet dans une fenêtre latérale de |vim|. Le problème de ce plugin est qu'il n'est pas fait pour être utilisé au clavier. Certes vous pouvez utiliser le clavier, mais il ne sera pas aussi efficace que les plugins pensés uniquement pour une utilisation au clavier.

Personnellement, le premier plugin que j'installe partout où j'ai à utiliser |vim|, c'est *Lusty Explorer* (http://www.vim.org/scripts/script.php?script_id=1890). Ce plugin va vous permettre de naviguer sur votre disque dur pour ouvrir facilement des fichiers en se passant de la souris. Il va aussi permettre de naviguer rapidement entre vos différents fichiers déjà ouverts (vos buffers en jargon |vim|). Commençons par l'installer.

Rendez-vous sur l'url du script http://www.vim.org/scripts/script.php?script_id=1890 et téléchargez la dernière version (c'est actuellement la 4.3, http://www.vim.org/scripts/download_script.php?src_id=17529). Faites ensuite le nécessaire dans votre répertoire ``.vim/`` pour qu'il ressemble à la structure ci-dessous :

.. code-block:: html

    .vim
    |-- autoload
    |   `-- pathogen.vim
    `-- bundle
        |-- lusty-explorer
        |   `-- plugin
        |       `-- lusty-explorer.vim

Si vous avez suivi tout ce que l'on a fait depuis le début votre répertoire ``.vim/``, il devrait maintenant ressembler à cela :

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

Reste à voir comment l'utiliser. Si l'on se réfère à la documentation, voilà ce que l'on trouve (traduit en français) :

.. code-block:: html

    <Leader>lf  - Ouvre l'explorateur de fichiers.
    <Leader>lr  - Ouvre l'explorateur de fichiers à partir du répertoire du fichier courant.
    <Leader>lb  - Ouvre l'explorateur de buffers.
    <Leader>lg  - Ouvre la recherche dans les buffers.

On voit qu'il est fait mention d'une touche nommée |tleader| qu'il faut ensuite faire suivre d'autres touches comme *lf*, *lr*, *lb* et *lg*. Cette touche |tleader| est une touche spéciale que l'on définit dans son fichier |vimrc|. Elle sera énormément utilisée par tous les plugins, beaucoup des commandes de ces derniers commenceront par la touche |tleader|. C'est un moyen d'éviter les collisions avec les raccourcis par défaut de |vim|.

Il faut donc choisir une touche |tleader|. Par défaut, |vim| utilise ``\`` comme touche |tleader|. Sur nos claviers francophones c'est une très mauvaise idée d'utiliser cette touche car elle n'est pas pratique du tout. La plupart des utilisateurs de |vim| la remplace par la touche |tcomma|. Elle est directement accessible sous l'index de la main droite ce qui en fait une parfaite candidate. Pour spécifier cela à |vim| il va falloir rajouter une ligne dans votre fichier |vimrc|, à savoir :::

    let mapleader = ","

Une fois la modification effectuée et prise en compte (en redémarrant |vim| ou en tapant :vimcmd:`:so ~/.vimrc` ou :vimcmd:`:so $MYVIMRC` en mode normal), vous devriez être en mesure de taper ``,lr`` et d'avoir le même style de résultat que sur la figure ci-dessous.

.. _la capture d'écran de lusty: lusty_

.. _lusty:

.. image:: ../book-tex/graphics/vim-lusty.png

Je vous conseille maintenant de désactiver *The Nerd Tree* (en commentant la ligne au dessus du *mapleader* comme je l'ai fait dans la figure suivante, il ne vous servira plus à grand chose, *Lusty Explorer* le remplace à merveille.

Vous pouvez constater sur `la capture d'écran de lusty`_ qu'il y a deux parties à *Lusty Explorer*. La partie basse vous indique le répertoire que vous êtes en train d'explorer et la partie haute liste le contenu de ce répertoire. En surbrillance se trouve l'élément couramment sélectionné. Dans le cas de `la capture d'écran de lusty`_ c'est le répertoire ``.vim/`` en jaune  (la couleur pourra être différente en fonction de votre thème).

*Lusty Explorer* utilise une fonctionnalité de *Fuzzy matching* qui va vous permettre de ne taper qu'une partie d'un nom de fichier pour le sélectionner. Dans mon exemple, si, dans la fenêtre de *Lusty*, je saisi ``.vimi`` il va me sélectionner le fichier ``.viminfo`` sans que j'ai à lui spécifier le nom entier, je n'aurais ensuite plus qu'à appuyer sur |ttenter| pour ouvrir le fichier dans |vim|. La figure suivante vous montre l'exemple en question.

.. _fuzzy:

.. image:: ../book-tex/graphics/vim-lusty-fuzzy.png


*Lusty Explorer* dispose en plus de quelques raccourcis bien pratiques pour utiliser le navigateur de fichiers :

* |tctrl| + |tn| pour sélectionner le fichier/répertoire suivant
* |tctrl| + |tp| pour sélectionner le fichier/répertoire précédent
* |tctrl| + |tw| pour descendre au répertoire parent
* |tctrl| + |te| crée un nouveau fichier vide (non sauvegardé sur le disque) avec le nom spécifié actuellement dans *Lusty Explorer*. Vous n'aurez plus qu'à utiliser :vimcmd:`:w` pour écrire le contenu du fichier sur le disque.

*Lusty Explorer* s'utilise donc pour deux choses : naviguer sur votre système de fichiers avec ``,lr`` et ``,lf``, et naviguer entre vos fichiers ouverts (buffers) avec ``,lb``. Personnellement j'utilise moins la recherche dans les buffers avec ``,lg``, à vous de tester et de vous faire votre propre opinion.

Je vous conseille en guise de test d'ouvrir plusieurs fichiers avec ``,lr`` ou ``,lf``. Ensuite, entraînez-vous à naviguer entre ces différents fichiers ouverts en même temps à l'aide de ``,lb``. C'est une des combinaisons que j'utilise le plus au quotidien.

Ce plugin est indispensable et ajoute à lui seul énormément de valeur à |vim| : se passer de la souris pour ouvrir des fichiers. Prenez donc le temps nécessaire pour l'apprendre correctement, c'est un investissement qui vaut le coup.

Recherche dans les fichiers sur le disque : *Ack*
=================================================

Lorsque l'on édite un fichier appartenant à un projet plus gros contenant lui même beaucoup de fichiers, il arrive souvent de vouloir rechercher une occurrence d'une chaîne de caractères dans tous les fichiers du projet. Pour ce faire, |vim| dispose d'un plugin permettant d'utiliser *Ack* pour faire cette recherche.

*Ack* (http://betterthangrep.com/) est un programme écrit en *perl* qui remplace avantageusement le bon vieux *grep* pour effectuer des recherches dans des fichiers. Il a en revanche un désavantage par rapport à *grep* : il est rarement installé par défaut. Nous allons donc commencer par installer *Ack* avant de pouvoir aller plus loin. Cela va bien sûr dépendre de la plateforme sur laquelle vous utilisez |vim|, vous pourrez trouver différentes instructions en fonction de votre plateforme sur la page du plugin : http://github.com/mileszs/ack.vim#installation.

Pour Debian/Ubuntu : ``sudo apt-get install ack-grep``. Pour Mac Os X vous allez avoir besoin de Homebrew (http://mxcl.github.com/homebrew/) en utilisant ``brew install ack``. Pour les utilisateurs de MacPorts ça sera avec la commande ``sudo port install p5-app-ack``. Pour Windows installez Strawberry Perl (http://strawberryperl.com/) et dans le shell de commandes exécutez ``C:\>cpan App::Ack``. Vous devriez ensuite pouvoir utiliser la commande **ack** dans votre terminal de commandes en lieu et place de **grep**.

Rendez-vous sur la page du plugin ack (http://www.vim.org/scripts/script.php?script_id=2572) et téléchargez la dernière version (à l'heure où j'écris ces lignes c'est la version 0.3.1). Décompressez l'archive dans votre répertoire ``~/.vim/bundle/``, de manière à obtenir une structure de ce type :

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

* **o** : ouvrir (idem que <Entrée>)
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

