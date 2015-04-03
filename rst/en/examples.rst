*********************
Cheatsheet & examples
*********************

So here we go, we now have everything needed to make a good start with |vim|. It should be enough to use it on a daily basis. It's the most important thing to do if you want to successfully use |vim|: developing the habit of using it everyday. Once you'll have this habit, everything should seem natural to you.

The aim of this chapter is to provide you with a reference for the most common things you'll have to do with |vim| so that, when you are lost, you know where to search for help. This chapters contains two parts. The first one is a set of Q/A covering the most common problems that newbies are facing. The goal is to answer this kind of question: "f**k, how can I do this, it was so simple with my old editor". The second is a non-exhaustive list of the most useful |vim| commands.

Questions / Answers
===================

How to quit |vim|?
------------------

First you need to be sure to be in normal mode. If you don't know how to be sure that you are in normal mode, just press |ttesc| or |ttsemicolon| (depending on your configuration) multiple times and you should be in normal mode. Then, type :vimcmd:`:q` to exit |vim|. The problem is that most of the times, |vim| will no let you quit like that. For example, if you have unsaved changes, it will not let you quit. You can cancel your modifications by using :vimcmd:`!` like that: :vimcmd:`:q!`. You can also save your modifications and save like that: :vimcmd:`:wq`.

How to save as?
---------------

In normal mode, if you type :vimcmd:`:w`, |vim| will by default save your modifications into the current file. If you want to use another filename to "save as", you just need to specify it after :vimcmd:`w` like that: :vimcmd:`:w myfile.txt`. |vim| will save your file under the name *myfile.txt*. On the other hand, |vim| will not open *myfile.txt*, it will stay on the previous file.

If you want |vim| to save under the filename *myfile.txt* and then open the file in the current buffer, you will have to use :vimcmd:`:sav myfile.txt`.

How to copy/cut paste?
----------------------

This one is easy, there is already a full chapter on it, cf. :ref:`moving`.

In short:

* Switch to visual mode with |ttv|,
* Select the text you want to copy by moving the cursor,
* Copy using |tty| or cut using |ttx| or |ttd|,
* Paste after the cursor using |ttp| or before using |ttP|.

Comment créer un nouveau fichier ?
----------------------------------

La façon traditionnelle de faire est de taper, en mode normal, :vimcmd:`:e monfichier.txt` pour ouvrir un tampon (buffer) vide. Ensuite, sauvegardez votre tampon grâce à :vimcmd:`:w`. Il sera sauvegardé sous le nom ``monfichier.txt`` dans le répertoire courant.

Vous pouvez aussi utiliser Lusty Explorer (cf. :ref:`seclusty`) pour ce faire. Lancez le grâce à ``,lr`` ou ``,lf``, tapez le nom du fichier que vous souhaitez créer puis appuyez sur |ttctrl| puis en même temps |tte|. Vous pouvez ensuite le sauvegarder de la même manière que ci-dessus.

Annuler / Refaire
-----------------

Pour annuler il suffit d'utiliser |ttu| en mode normal. Pour annuler le annuler (donc refaire) maintenez |ttctrl| appuyée puis |ttr|.

Pense-bête
==========

Fichiers
--------

=================================================== ==================================== ============
Résultat attendu                                    Action                               Commentaire
=================================================== ==================================== ============
**Sauvegarder**                                     :vimcmd:`:w` & (w pour write)
**Sauvegarder sous**                                :vimcmd:`:w nomdefichier.txt`        Sauvegarde sous nomdefichier.txt mais n'ouvre pas nomdefichier.txt
**Sauvegarder sous / ouvre**                        :vimcmd:`:sav nomdefichier.txt`      Sauvegarde sous et ouvre nomdefichier.txt
**Quitter sans sauvegarder (forcer à quitter)**     :vimcmd:`:q!`
**Sauvegarder et quitter**                          :vimcmd:`:wq`                        wq pour write and quit
**Sauvegarder en tant que root**                    :vimcmd:`:w !sudo tee %`             
=================================================== ==================================== ============

Déplacements
------------

