\chapter{Pense-bête et exemples}

Nous venons de faire un tour d'horizon de tout ce qui est nécessaire pour bien commencer dans la vie avec |vim|. Tout cela devrait être suffisant pour pouvoir l'utiliser au quotidien. C'est le secret de la réussite avec |vim| : réussir à l'encrer dans nos habitudes journalières. Une fois que cela est fait, le reste devrait couler de source.

Cette dernière partie est là pour vous donner un endroit de référence où vous pourrez revenir comme bon vous semble lorsque vous serez un peu perdu sur comment faire telle ou telle chose avec |vim|. Ce chapitre est composé de deux parties. La première est un ensemble de questions réponses qui couvre les principaux problèmes que les débutants rencontrent lorsqu'ils commencent. Le but est de répondre aux questions du type : « rha mais comment on fait ça, c'était pourtant si simple avec mon ancien éditeur ». La seconde partie est une liste (non exhaustive) des commandes |vim| les plus utiles dont vous pourrez vous servir comme pense-bête. Allez hop, au boulot.

\section{Questions / réponses}

\subsection{Comment quitter |vim| ?}

La première chose à faire est de se mettre en mode normal. Grosso modo, excitez-vous sur |ttesc| ou |ttsemicolon| en fonction de votre configuration et vous devriez vous retrouver en mode normal. Ensuite tapez :vimcmd:`:q` pour quitter. Il y a de grandes chances que |vim| ne vous laisse pas faire. Si vous avez des modifications non enregistrées par exemple, il ne voudra pas quitter. Vous pouvez annuler les modification en le forçant à quitter grâce à l'utilisation de :vimcmd:`!` comme ceci : :vimcmd:`:q!`. Vous pouvez aussi enregistrer vos modifications puis quitter comme ceci : :vimcmd:`:wq`.

\subsection{Comment sauvegarder sous ?}

En mode normal, si vous tapez :vimcmd:`:w`, |vim| par défaut sauvegarde vos modifications dans le fichier courant. Si vous souhaitez utiliser un autre nom de fichier pour « sauvegarder sous », vous avez juste à lui spécifier le nom du fichier après :vimcmd:`w` comme ceci : :vimcmd:`:w monfichier.txt`. |vim| sauvegardera alors votre fichier sous le nom *monfichier.txt*. En revanche |vim| n'ouvrira pas *monfichier.txt*, il restera sur votre précédent fichier.

Si vous souhaitez que |vim| sauvegarde sous *monfichier.txt* et ouvre ensuite ce fichier dans le tampon courant, vous devrez utiliser :vimcmd:`:sav monfichier.txt`.

\subsection{Comment copier/couper coller ?}

Celle là est facile, j'y ai déjà consacré un chapitre, cf. \nameref{sec:se-deplacer}. 

En résumé :

\begin{itemize}
    \item Passez en mode visuel avec |ttv|,
    \item Sélectionnez ce que vous voulez copier en vous déplaçant,
    \item Copiez avec |tty| ou couper avec |ttx| ou |ttd|,
    \item Collez après l'emplacement du curseur avec |ttp| ou avant l'emplacement du curseur avec |ttP|.
\end{itemize}

\subsection{Comment créer un nouveau fichier ?}

La façon traditionnelle de faire est de taper, en mode normal, :vimcmd:`:e monfichier.txt` pour ouvrir un tampon (buffer) vide. Ensuite, sauvegardez votre tampon grâce à :vimcmd:`:w`. Il sera sauvegardé sous le nom ``monfichier.txt`` dans le répertoire courant.

Vous pouvez aussi utiliser Lusty Explorer (cf. \nameref{lusty}) pour ce faire. Lancez le grâce à :vimcmd:`,lr` ou :vimcmd:`,lf`, tapez le nom du fichier que vous souhaitez créer puis appuyez sur |ttctrl| puis en même temps |tte|. Vous pouvez ensuite le sauvegarder de la même manière que ci-dessus.

\subsection{Annuler / Refaire}

Pour annuler il suffit d'utiliser |ttu| en mode normal. Pour annuler le annuler (donc refaire) maintenez |ttctrl| appuyée puis |ttr|.

\section{Pense-bête}

\section{Fichiers}

\begin{tabularx}{17cm}{|X|c|X|}
  \hline
  Résultat attendu & Action & Commentaire \\
  \hline \hline
  **Sauvegarder** & :vimcmd:`:w` & (w pour write)\\
  \hline
  **Sauvegarder sous** & :vimcmd:`:w *nomdefichier.txt`* & Sauvegarde sous nomdefichier.txt mais n'ouvre pas nomdefichier.txt \\
  \hline
  **Sauvegarder sous / ouvre** & :vimcmd:`:sav *nomdefichier.txt`* & Sauvegarde sous et ouvre nomdefichier.txt  \\
  \hline
  **Quitter sans sauvegarder (forcer à quitter)** & :vimcmd:`:q!` & \\
  \hline
  **Sauvegarder et quitter** & :vimcmd:`:wq` (wq pour write and quit) & \\
  \hline
\end{tabularx}

\section{Déplacements}

