****************************************
The text editor you've always dreamed of
****************************************

I confess, I have some weird dreams. But hey, maybe my dreams are not as weird as they seem: dreaming of a tool that can improve all the professionals areas of my life as a coder, writer, teacher, …  doesn't seem so weird after all.

The success of |vim| is due to its ability to **ease the text manipulations**. Certainly, it will provide you with functionalities dedicated to specific tasks (often via plugins) as syntax highlighting, spell checking, … but in the end, it's always to write/fix/handle/move text that you spend most of your time.

This is where the difference lies between |vim| and the IDE like Eclipse/Netbeans/PhpStorm and others. Such IDE will put the focus on the particularities of your programming language while providing basic text manipulation functionalities. |vim| takes the opposite approach: you will by default be **very effective** to manipulate/write text no matter what kind of text. But then, when you will feel the need, you will be able to enrich |vim| with plugins specific to your needs and programming languages.

This chapter will cover how to use |vim| the right way (you will begin to forget your mouse) and what is the logic behind all these obscure commands. By the end of this chapter, you should be able to **not use your mouse anymore** to edit/handle text. In any case, you should force yourself when learning |vim|, it's not that hard to only use the keyboard, and it will make a huge diffrence in your day to day life.

.. _moving:

Learning how to move: the copy/paste use case
=============================================

We have already seen in the ":ref:`insertmode`" section how to switch between the insert mode (to write text) and the normal mode (for the moment, you should not totally get what is the purpose of this mode). When you press |tti| your cursor will switch to the insert mode (when you are already in the normal mode) and when you press |ttesc| it will switch back to the normal mode. Well, that's cool. And now, what else?

Preamble
--------

Now is the time to learn our first text manipulation: the famous copy/paste. I can already hear some of you saying that it is useless: you already know how to do that. You switch to the insert mode, you use your mouse (or you move using the directional keys while holding |ttshift|) to select some text. Then you go to the ``edit`` menu and you select ``copy``. Then, ``edit`` menu and ``paste``. Well, why not.

But if you have understood the ":ref:`modes`" section about the ideal position of your hands on the keyboard, you should know that you did things your are not supposed to do:

- You have used your your mouse
- You have moved your right hand a lot from its rest position, to press the directional keys that are far away from your fingers

Certainly, it doesn't really matter, but it's totally ineffective (using your mouse or moving your right hand toward the directional keys is very slow) and harmful for your little hands. This is your last chance: if you are not ready to force yourself to not do it, **|vim| is not for you**. |vim| does a perfect job at keeping your hands on the keyboard and at forgetting your mouse. If you don't do it, you will not be using |vim| to its fullest. And, one day or another, **you will quit for another editor** that was made to be used with a mouse. So, should we continue?

Forget the mouse
----------------

If you are reading thoses lines it means that you answered "yes" to the question above, so let's go! Our first step will be to get rid of the mouse. Then we will do the same with directional keys, but first things first.

To copy/past using |vim|, you will have to switch to the "normal" mode (the default one when you open |vim|). To know what the current mode is, just have a look at the bottom left of your |vim|. You can see |vim| in "insert" mode in `the figure below`.

.. _the figure below: `mode insert`_

.. _mode insert:

.. image:: ../book-tex/graphics/vim-insert.png


When there is nothing displayed at the bottom left, it's because you are currently in "normal" mode. In order to quit a mode to return to the normal one, you just have to press |ttesc|. You may already have noticed that pressing |ttesc| is a pain for your fingers. No worries, it's just a temporary thing, I will explain why in the ":ref:`secesc`" section.

Let's say that you are currently in the "normal" mode and that you already have some text in you |vim|. For example, it could be this beautiful quote from Mark Twain: "They did not know it was impossible, so they did it.". Your |vim| should like the one in the figure below. Notice that there is nothing displayed at the bottom left.

.. _twain:

.. image:: ../book-tex/graphics/vim-twain.png

The most intuitive way (but not the most efficient, we will see why a little bit later) to copy/paste the "impossible" word is to move the cursor at the first letter of the word using the directional keys, to press |ttv| (to switch to the "visual" mode), to move to the last letter of the word (you should have the word "impossible" highlighted) and then to press |tty| (|tty| stands for *yank*). You've just copied your first word using |vim|. Hooray!

