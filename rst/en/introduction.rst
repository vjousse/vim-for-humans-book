************
Introduction
************

When you need to write or to code, you have to choose a text editor, and a very good one. They are many text editors available out there, but very few of them are more than 40 years old. It's the case of *Emacs* (https://www.gnu.org/software/emacs/), *Vi*, and its improved successor |vim| (https://www.vim.org). They were created in the 70's and are still used a lot nowadays. You may have already noticed that it's not thanks to the beauty of their website or the efficiency of their communication (although I must admit that the *Emacs* site has made efforts since the first version of this book). Here are some **reasons for their success**:

**Forever** 
    You learn them once and you use them forever. In a world where languages and technologies are constantly changing, learning vim is a real chance to invest in a skill you'll be able to use forever.

**Everywhere**
    They are available for each and every possible platform : Mac Os X, Windows, GNU/Linux, BSD, and so on, and it's always been that way.

**Efficient** 
    Thanks to their features (like the extensive use of the keyboard), you can edit and write text as fast as your thoughts.

**For everything** 
    They allow you to edit everything and anything. When you'll use another programming language, or another markup language, you won't have to change your editor. Of course, this book has been written using |vim| (and the `ReST Markup <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_).

Yet, these text editors are difficult to learn. Not that they are harder than anything else, not that you can't handle it, but rather because there is no smart way out there to learn them for now. So, here we are.

The aim of this book is to address this gap by guiding you through your discovery of |vim|. I'll put *Emacs* aside from now and I'll focus on |vim|. If you want to know more about this **Editor war**, be sure to check the `Wikipedia page <https://en.wikipedia.org/wiki/Editor_war>`_. This book doesn't claim to be a reference book about |vim|. There are already a lot of good references on the subject like `A byte of Vim <https://vim.swaroopch.com/>`_. However, it claims to reduce the entry barrier to get used to |vim|. In my opinion, the most difficult thing about learning |vim| is not getting discouraged while finding a way to use it, learning |vim| step by step. We all have to get things done with our text editor on a daily basis, that's why losing all your productivity when switching to |vim| is not an option.

I'm sure you'll find a lot of people who will tell you: "Just do it cold turkey", "You'll see, it's hard at the beginning, but time will help". True, but you’ll still have the problem of trying to remain productive on a daily basis. The approach of this book is the following:

- Have a modern |vim|: syntax highlighting and nice colors.
- Use |vim| as any other text editor: easily edit code and switch between files using the mouse.
- Learn keyboard shortcuts and go without the mouse step by step.
- Install the *best* plugins to start using |vim| to its full potential.

Starting from bullet number 2, you'll already be able to use |vim| on a daily basis without losing a lot of productivity. It's where the magic will happen: if you can integrate |vim| in your daily habits, you have won. You'll then have the rest of your life to learn all the shortcuts and the tip and tricks of |vim|.

You're tired of trying a new editor each year? You're tired of having to relearn everything from scratch every time? You're tired having to change your editor when you're using your Mac, Windows or Linux? So, just stop it, and join the community of people happy with their text editor!

What about Neovim?
==================

A quick aside about *Neovim* https://neovim.io/ (if you don't know what it is, you can skip this part). I've decided to concentrate solely on |vim| in this book so as not to frustrate people who can only use |vim|.

If you're a *Neovim* user, everything in this book is still valid, as *Neovim* is compatible with |vim|. What's more, modes, text manipulations and everything else that doesn't concern plugins is common to both |vim| and *Neovim*: learning them for |vim| or for *Neovim* makes no difference. In fact, you can follow this book using *Neovim* instead of |vim| without any problems.

The special feature of *Neovim* is that it is more actively maintained than |vim| and, among other things, uses the **Lua** programming language for plugin management. As a result, plugins written for *Neovim* are not compatible with |vim| (the reverse is not true: plugins written for |vim| are compatible with *Neovim*). Part of the |vim| community has switched to *Neovim*, and plugins for *Neovim* are flourishing much faster than those for |vim|. For the purpose of this book, this won't make any difference and you can follow it without any problem with |vim| or *Neovim*. I may be making more *Neovim*-specific content in the future.


For who?
========

Every person having to produce text (code, book, reports, slideshows, …) regularly. Developers are of course concerned, but it's not only about them.

For example, if you are a:

**Student**
    If you want to impress your future boss with your resume, it's a must. It's a proof of seriousness to see that a student took the time to learn |vim| on his or her own. Moreover, you'll have a unique tool to write all what you'll have to write (and that you'll be able to use for the rest of your career): your LaTeX reports, your slideshows, your code (if you need Word or LibreOffice to write you reports, it's time to use `LaTeX <http://en.wikipedia.org/wiki/LaTeX>`_, `Markdown <http://en.wikipedia.org/wiki/Markdown>`_ or `reStructuredText <http://en.wikipedia.org/wiki/ReStructuredText>`_).

    Friendly advice: for your slideshows, don't hesitate to use something like `impress.js <http://bartaz.github.com/impress.js>`_. It's using HTML/JS/CSS and I highly recommend that you use it to do awesome presentations based on non-proprietary technologies. You can have a look at `reveal.js <http://lab.hakim.se/reveal-js/>`_ too, and its online editor `slide.es <http://slid.es/>`_.

**Teacher** 
    It's time to set an example for your students and to teach them a tool they will use during their entire life. |Vim| is something they'll be able to use a lot more than any programming language.

**Coder** 
    It's essential to invest time in your daily tool. You'll be learning keyboard shortcuts anyway, so you should do it for something useful. If this investment is still profitable 10 years from now, it's the perfect investment. If you put time into learning |vim|, you will be able to use it for many decades.

**System and network administrator**
    If you use *Emacs*, then I can forgive you. If you use nano/pico, there is nothing I can do for you. Otherwise, it's time to get some work done, folks! Remote administration of a Unix system is the perfect use case for |vim| (a powerful text editor without the need of a graphical interface).

**Writer** 
    If you write using Markdown/reStructuredText/WikiMarkup or LaTeX, |vim| will save you a lot of time. You'll not be able to go back to another editor after it, or you'll want to *Vimify* it at all costs.

Trust me, I have done and still do all these 5 roles, and my best investment has always been, by far, |vim|.

What you will be learning
=========================

- How to use |vim| as a "usual" editor first (you know, the type of text editors having syntax highlighting, allowing you to open files, to click using the mouse, …). In short, we will be demystifying |vim| to allow you to go further.
- How to move from classical text editing to the power of |vim|, baby step by baby step (it's where addiction begins).
- How to do without the mouse and why it's the best thing that can happen to you when you're programming/writing text.
- How you can easily deduce keyboard shortcuts with some simple rules.

To sum up: if you consider yourself a craftsman, act like one. Learn how to use your tool, once and for all.

What you will not be learning
=============================

- You will not be learning how to install and to configure |vim| for Windows. It's doable, but I have very limited knowledge about Windows. It may happen, but not yet. Only Linux/Unix will be discussed (and by extension Mac OS X).
- You will not be learning how to use *Vi* (notice the lack of "*m*"). I'll only teach you how to be productive writing text with |vim|, I won't be teachng you how to impress your friends with *Vi* (and anyway, |vim| is enough for that). For those who don't get what I'm talking about, *Vi* is the "ancestor of |vim| (which stands for *Vi* - *IMproved*)" and is installed by default on all Unix-like systems (even on Mac OS X).
- You will not be learning to know |vim| by heart: this book is not a reference it's a pragmatic smart way to learn |vim|.
- You will not learn how to pimp the colors of your |vim|, although I will go over how to change your theme. I'll use the `Solarized <http://ethanschoonover.com/solarized>`_ theme, it's the best theme for your eyes.

The hardest part is to get started
==================================

So, your are ready for the adventure? Ready to sacrifice one hour to start using |vim|, one week to be familiar with it, and the rest of your life to be happy with your choice? So here we go! Well, almost, we need to talk a little bit before.

With |vim| you'll have to struggle. No matter how big your willpower is, you will struggle. Be prepared. The goal of this guide is to diminish this struggle as much as possible, but be aware that you will struggle anyway. No pain, no gain. Here is the method I recommend to tame the beast:

- Try to make using |vim| a habit. Be sure to follow this guide until the chapter about *The NERD Tree* (the file explorer). Then you'll be able to use |vim| as you would do with Notepad++, Textmate or Sublime Text for example. You'll be using only 1% of the capacities of |vim|, but whatever. What really matters is to use |vim| on a daily basis.
- Be sure to have a printed sheet with all the main |vim| shortcuts near you. The goal here is not to learn them by heart, but only to have somewhere to look when you'll ask yourself: "There must be a better way to do this".
- Keep the faith. At the beginning you'll be sceptical regarding the usefulness of learning everything from scratch with |vim|. And then, one day, you'll have that "a-ha!" moment. You'll be asking yourself why all the software you're using can't be controlled using |vim| shortcuts.
- Keep in mind that it's an investment for your next 20 years. As you know, investments are rarely profitable immediately.

So, enough talking, let's get started!
