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

How to create a new file?
-------------------------


The traditional way to create a file is to type, in normal mode, :vimcmd:`:e myfile.txt` to open an empty buffer. Then, save your buffer using :vimcmd:`:w`. Il will be saved as ``myfile.txt`` in the current directory.

You can also use Lusty Explorer (cf. :ref:`seclusty`). To do so, launch it using ``,lr`` or ``,lf`` (supposing that your leader key is ``,``), type the name of the file you want to create and then press |ttctrl| and |tte| at the same time. You can then save as above.

Undo/redo
---------

To undo, just press |ttu| while in normal mode. To undo your undo (and so, to redo) press |ttctrl| and |ttr| at the same time.

Reminders
=========

Files
-----

=================================================== ==================================== ============
Expected result                                     Action                               Comments
=================================================== ==================================== ============
**Save**                                            :vimcmd:`:w`
**Save as**                                         :vimcmd:`:w filename.txt`            Save as filename.txt but don't open filename.txt
**Save as / open**                                  :vimcmd:`:sav filename.txt`          Save as and open filename.txt
**Quit without saving (force quit)**                :vimcmd:`:q!`
**Save and quit**                                   :vimcmd:`:wq`                        
**Save as root**                                    :vimcmd:`:w !sudo tee %`             
=================================================== ==================================== ============

Moves
-----

=============================================================== ===========
Expected result                                                 Action
=============================================================== ===========
**Move one character left**                                     ``h``
**Move one line down**                                          ``j``
**Move one line up**                                            ``k``
**Move one character right**                                    ``l``
**Move to the end of the word**                                 ``e``
**Move to the beginning of the word**                           ``b``
**Move to the beginning of the next word**                      ``w``
**Move to line 42**                                             ``:42``
**Move to the beginning of the file**                           ``gg`` or ``:0``
**Move to the end of the file**                                 ``GG`` or ``:$``
**Move to the end of the line**                                 ``$``
**Move to the first non empty character of the line**           ``^``
**Move to the beginning of the line**                           ``0``
**Move one page down**                                          ``Ctrl+f``
**Move one page up**                                            ``Ctrl+b``
**Move to the first line of the screen**                        ``H``
**Move to the middle of the screen**                            ``M``
**Move to the last line of the screen**                         ``L``
=============================================================== ===========

Text editing
------------

=============================================================================== =========== ========================
Expected result                                                                 Action      Comments
=============================================================================== =========== ========================
**Insert before the cursor**                                                    ``i``       Normal mode
**Insert before the first non empty character of the line**                     ``I``       Normal mode 
**Insert after the cursor**                                                     ``a``       Normal mode 
**Insert at the end of the line**                                               ``A``       Normal mode 
**Insert a new line below**                                                     ``o``       Normal mode 
**Insert a new line above**                                                     ``O``       Normal mode 
**Replace everything after the cursor**                                         ``C``       Normal mode 
**Replace one character (and stay in normal mode)**                             ``r``       Normal mode 
**Delete the character after the cursor (like the del. key)**                   ``x``       Normal mode
**Delete the character before the cursor (like the backspace key)**             ``X``       Normal mode
**Delete the current line**                                                     ``dd``      Normal mode
**Copy the current line**                                                       ``yy``      Normal mode
**Paste after the cursor. If it's line, paste the line below.**                 ``p``       Normal mode
**Paste before the cursor. If it's line, paste the line above**                 ``P``       Normal mode 
**Switch the case (upper/lower)**                                               ``~``       Visual mode
**Move the text to the right (indent)**                                         ``>``       Visual mode
**Move the text to the left**                                                   ``<``       Visual mode
**In visual mode, delete the selected text**                                    ``d``       Visual mode
**In visual mode, replace the selected text**                                   ``c``       Visual mode
**In visual mode, copy the selected text**                                      ``y``       Visual mode
**Undo**                                                                        ``u``       Normal mode 
**Redo**                                                                        ``Ctrl+r``  Normal mode
=============================================================================== =========== ========================

Search and/or replace
---------------------

=================================================================== ======================= =================================
Expected result                                                     Action                  Comments
=================================================================== ======================= =================================
**Search**                                                          ``/*toto``              Search the *toto* string starting at the current cursor position
**Next**                                                            ``n``                   Go to the next search result
**Previous**                                                        ``N``                   Go to the previous search result
**Replace on the current line (once)**                              ``:s/toto/titi``        Replace toto by titi on the current line (once)
**Replace on the current line (multiple)**                          ``:s/toto/titi/g``      Replace toto by titi on the current line (for all occurences of toto)
**Replace on all the lines (once)**                                 ``:%s/toto/titi``       Replace toto by titi on all the lines of the file (once per line)
**Replace on all the lines (multiple)**                             ``:%s/toto/titi/g``     Replace toto by titi on all the lines of the file (for all occurences of toto)
**Replace on the current line, case insensitive (once)**            ``:s/toto/titi/i``      Replace toto by titi on the current line, case insensitive (once)
**Replace on the current line, case insensitive (multiple)**        ``:s/toto/titi/gi``     Replace toto by titi on the current line, case insensitive (for all occurences of toto)
=================================================================== ======================= =================================