Then, move to the end of the sentence (in "normal" mode) and press |ttp| (|ttp| standing for *paste*). The word should now be pasted at the end, and you should have something like the figure below.

.. _vim-paste:

.. image:: ../book-tex/graphics/vim-paste.png

We can see that |vim| is using the mode switching trick (including the "normal" mode for moving) in order to not have to use the mouse.
When you will be used to switch quickly from one mode to another (and in order to do so, going without |ttesc| will be mandatory), using the mouse will appear like a pure waste of time. But obviously, you will first need to train yourself.

.. _secse-passer-touches-dir:

Forgetting the directional keys
===============================

Here we are. Even if forgetting the mouse is a first good step, the real goal when using |vim| is to forget the directional keys too. You will be faster and better when using |vim| on the sole condition that you don't use the directional keys anymore. It will indeed force you to keep your hands on the home row and you will have to switch to the normal mode to move around. This is a prerequisite to use |vim| at its fullest.

In this section, I will explain how to move without using the directional keys. Then, when you will know how to do it, I will give you the code that you need to put in your |vimrc| to totally disable the directional keys. It was the only way I found to force me to not use the directional keys anymore.

Moving without using the directional keys
-----------------------------------------

When in normal mode, 4 keys will allow you to move your cursor:

* |tth| to move to the **left**
* |ttj| to move to the **bottom**
* |ttk| to move to the **top**
* |ttl| to move to the **right**


.. _hjkl:

.. image:: ../book-tex/graphics/hjkl.png

As you can notice, thoses keys are located on the home row so that you don't have to move your hands. Your index has two moves (left and bottom) while your auricular doesn't have any. You will see that it's not a problem, it's even a feature: your index is stronger than your auricular. By checking the keyboard that was used to develop *Vi* in the ":ref:`secesc`" section, you will understand why.

On a side note, once you will be used to |vim|, you will note use the left and right moves a lot. You will primarily move the cursor word by word, paragraph by paragraph or by using the search function. Here are some "fast moves" that I otfen use:

========== =================================================
Key        Move
========== =================================================
|te|       **to the end of the current word**
|tb|       **to the beginning of the current word**
|tw|       **to the beginning of the next word**
|that|     **to the first non white character of the line**
|tdollar|  **to the end of the line**
|tzero|    **to the start of the line**
========== =================================================


Vous avez ici le minimum pour vous déplacer en mode normal. Il existe aussi des commandes vous permettant de vous déplacer puis de rentrer en mode insertion directement, elles sont très pratiques car elles vont vous permettre d'économiser quelques touches. En voici quelques unes que j'utilise à peu près tout le temps :

======== ================================================================
Touche   Action
======== ================================================================
|ti|     se place en mode insertion **avant l'emplacement du curseur**
|ta|     se place en mode insertion **après l'emplacement du curseur**
|tI|     se place en mode insertion **au début de la ligne**
|tA|     se place en mode insertion **à la fin de la ligne**
|to|     insère une nouvelle ligne **en dessous de la ligne courante**
|tO|     insère une nouvelle ligne **au dessus de la ligne courante**
|tr|     **remplace les caractères** sous le curseur
======== ================================================================

Arrêtons-nous un peu là dessus. Au risque d'insister lourdement, mais la clé de l'utilisation de |vim| vient de ce que nous venons de voir dans ce chapitre, ni plus, ni moins. Il y a une chose que vous avez à vous forcer à faire, c'est **d'utiliser les touches hjkl** pour les déplacements. Si vous y arrivez, vous apprendrez tout le reste au fur et à mesure.

Vous trouverez des sites entiers vous détaillant les différentes commandes possibles, les différentes combinaisons, j'en passe et des meilleures. Vous les apprendrez puis les oublierez (ou pas, en fonction de si elles vous sont vraiment utiles). Si vous avez un seul effort à faire c'est celui de se passer des touches directionnelles et donc de vous forcer à utiliser le mode normal. Le reste tombera sous le sens.

Voici l'ultime configuration qu'il vous faudra mettre dans votre |vimrc| pour atteindre le Saint Graal : désactiver les touches directionnelles.::

    " Désactiver les touches directionnelles
    map <up> <nop>
    map <down> <nop>
    map <left> <nop>
    map <right> <nop>
    imap <up> <nop>
    imap <down> <nop>
    imap <left> <nop>
    imap <right> <nop>