=============================================================== ===========
Résultat attendu                                                Action
=============================================================== ===========
**Se déplacer d'un caractère à gauche**                         ``h``
**Se déplacer d'un caractère en bas**                           ``j``
**Se déplacer d'un caractère en haut**                          ``k``
**Se déplacer d'un caractère à droite**                         ``l``
**Se déplacer à la fin d'un mot**                               ``e``
**Se déplacer au début d'un mot**                               ``b``
**Se déplacer au début du mot suivant**                         ``w``
**Se déplacer à la ligne 42**                                   ``:42``
**Se déplacer au début du fichier**                             ``gg`` ou ``:0``
**Se déplacer à la fin du fichier**                             ``GG`` ou ``:$``
**Se déplacer à la fin de la ligne**                            ``$``
**Se déplacer au premier caractère non vide de la ligne**       ``^``
**Se déplacer au début de la ligne**                            ``0``
**Descendre d'une page**                                        ``Ctrl+f``
**Monter d'une page**                                           ``Ctrl+b``
**Se déplacer à la première ligne de l'écran**                  ``H``
**Se déplacer au milieu de l'écran**                            ``M``
**Se déplacer à la dernière ligne de l'écran**                  ``L``
=============================================================== ===========

Édition de texte
----------------

=============================================================================== =========== ========================
Résultat attendu                                                                Action      Commentaire
=============================================================================== =========== ========================
**Insérer avant le curseur**                                                    ``i`` 
**Insérer avant le premier caractère non vide de la ligne**                     ``I`` 
**Insérer après le curseur**                                                    ``a`` 
**Insérer à la fin de la ligne**                                                ``A`` 
**Insérer une nouvelle ligne en dessous**                                       ``o`` 
**Insérer une nouvelle ligne au dessus**                                        ``O`` 
**Remplace le reste de la ligne**                                               ``C`` 
**Remplace un seul caractère (et reste en mode normal)**                        ``r`` 
**Supprime le caractère après le curseur (comme la touche suppr.)**             ``x`` 
**Supprime le caractère avant le curseur (comme la touche backspace)**          ``X`` 
**Supprime la ligne courante**                                                  ``dd`` 
**Copie la ligne courante**                                                     ``yy`` 
**Colle après le curseur. Si c'est une ligne, colle la ligne en dessous.**      ``p`` 
**Colle avant le curseur. Si c'est une ligne, colle la ligne au dessus.**       ``P`` 
**Intervertit la case des caractères (majuscules / minuscules)**                ``~``       Marche en mode visuel
**Déplace le texte vers la droite (indentation)**                               ``>``       Marche en mode visuel 
**Déplace le texte vers la gauche**                                             ``<``       Marche en mode visuel 
**En mode visuel, supprime la sélection**                                       ``d``       Mode visuel 
**En mode visuel, remplace la sélection**                                       ``c``       Mode visuel 
**En mode visuel, copie la sélection**                                          ``y``       Mode visuel 
**Annuler (Undo)**                                                              ``u`` 
**Refaire (Redo)**                                                              ``Ctrl+r``
=============================================================================== =========== ========================

Chercher et/ou remplacer
------------------------

=================================================================== ======================= =================================
Résultat attendu                                                    Action                  Commentaire
=================================================================== ======================= =================================
**Rechercher**                                                      ``/*toto``              Cherche la chaîne de caractères *toto* à partir de l'emplacement courant du curseur 
**Suivant**                                                         ``n``                   Affiche le prochain résultat de recherche
**Précédent**                                                       ``N``                   Affiche le précédent résultat de recherche
**Remplacer sur la ligne courante**                                 ``:s/toto/titi``        Remplace toto par titi sur la ligne courante (une fois)
**Remplacer tout sur la ligne courante**                            ``:s/toto/titi/g``      Remplace toto par titi sur la ligne courante (pour toutes les occurrences de toto)
**Remplacer dans toutes les lignes**                                ``:%s/toto/titi``       Remplace toto par titi sur toutes les lignes du fichier (une fois par ligne)
**Remplacer tout dans toutes les lignes**                           ``:%s/toto/titi/g``     Remplace toto par titi sur toutes les lignes du ficher (pour toutes les occurrences de toto par ligne)
**Remplacer sur la ligne courante en ignorant la casse**            ``:s/toto/titi/i``      Remplace toto par titi sur la ligne courante (une fois)
**Remplacer tout sur la ligne courante en ignorant la casse**       ``:s/toto/titi/gi``     Remplace toto par titi sur la ligne courante (pour toutes les occurrences de toto)
=================================================================== ======================= =================================
