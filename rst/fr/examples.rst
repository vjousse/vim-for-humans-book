**********************
Pense-bête et exemples
**********************

Nous venons de faire un tour d'horizon de tout ce qui est nécessaire pour bien commencer dans la vie avec |vim|. Tout cela devrait être suffisant pour pouvoir l'utiliser au quotidien. C'est le secret de la réussite avec |vim| : réussir à l'encrer dans nos habitudes journalières. Une fois que cela est fait, le reste devrait couler de source.

Cette dernière partie est là pour vous donner un endroit de référence où vous pourrez revenir comme bon vous semble lorsque vous serez un peu perdu sur comment faire telle ou telle chose avec |vim|. Ce chapitre est composé de deux parties. La première est un ensemble de questions réponses qui couvre les principaux problèmes que les débutants rencontrent lorsqu'ils commencent. Le but est de répondre aux questions du type : « rha mais comment on fait ça, c'était pourtant si simple avec mon ancien éditeur ». La seconde partie est une liste (non exhaustive) des commandes |vim| les plus utiles dont vous pourrez vous servir comme pense-bête. Allez hop, au boulot.

Questions / réponses
====================

Comment quitter |vim| ?
-----------------------

La première chose à faire est de se mettre en mode normal. Grosso modo, excitez-vous sur |ttesc| ou |ttsemicolon| en fonction de votre configuration et vous devriez vous retrouver en mode normal. Ensuite tapez :vimcmd:`:q` pour quitter. Il y a de grandes chances que |vim| ne vous laisse pas faire. Si vous avez des modifications non enregistrées par exemple, il ne voudra pas quitter. Vous pouvez annuler les modification en le forçant à quitter grâce à l'utilisation de :vimcmd:`!` comme ceci : :vimcmd:`:q!`. Vous pouvez aussi enregistrer vos modifications puis quitter comme ceci : :vimcmd:`:wq`.

Comment sauvegarder sous ?
--------------------------

En mode normal, si vous tapez :vimcmd:`:w`, |vim| par défaut sauvegarde vos modifications dans le fichier courant. Si vous souhaitez utiliser un autre nom de fichier pour « sauvegarder sous », vous avez juste à lui spécifier le nom du fichier après :vimcmd:`w` comme ceci : :vimcmd:`:w monfichier.txt`. |vim| sauvegardera alors votre fichier sous le nom *monfichier.txt*. En revanche |vim| n'ouvrira pas *monfichier.txt*, il restera sur votre précédent fichier.

Si vous souhaitez que |vim| sauvegarde sous *monfichier.txt* et ouvre ensuite ce fichier dans le tampon courant, vous devrez utiliser :vimcmd:`:sav monfichier.txt`.

Comment copier/couper coller ?
------------------------------

Celle là est facile, j'y ai déjà consacré un chapitre, cf. :ref:`se-deplacer`. 

En résumé :

* Passez en mode visuel avec |ttv|,
* Sélectionnez ce que vous voulez copier en vous déplaçant,
* Copiez avec |tty| ou couper avec |ttx| ou |ttd|,
* Collez après l'emplacement du curseur avec |ttp| ou avant l'emplacement du curseur avec |ttP|.

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