Nous y voilà. Croyez-moi, vous allez souffrir un peu au début. Pour moi, ça n'a pas duré plus de deux jours. Ensuite vous aurez oublié. Si vous n'êtes pas prêt à galérer un peu pendant deux jours pour améliorer votre efficacité à vie, que faites-vous ici !

Je ne vous donnerai pas d'autres détails sur toutes les touches possibles pour vous déplacer, d'autres ressources le font déjà bien mieux que moi. Je vais en revanche vous apprendre dans :ref:`combine-move` comment les utiliser à bon escient.

On peut notamment citer le livre gratuit "A byte of |vim|" traduit en français et disponible à l'adresse suivante : http://swaroopch.com/notes/Vim_fr/.

Ou encore l'infographie de la figure ci-dessous (téléchargeable sur http://www.nathael.org/) qui donne un aperçu des différents mouvements pour chacune des touches d'un clavier français.

.. _cheat-sheet:

.. image:: ../book-tex/graphics/vi-vim-cheat-sheet.png


N'oubliez pas que le but ici est de gagner en rapidité en ne bougeant quasi plus ses mains de la rangée de repos, et en utilisant le plus possible le « mode normal ». Au boulot !

.. _secesc:

Se passer de la touche Échap
============================

Utiliser |ttesc| pour sortir du mode « insertion » semble être une hérésie tellement elle est difficilement accessible. Il faut déplacer entièrement la main gauche pour y accéder ou alors se torturer le petit doigt.

Pour comprendre pourquoi |ttesc| est utilisée par défaut, il faut faire un bon de quelques années en arrière, pour se retrouver en face du clavier sur lequel *Vi* a été développé. Vous pouvez voir sur la photo ci-dessous que |ttesc| était très facilement accessible. Vous pouvez aussi noter l'emplacement des touches directionnelles. Malheureusement depuis, cela a bien changé.

.. _vi-keyboard:

.. image:: ../book-tex/graphics/lsi-adm3a-full-keyboard.jpg

L'étape ultime (après avoir réussi à se passer des touches directionnelles) est donc de rapprocher |ttesc| de vos petits doigts. Il y a plusieurs solutions pour cela, mais celle que je vous recommande si vous avez un clavier avec une disposition française est la suivante (dans votre |vimrc|) :::

    " Les ; sont rarement utilisés l'un à la suite de l'autre
    :imap ;; <Esc>
    :map ;; <Esc>

Lorsque vous êtes en mode insertion, il vous suffit d'appuyer deux fois sur |ttsemicolon| pour retourner au mode normal. |ttsemicolon| ne vous demande pas de bouger votre main de la rangée de repos et on l'utilise rarement deux fois de suite (et si c'est le cas, il suffit d'attendre un peu avant de taper le deuxième |tsemicolon|), c'est donc le parfait candidat.

