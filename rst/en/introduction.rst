************
Introduction
************

When you need to write or to code, you have to choose a text editor, and a very good one. They are many text editors available out there, but very few of them are more than 40 years old. It's the case of *Emacs* (http://www.gnu.org/software/emacs/), *Vi* and its improved successor |vim| (http://www.vim.org). They were created in the 70's and are still used a lot nowadays. You may have already noticed that it's not thanks to the beauty of their website or the efficiency of their communication. Here are some **reasons for their success**:

**Forever** 
    You learn them once and you use them forever. In a world where the languages and technologies are constantly changing, it's a real chance to be able to invest for the long term.

**Everywhere**
    They are available for each and every possible platform : Mac Os X, Windows, GNU/Linux, BSD, … and it's always been the case.

**Efficient** 
    Thanks to their features (like the extensive use of the keyboard), you can edit and write text as fast as your thoughts.

**For everything** 
    They allow you to edit everything and anything. When you'll use another programming language, or another markup language, you'll not have to change your editor. Of course, this book was written using |vim| (and the `ReST Markup <http://sphinx-doc.org/rest.html>`_).

Et pourtant, ces éditeurs de texte restent difficiles à apprendre. Non pas qu'ils soient plus compliqués qu'autre chose, non pas que vous ne soyez pas à la hauteur, mais plutôt à cause d'un manque de pédagogie des différentes documentations.

Ce livre a pour but de pallier ce manque en vous guidant tout au long de votre découverte de |vim|. Je laisse *Emacs* à ceux qui savent (pour un bref comparatif c'est ici : http://fr.wikipedia.org/wiki/Guerre_d'\%C3\%A9diteurs. Les goûts et les couleurs …). Il ne prétend pas être un guide exhaustif, vous pouvez essayer *A Byte of vim* pour celà : http://www.swaroopch.org/notes/Vim. En revanche, il prétend diminuer la marche à franchir pour s'habituer à |vim|. À mon sens, le plus compliqué avec |vim|, c'est de ne pas se décourager de suite et de trouver une méthode qui vous permette de l'apprendre au fur et à mesure. Nous avons tous un travail à effectuer au quotidien, et perdre toute sa productivité à cause d'un changement d'éditeur de texte n'est pas envisageable.

Vous trouverez beaucoup de personnes pour vous dire « mais tu n'as qu'à t'y mettre pour de bon », « tu verras après ça va aller mieux », certes, mais vous devez toujours être productif au jour le jour, ça ne change rien au problème. L'approche de ce livre est la suivante :

- Disposer d'un |vim| un temps soit peu moderne : coloration syntaxique et jolies couleurs.
- Pouvoir utiliser |vim| comme n'importe quel autre éditeur de texte : éditer facilement du code et naviguer entre les fichiers en utilisant la souris.
- Apprendre des raccourcis clavier et se passer de la souris au fur et à mesure.
- Installer un *best-of* des plugins pour commencer à tirer partie de la puissance de |vim|.

À partir du point numéro 2, vous pourrez déjà utiliser |vim| au quotidien sans perdre énormément de productivité. Et c'est là que la différence se fait : si vous pouvez intégrer |vim| dans votre quotidien c'est gagné. Vous aurez ensuite toute votre vie pour connaître tous les raccourcis clavier.

Vous aussi vous en avez marre d'attendre la release de TextMate 2 (à noter que depuis l'écriture de ce livre, le code de TextMate 2 a été publié sous licence GPL : https://github.com/textmate/textmate) ? D'essayer le n-ième éditeur à la mode et de devoir tout réapprendre et ce jusqu'à la prochaine mode ? De devoir changer d'éditeur quand vous passez de votre Mac, à votre Windows, à votre Linux ? Alors vous aussi, rejoignez la communauté des gens heureux de leur éditeur de texte. **Le changement, c'est maintenant** !

Pour qui ?
==========

Toute personne étant amenée à produire du texte (code, livre, rapports, présentations, ...) de manière régulière. Les développeurs sont bien sûr une cible privilégiée, mais pas uniquement.

Par exemple vous êtes :

**Étudiant**
    Si vous voulez faire bien sur un CV, c'est un must. C'est en effet un gage de sérieux de voir qu'un étudiant a pris sur son temps personnel pour apprendre |vim|. De plus, vous aurez un outil unique pour écrire tout ce que vous avez à écrire (et que vous pourrez réutiliser tout au long de votre carrière) : vos rapports en LaTeX, vos présentations, votre code (si vous avez besoin d'OpenOffice ou de Word pour écrire vos rapports, il est temps de changer d'outil et d'utiliser LaTeX, Markdown ou reStructuredText).

    Petit conseil d'ami, pour vos présentations, n'hésitez pas à utiliser un outil comme *impress.js* : http://bartaz.github.com/impress.js. Basé sur du HTML/JS/CSS, je vous le recommande grandement pour des présentations originales et basées sur des technologies non propriétaires. Il existe aussi *reveal.js* (http://lab.hakim.se/reveal-js/) et son éditeur en ligne *slid.es* (http://slid.es/).

**Enseignant** 
    Il est temps de montrer l'exemple et d'apprendre à vos étudiants à bien utiliser un des outils qui leur servira à vie, bien plus qu'un quelconque langage de programmation.

