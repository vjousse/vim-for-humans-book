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

Yet, these text editors are difficult to learn. Not that they are harder than anything else, not that you can't handle it, but rather because there is no smart way out there to learn them for now. So, here we are.

The goal of this book is to address this gap by guiding you through your discovery of |vim|. I'll put *Emacs* aside from now and I'll focus on |vim|. If you want to know more about this **Editor war**, be sure to check the `Wikipedia page <http://en.wikipedia.org/wiki/Editor_war>`_. This book doesn't claim to be a reference book about |vim|. They are already a lot of good references on the subject like `A byte of Vim <http://swaroopch.com/notes/vim/>`_. However, it claims to reduce the entry barrier to get used to |vim|. To me, the hardest thing to do when learning |vim| is not to discourage away and find a method allowing use to learn it step by step. We all have to get things done with our text editor on a daily basis, that's why loosing all your productivity when switching to |vim| is not possible

I'm sure you'll find a lot of person who will say to you: "Just do it cold turkey", "you'll see, it's hard at the beginning, but time will help". Sure. But you still have to be productive on a daily basis, the problem remains. The approach of this book is the following:

- Have a modern |vim|: syntax highlighting and nice colors.
- Use |vim| as any other text editor: easily edit code and switch between files using the mouse.
- Learn keyboard shortcuts and go without the mouse step by step.
- Install the *best* plugins to start using |vim| to its full potential.

Starting from bullet number 2, you'll already be able to use |vim| on a daily basis without loosing a lot of your productivity. It's were the magic will happen: if you can integrate |vim| in your daily habits, you won. You'll then have the rest of your life to learn all the shortcuts and the tip and tricks of |vim|.

You're tired of trying a new editor each year? You're tired of having to relearn everything from scratch every time? You're tired to have to change your editor when you're using your Mac, Windows or Linux? So, just stop it, and join the community of people happy with their text editor!

For who?
========

Every guy having to produce text (code, book, reports, slideshows, …) regularly. Developers are of course concerned, but it's not only about them.

For example, your are a:

**Student**
    If you want to impress your future boss with your resume, it's a must. It's a proof of seriousness to see that a student took the time to learn |vim| on its own. Moreover, you'll have a unique tool to write all what you'll have to write (and that you'll be able to use for the rest of your career): your LaTeX reports, your slideshows, your code (if you need Word or LibreOffice to write you reports, it's time to use `LaTeX <http://en.wikipedia.org/wiki/LaTeX>`_, `Markdown <http://en.wikipedia.org/wiki/Markdown>`_ or `reStructuredText <http://en.wikipedia.org/wiki/ReStructuredText>`_).

    Friendly advice: for your slideshows, don't hesitate to use something like `impress.js <http://bartaz.github.com/impress.js>`_. It's using HTML/JS/CSS and I highly recommend that you use it to do awesome presentations based on non-proprietary technologies. You can have a look at `reveal.js <http://lab.hakim.se/reveal-js/>`_ too, and its online editor `slide.es <http://slid.es/>`_.

**Teacher** 
    It's time to set an example for your student and to learn them one of the tool the will use during their entire life. A lot more than any other programming language.

**Coder** 
    To invest time in your daily tool is something essential. You'll anyway have to learn keyboard shortcuts, so you'd better do it for something useful. If this investment is style profitable 10 years from now, it's the perfect investment, it's |vim|.

**System and network administrator**
    If you're using *Emacs*, then I can forgive you. If you are using nano/pico, there is nothing I can do for you, otherwise, it's time to get some job done guys! To remotely administrate a Unix system is the perfect use case for |vim| (a powerful text editor without the need of a graphical interface).

**Writer** 
    If your are writing using Markdown/reStructuredText/WikiMarkup or LaTeX, |vim| will save you a lot of time. You'll not be able to go back to another editor after it, or you'll want to *Vimify* it at all costs.

Trust me, I am doing/did all this 5 roles, and my best investment has always been, by far, |vim|.

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