\begin{tabularx}{17cm}{|X|c|}
  \hline
  Résultat attendu & Action \\
  \hline \hline
  **Se déplacer d'un caractère à gauche** & :vimcmd:`h` \\
  \hline
  **Se déplacer d'un caractère en bas** & :vimcmd:`j` \\
  \hline
  **Se déplacer d'un caractère en haut** & :vimcmd:`k` \\
  \hline
  **Se déplacer d'un caractère à droite** & :vimcmd:`l` \\
  \hline
  **Se déplacer à la fin d'un mot** & :vimcmd:`e` \\
  \hline
  **Se déplacer au début d'un mot** & :vimcmd:`b` \\
  \hline
  **Se déplacer au début du mot suivant** & :vimcmd:`w` \\
  \hline
  **Se déplacer à la ligne 42** & :vimcmd:`:42` \\
  \hline
  **Se déplacer au début du fichier** & :vimcmd:`gg` ou :vimcmd:`:0` \\
  \hline
  **Se déplacer à la fin du fichier** & :vimcmd:`GG` ou :vimcmd:`:\$` \\
  \hline
  **Se déplacer à la fin de la ligne** & :vimcmd:`\$` \\
  \hline
  **Se déplacer au premier caractère non vide de la ligne** & :vimcmd:`\^{ `} \\
  \hline
  **Se déplacer au début de la ligne** & :vimcmd:`0` \\
  \hline
  **Descendre d'une page** & :vimcmd:`Ctrl+f` \\
  \hline
  **Monter d'une page** & :vimcmd:`Ctrl+b` \\
  \hline
  **Se déplacer à la première ligne de l'écran** & :vimcmd:`H` \\
  \hline
  **Se déplacer au milieu de l'écran** & :vimcmd:`M` \\
  \hline
  **Se déplacer à la dernière ligne de l'écran** & :vimcmd:`L` \\
  \hline
\end{tabularx}

\section{Édition de texte}

\begin{tabularx}{17cm}{|X|c|X|}
  \hline
  Résultat attendu & Action & Commentaire \\
  \hline \hline
  **Insérer avant le curseur** & :vimcmd:`i` & \\
  \hline
  **Insérer avant le premier caractère non vide de la ligne** & :vimcmd:`I` & \\
  \hline
  **Insérer après le curseur** & :vimcmd:`a` & \\
  \hline
  **Insérer à la fin de la ligne** & :vimcmd:`A` & \\
  \hline
  **Insérer une nouvelle ligne en dessous** & :vimcmd:`o` & \\
  \hline
  **Insérer une nouvelle ligne au dessus** & :vimcmd:`O` & \\
  \hline
  **Remplace le reste de la ligne** & :vimcmd:`C` & \\
  \hline
  **Remplace un seul caractère (et reste en mode normal)** & :vimcmd:`r` & \\
  \hline
  **Supprime le caractère après le curseur (comme la touche suppr.)** & :vimcmd:`x` & \\
  \hline
  **Supprime le caractère avant le curseur (comme la touche backspace)** & :vimcmd:`X` & \\
  \hline
  **Supprime la ligne courante** & :vimcmd:`dd` & \\
  \hline
  **Copie la ligne courante** & :vimcmd:`yy` & \\
  \hline
  **Colle après le curseur. Si c'est une ligne, colle la ligne en dessous.** & :vimcmd:`p` & \\
  \hline
  **Colle avant le curseur. Si c'est une ligne, colle la ligne au dessus.** & :vimcmd:`P` & \\
  \hline
  **Intervertit la case des caractères (majuscules / minuscules)** & :vimcmd:`|textasciitilde`| & Marche en mode visuel\\
  \hline
  **Déplace le texte vers la droite (indentation)** & :vimcmd:`>` & Marche en mode visuel \\
  \hline
  **Déplace le texte vers la gauche** & :vimcmd:`<` & Marche en mode visuel \\
  \hline
  **En mode visuel, supprime la sélection** & :vimcmd:`d` & Mode visuel \\
  \hline
  **En mode visuel, remplace la sélection** & :vimcmd:`c` & Mode visuel \\
  \hline
  **En mode visuel, copie la sélection** & :vimcmd:`y` & Mode visuel \\
  \hline
  **Annuler (Undo)** & :vimcmd:`u` & \\
  \hline
  **Refaire (Redo)** & :vimcmd:`Ctrl+r` & \\
  \hline
\end{tabularx}

\section{Chercher et/ou remplacer}

\begin{tabularx}{17cm}{|X|c|X|}
  \hline
  Résultat attendu & Action & Commentaire \\
  \hline \hline
  **Rechercher** & :vimcmd:`/*toto`* & Cherche la chaîne de caractères *toto* à partir de l'emplacement courant du curseur \\
  \hline
  **Suivant** & :vimcmd:`n` & Affiche le prochain résultat de recherche\\
  \hline
  **Précédent** & :vimcmd:`N` & Affiche le précédent résultat de recherche\\
  \hline
  **Remplacer sur la ligne courante** & :vimcmd:`:s/toto/titi` & Remplace toto par titi sur la ligne courante (une fois)\\
  \hline
  **Remplacer tout sur la ligne courante** & :vimcmd:`:s/toto/titi/g` & Remplace toto par titi sur la ligne courante (pour toutes les occurrences de toto)\\
  \hline
  **Remplacer dans toutes les lignes** & :vimcmd:`:\%s/toto/titi` & Remplace toto par titi sur toutes les lignes du fichier (une fois par ligne)\\
  \hline
  **Remplacer tout dans toutes les lignes** & :vimcmd:`:\%s/toto/titi/g` & Remplace toto par titi sur toutes les lignes du ficher (pour toutes les occurrences de toto par ligne)\\
  \hline

  **Remplacer sur la ligne courante en ignorant la casse** & :vimcmd:`:s/toto/titi/i` & Remplace toto par titi sur la ligne courante (une fois)\\
  \hline
  **Remplacer tout sur la ligne courante en ignorant la casse** & :vimcmd:`:s/toto/titi/gi` & Remplace toto par titi sur la ligne courante (pour toutes les occurrences de toto)\\
  \hline
\end{tabularx}