**Codeur** 
    Investir dans votre outil de tous les jours est indispensable. Quitte à apprendre des raccourcis claviers, autant le faire de manière utile. Si cet investissement est encore rentable dans 10 ans, c'est ce que l'on pourrait appeler l'investissement parfait, c'est |vim|.

**Administrateur système Unix**
    Si vous utilisez *Emacs* vous êtes pardonnable. Si vous utilisez nano/pico je ne peux plus rien pour vous, sinon il est grand temps de s'y mettre les gars. Administrer un système Unix à distance est un des cas d'utilisation parfait pour |vim| (un éditeur de texte surpuissant ne nécessitant pas d'interface graphique).

**Écrivain** 
    Si vous écrivez en markdown/reStructuredText/WikiMarkup ou en LaTeX, |vim| vous fera gagner beaucoup de temps. Vous ne pourrez plus repasser à un autre éditeur, ou vous voudrez le "Vimifier" à tout prix.

Faites moi confiance, je suis passé et repassé par ces 5 rôles, mon meilleur investissement a toujours été |vim|, et de loin.

Ce que vous apprendrez (entre autres choses)
============================================

- Comment utiliser |vim| comme un éditeur « normal » d'abord (vous savez, ceux qui permettent d'ouvrir des fichiers, de cliquer avec la souris, qui ont une coloration syntaxique ...). En somme, la démystification de |vim| qui vous permettra d'aller plus loin.
- Comment passer de l'édition de texte classique à la puissance de |vim|, petit à petit (c'est là que l'addiction commence).
- Comment vous passer de la souris et pourquoi c'est la meilleure chose qu'il puisse vous arriver quand vous programmez/tapez du texte.
- Comment vous pouvez facilement déduire les raccourcis claviers avec quelques règles simples.

Si je devais le résumer en une phrase : puisque vous vous considérez comme **un artiste, passez du temps à apprendre** comment utiliser l'outil qui vous permet de vous exprimer, une bonne fois pour toute.

Ce que vous n'apprendrez pas (entre autres choses)
==================================================

- Vous n'apprendrez pas comment installer/configurer |vim| pour Windows. Pas que ce ne soit pas faisable, mais je n'ai que très peu de connaissances de Windows. Ça viendra peut-être, mais pas tout de suite. On couvrira ici Linux/Unix (et par extension Mac OS X).
- Vous n'apprendrez pas comment utiliser *Vi* (notez l'absence du "m"). Je vais vous apprendre à être productif pour coder/produire du texte avec |vim|, pas à faire le beau devant les copains avec *Vi* (|vim| est suffisant pour cela de toute façon). Pour ceux qui ne suivent pas, *Vi* est "l'ancêtre de |vim| (qui veut dire *Vi* - *IMproved*, *Vi* amélioré)" et est installé par défaut sur tous les Unix (même sur votre Mac OS X).
- Vous n'apprendrez pas à connaitre les entrailles de |vim| par cœur : ce n'est pas une référence, mais un guide utile et pragmatique.
- Vous n'apprendrez pas comment modifier votre |vim| parce que vous préférez le rouge au bleu : je vous ferai utiliser le thème *Solarized* (http://ethanschoonover.com/solarized), il est parfait pour travailler.

Le plus dur, c'est de commencer
===============================

Alors, prêt pour l'aventure ? Prêt à sacrifier une heure pour débuter avec |vim|, une semaine pour devenir familier avec la bête, et le reste de votre vie pour vous féliciter de votre choix ? Alors c'est parti ! Enfin presque, il faut qu'on parle avant.

|vim| fait partie de ces outils avec lesquels vous allez galérer au début. Le but de ce guide est de vous mettre le pied à l'étrier et de diminuer la hauteur de la marche à franchir. Mais soyez conscients que vous mettre à |vim| va vous demander de la volonté et quelques efforts. Comme on dit souvent, on n'a rien sans rien. Voici la méthode que je vous recommande pour apprivoiser la bête :

- Essayez de faire entrer |vim| dans vos habitudes. Suivez le premier chapitre de ce guide jusqu'à la partie concernant l'explorateur de fichiers utilisable à la souris *The NERD Tree*. Ensuite, vous pourrez utiliser |vim| comme un Notepad++ ou un TextMate ou un Sublime Text. Vous n'utiliserez que 1% des capacités de |vim| mais peu importe. Ce qui est important, c'est de le faire entrer dans votre quotidien.
- Gardez une feuille avec les principaux raccourcis imprimée à côté de vous. Le but ce n'est pas de les apprendre par cœur, mais c'est de les avoir à portée de main quand vous vous demanderez « mais il y a certainement une façon plus efficace de faire cela ».
- Gardez la foi. Au début vous resterez un sceptique quant à l'utilité de tout réapprendre avec |vim|. Et puis un jour vous aurez un déclic et vous vous demanderez pourquoi tous vos logiciels ne peuvent pas se contrôler avec les commandes de |vim|.
- Gardez à l'esprit que c'est un investissement pour vos 20 prochaines années, et c'est bien connu, un investissement ce n'est pas complètement rentable de suite.

Trêve de bavardage, passons aux choses sérieuses. Go go go !