Voici d'autres solutions possibles (cf http://vim.wikia.com/wiki/Avoid_the_escape_key):::

    :imap jj <Esc>

    :imap jk <Esc>

    :imap ii <Esc>

    :imap ` <Esc>

    " Shift-Espace (peut ne pas marcher sur votre système).
    :imap <S-Space> <Esc>

    " Sous Linux avec gvim Vim en console, vous pouvez utiliser Alt-Space.
    :imap <M-Space> <Esc>

.. _combine-move:

Combiner des touches/déplacements
=================================

Maintenant que nous savons nous déplacer en mode normal, il est temps de voir comment réaliser d'autres opérations. Nous avons déjà vu le copier/coller au chapitre :ref:`se-deplacer`, nous allons maintenant voir comment supprimer/éditer plus facilement.

Dans :ref:`secse-passer-touches-dir` nous avons vu qu'il suffisait d'utiliser |ttw| pour se déplacer au début du mot suivant. Nous allons essayer de combiner cela avec quelques nouvelles touches du mode normal :

* |ttd| est utilisée pour « supprimer »
* |ttc| est utilisée pour « supprimer et passer en mode insertion »

À noter que ce qui est supprimé est placé dans le presse-papier en même temps (le « supprimer » se comporte par défaut comme un « couper »).

La particularité de ces touches, c'est qu'elles attendent ensuite un « ordre de déplacement » pour savoir quoi supprimer. Il va donc falloir les combiner avec les déplacements que nous avons déjà vus dans :ref:`secse-passer-touches-dir`.

Cela donnera par exemple :


======================= ============================================================================
Action                  Résultat
======================= ============================================================================
|ttd| puis |ttw|        supprime les caractères jusqu'au prochain mot
|ttc| puis |ttw|        supprime les caractères jusqu'au prochain mot et passera en mode insertion
|ttd| puis |ttdollar|   supprime tout jusqu'à la fin de la ligne
|ttd| puis |tthat|      supprime tout jusqu'au début de la ligne
======================= ============================================================================

Vous pouvez aussi utiliser cela pour copier :

======================= =============================================================
Action                   Résultat
======================= =============================================================
|tty| puis |ttw|        copie les caractères jusqu'au prochain mot
|tty| puis |ttdollar|   copie tout jusqu'à la fin de la ligne
|tty| puis |tthat|      copie tout jusqu'au premier caractère non blanc de la ligne
======================= =============================================================

Il ne vous restera qu'a appuyer sur |ttp| pour coller ce que vous voulez où vous voulez. Par défaut |ttp| colle le texte après la position courante du curseur. Si vous voulez coller avant la position du curseur, utilisez |ttP|.

Il arrive de temps en temps de vouloir aussi supprimer du texte (non sans blague !), voici quelques commandes utiles pour cela :

========= ============
Action    Résultat
========= ============
|tdtd|    efface la ligne courante et la place dans le presse-papier
|tx|      efface le caractère sous le curseur
|tX|      efface le caractère avant le curseur
========= ============

La plupart des mouvements peuvent être préfixés par un nombre multiplicateur. Voici quelques exemples :

================= ============
Action            Résultat
================= ============
``2``\ |td|\ |td| efface deux lignes
``3``\ |tx|       efface 3 caractères vers l'avant du curseur
``3``\ |tX|       efface 3 caractères vers l'arrière du curseur
``2``\ |ty|\ |ty| copie 2 lignes dans le presse-papier
``5``\ |tj|       se déplace de 5 lignes vers le bas
================= ============


Rechercher / Se déplacer rapidement
===================================

Maintenant que nous connaissons les commandes de base pour éditer du texte avec |vim|, voyons voir comment nous déplacer plus rapidement dans notre document. Nous avons déjà évoqué les touches |tw|, |tb|, |that| et |tdollar| qui nous permettent respectivement de se déplacer à la fin d'un mot, au début d'un mot, au début d'une ligne et la fin d'une ligne. Tout d'abord, voyons voir comment « scroller » sans la souris. À noter que toutes ces commandes se font en mode « normal ».

Sauts de page
-------------

Pour faire défiler les pages, il faut utiliser :

* |tctrl| + |tf| pour passer à la page suivante (|tf| pour forward)
* |tctrl| + |tb| pour passer à la page précédente (|tb| pour backward)

Ces raccourcis vont vous permettre d'avancer rapidement dans votre document. 

Vous pouvez aussi :

* Vous rendre au début du fichier en tapant |tgtg|
* Vous rendre à la fin du fichier en tapant |tG|
* Vous rendre à la ligne 23 en tapant |tcolon|\ ``23``

Les marqueurs
-------------

Lorsque je me déplace dans un fichier, j'aime bien pouvoir revenir à certains endroits. Par exemple lorsque je me rends au début du fichier alors que j'étais en train de travailler au milieu de celui-ci, j'aime bien pouvoir revenir directement où je travaillais. Heureusement, |vim| a tout prévu pour cela grâce à l'utilisation de **marqueurs**. Les marqueurs sont tout simplement des « marque-pages » qui permettent à votre curseur de se retrouver à la position où vous aviez mis votre marqueur.

Un marqueur se pose en tapant |tm|\ |ta|. Pour déplacer votre curseur à la position du marqueur tapez |tapos|\ |ta|. Vous pouvez placez plusieurs marqueurs en changeant |ta| par n'importe quelle lettre de l'alphabet (on appelle cela des registres en langage |vim|). Pour placer un autre marqueur vous pouvez par exemple utiliser la lettre |td|. Grâce à |tm|\ |td| vous placerez le marqueur et à |tapos|\ |td| vous vous y rendrez.

La recherche
------------

En mode normal, vous pouvez lancez une recherche en utilisant |ttslash| suivi du texte que vous souhaitez rechercher puis de |ttenter|. Grâce à notre configuration de |vim| vous devriez voir vos occurrences de recherche surlignées en même temps que vous tapez. Par défaut la recherche n'est pas sensible à la casse (pas de différence entre minuscules/majuscules). En revanche, dès que vous taperez une majuscule, la recherche deviendra sensible à la casse. Vous pouvez vous déplacer à la prochaine occurrence de la recherche grâce à |ttn|. Pour vous déplacer à la précédente utilisez |ttN|.

Pour rappel, voici les lignes de votre fichier de configuration qui permettent de faire cela :::

    " -- Recherche
    set ignorecase            " Ignore la casse lors d'une recherche
    set smartcase             " Si une recherche contient une majuscule,
                                " re-active la sensibilite a la casse
    set incsearch             " Surligne les resultats de recherche pendant la
                                " saisie
    set hlsearch              " Surligne les resultats de recherche

Attention par défaut, la recherche utilise les expressions régulières POSIX. Si vous souhaitez rechercher des caractères habituellement utilisés dans les expressions régulières (comme [ ] ^{ } $ /) n'oubliez pas de les préfixer par \\.

Vous pouvez aussi rechercher directement le mot qui est placé sous votre curseur grâce à |ttstar|. Utiliser |ttstar| fera une recherche vers l'avant. Pour faire une recherche vers l'arrière, utilisez |ttsharp|.

Le mode visuel
==============

Je vous en ai déjà parlé lors de l'explication sur le Copier / Coller, mais comme je sais que certains d'entre vous sont tête en l'air, je vous fais un petit rappel ici.

Lorsque vous êtes en mode « normal » appuyez sur |ttv| pour passer en mode "visuel". Vous pourrez alors sélectionner des caractères ou des lignes entières grâce aux différentes façon de vous déplacer que vous venez d'apprendre. Vous pourrez ensuite copier le texte sélectionné avec |tty| puis le coller avec |ttp|. Pour le couper il vous faudra utiliser |ttd|.

En mode normal vous pourrez utiliser |ttV| pour sélectionner lignes par lignes. Et bien sûr, utiliser |ttesc| ou :vimcmd:`;;` pour revenir au mode normal.

À vous de jouer
===============

Vous devriez maintenant être capable de n'utiliser que le clavier pour les opérations de manipulation de texte et d'édition. Je n'ai fait que survoler la puissance de |vim| ici, mais ça devrait être suffisant pour survivre. Je vous ai donné ici le strict nécessaire, mais ce strict nécessaire vous permet déjà de profiter de |vim| et du plaisir de ne plus utiliser la souris.

À vous maintenant de lire les nombreuses ressources disponibles sur internet vous décrivant tous les mouvements possibles et imaginables. Je ne manquerai d'ailleurs pas de compléter ce guide avec des articles sur le site internet qui lui est dédié http://vimebook.com.

Voici une liste de ressources qui pourraient vous être utiles, malheureusement les ressources en français sont assez rares :

* A byte of |vim| en français http://www.swaroopch.com/notes/vim_fr/
* Un petit pense bête sympathique de différents raccourcis clavier http://www.tuteurs.ens.fr/unix/editeurs/vim.html
* Un wiki non officiel francophone (un peu fouillis soit dit en passant) : www.vim-fr.org/
* Les vidéos Peepcode en anglais mais vraiment superbement réalisées : https://peepcode.com/products/smash-into-vim-i et https://peepcode.com/products/smash-into-vim-ii
* Le blog de Derek Wyatt's en anglais http://www.derekwyatt.org/vim/vim-tutorial-videos/

Histoire de réveilleur l'enfant qui est en vous, je vous conseille vivement d'aller vous amuser avec http://vim-adventures.com/. C'est un jeu de rôle en ligne qui a pour but de vous apprendre à manipuler |vim| ! Voici un petit aperçu :

.. _vim-adventures:

.. image:: ../book-tex/graphics/vim-adventures.png

Nous allons maintenant passer à la vitesse supérieure : l'utilisation de plugins, ou comment rendre |vim| incontournable.
