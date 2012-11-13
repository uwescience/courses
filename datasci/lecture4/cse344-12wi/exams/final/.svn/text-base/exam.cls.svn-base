% exam.cls
%
% A LaTeX2e document class for preparing exams.

%% exam.cls
%% Copyright (c) 1994, 1997, 2000, 2004, 2008 Philip S. Hirschhorn
%
% This work may be distributed and/or modified under the
% conditions of the LaTeX Project Public License, either version 1.3
% of this license or (at your option) any later version.
% The latest version of this license is in
%   http://www.latex-project.org/lppl.txt
% and version 1.3 or later is part of all distributions of LaTeX
% version 2003/12/01 or later.
%
% This work has the LPPL maintenance status "author-maintained".
% 
% This work consists of the files exam.cls and examdoc.tex.


% The user documentation for exam.cls is in the file examdoc.tex.


%%% Philip Hirschhorn
%%% Department of Mathematics
%%% Wellesley College
%%% Wellesley, MA 02481
%%% psh@math.mit.edu

% The newest version of this documentclass should always be available
% from my web page: http://www-math.mit.edu/~psh/


\def\fileversion{2.3}
\def\filedate{2008/07/19}
%---------------------------------------------------------------------
%---------------------------------------------------------------------
% 
% If there's some feature that you'd like that this file doesn't
% provide, tell me about it.
% 
%
%
%
%
% Thanks to:
%
% Piet van Oostrum, from whose excellent ``fancyheadings.sty'' we
% shamelessly stole most of the code for setting the headers and
% footers.
%
% Mate Wierdl <mw@wierdlmpc.msci.memphis.edu>, who contributed the
% code so that if the number of points is ``1'', then the default
% value of \pointname will print ``1 point'' instead of ``1 points''.
%
% Tom Brikowski <brikowi@utdallas.edu>, who contributed the code for
% making the number of points and number of questions available as
% macros (as well as the idea of putting the number of points in a 
% box, instead of in parentheses).  (I changed his code to make this
% all optional, so if there are errors there, it's my fault and not
% his.)
%
% Ottmar Beucher <beucher@fh-karlsruhe.de>, Dan Drake
% <drake@math.umn.edu>, and Justus Piater <Justus.Piater@ULg.ac.be> who
% contributed ideas and code for the \pointsofquestion and \gradetable
% commands for printing a Grading Table.  (I changed all the code to
% make this compatible with hyperref.sty, so if there are errors there,
% it's my fault and not theirs.)
%
% Justus Piater <Justus.Piater@ULg.ac.be>, who contributed the code for
% the solution environment.  (I changed his code to allow page breaks
% inside solutions so, once again, if it's buggy, it's my fault.) 
%
% Donald Arseneau <asnd@triumf.ca>, who created the excellent
% ``framed.sty'' and generously allowed me to include basically the
% whole thing in exam.cls, making the few changes needed for it to
% work well with question environments:
% framed.sty   v 0.8a   21-Jul-2003
% Copyright (C) 1992-2003 by Donald Arseneau
% These macros may be freely transmitted, reproduced, or modified
% provided that this notice is left intact.
%
%--------------------------------------------------------------------
%--------------------------------------------------------------------
%                    Changelog since version 2.2:

%--------------------------------------------------------------------
% Version 2.3, 2008/07/16:
%
% Minor typographic corrections to comments.
%
%--------------------------------------------------------------------
% Version 2.222$\beta$, 2008/07/13:
%
% Corrected a typo in the error message displayed when
% \shadedsolutions is used without having said \usepackage{color}.
%
%--------------------------------------------------------------------
% Version 2.221$\beta$, 2008/07/03:
%
% \themarginpoints used to expand to 
%     \@points \@marginpointname
% whether the points were bonus or non-bonus.  We fixed that, so that
% it expands to either
%     \@points \@marginbonuspointname
% or
%     \@points \@marginpointname
% depending on whether or not the points are bonus points.
%
%--------------------------------------------------------------------
% Version 2.220$\beta$, 2008/05/24:
%
% New command: \fillwithdottedlines 
% New environment: solutionordottedlines
%
%
% \fillwithdottedlines is similar to \fillwithlines except that it
% inserts dotted lines (created by \dotfill) instead of solid lines.
%
% \fillwithdottedlines takes one argument, which is either a length or
% \fill, and it fills that much vertical space with dotted horizontal
% lines that run the length of the current line.  That is, they extend
% from the current left margin (which depends on whether we're in a
% question, part, subpart, or subsubpart) to the right margin.
%
% The distance between the lines is \dottedlinefillheight, whose
% default value is set with the command
%
%   \setlength\dottedlinefillheight{.25in}
%
% This value can be changed by giving a new \setlength command.
%
% The solutionordottedlines environment is almost identical to the
% solutionorlines environment, except that when solutions are not
% being printed and an optional argument appears specifying an amount
% of space to be left for answers, that space is filled with dotted
% lines (created by \dotfill), rather than filled with solid lines (as
% it is by the solutionorlines environment).
%
%--------------------------------------------------------------------
% Version 2.219$\beta$, 2007/11/24:
% 
% There can now be partial grade tables and point tables, either bonus
% or non-bonus.
% 
% New commands:
% 
%   \partialgradetable
%   \partialbonusgradetable
%   \partialpointtable
%   \partialbonuspointtable
%   \begingradingrange
%   \endgradingrange
% 
% The user defines a grading range by saying
% 
%   \begingradingrange{whatever}
% 
% to start the range and
% 
%   \endgradingrange{whatever}
% 
% to end the range (where ``whatever'' is a name chosen by the user).
% To create the table, the user says, e.g., 
% 
%   \partialgradetable{whatever}[v][questions]
% 
% That is, each of \partialgradetable, \partialbonusgradetable,
% \partialpointtable, and \partialbonuspointtable takes
% 
%   one required argument (the name of the grading range) and
% 
%   two optional arguments, the first being either ``[v]'' or ``[h]'',
%   the second being either ``[questions]'' or ``[pages]''.
% 
% If either or both of the optional arguments are omitted, [questions]
% and [v] will be used.
% 
% If the table is indexed by questions, then it will include all
% questions following the \begingradingrange{whatever} and preceding the
% \endgradingrange{whatever}.
% 
% If the table is indexed by pages, then it will include all pages with
% points starting with the page containing the
% \begingradingrange{whatever} and ending with the page containing the
% \endgradingrange{whatever}.
% 
% Otherwise, 
% 
%   \partialgradetable is similar to \gradetable
%   \partialbonsugradetable is similar to \bonusgradetable
%   \partialpointtable is similar to \pointtable
%   \partialbonuspointtable is similar to \bonuspointtable
% 
%--------------------------------------------------------------------
% Version 2.218$\beta$, 2007/10/31:
% 
% Instead of appending
%   \the \pageinfo@commands \the \point@toks 
% to \everypar, we insert them into the box \@labels.  This corrects the
% problem that arose when a question (or part, etc.) begins with a list
% environment (including verbatim, flushleft, center, flushright, and
% possibly others that are implemented as trivlist environments).  The
% \item command in those environments throws away the previous contents
% of \everypar, and so the tokens
%   \the \pageinfo@commands \the \point@toks
% didn't get inserted where we expected.  List environments *do*
% preserve the contents of the box \@labels, though.

% This version of exam.cls is not completely backward compatible with
% older versions.  The changes only affect documents in which the user
% was doing something that probably should not have been done with the
% older versions, though.  This new version does something useful in
% situations in which older versions did something not very useful:

% This change introduces a change in behavior for documents in which a
% question with points begins with a parts environment, so that the
% points for the first part (if any) would appear on the same line as
% the points for the question.  In earlier versions of exam.cls, the
% points for the question would not be printed if there are points for
% the part that begins on the same line.  In this version of exam.cls,
% all points will be printed.  If they're both printed in the left
% margin, or both in the right margin, then they'll be printed directly
% on top of one another, which is not what you want.  (You can use
% \pointsinmargin, \pointsinrightmargin, and \nopointsinmargin to print
% them in different places.)  If points are being printed right in the
% text (i.e., \nopointsinmargin), then the points for the question will
% be printed *before* the label (a) for the first part is printed.

% The behavior of this new version of exam.cls seems clearly preferable
% to the old behavior, but it is a change!
%
%--------------------------------------------------------------------
% Version 2.217$\beta$, 2007/10/22:
% 
% We changed things so that we're now compatible with calc.sty
%
% calc.sty redefines \setcounter and \addtocounter in a way that
% conflicts with a trick we were using to deal with \half points.
%
% We replaced one \setcounter command with
%
%    \global\csname c@#1\endcsname 0#2\relax
%
% and one \addtocounter command with
%
%    \global\advance\csname c@#1\endcsname 0#2\relax
%
%--------------------------------------------------------------------
% Version 2.216$\beta$, 2007/08/27:
% 
% The command \answerline now takes an optional argument.  If the
% optional argument appears, then when \printanswers is true the
% argument will be printed on the answer line.  When \printanswers is
% false, the optional argument is ignored.
% 
% When the argument is printed, it is printed with
% \CorrectChoiceEmphasis and it is a distance of \answerclearance above
% the line.  The default value of \answerclearance is set with the
% command
% 
% \setlength\answerclearance{0.2ex}
% 
% and it can be changed with a \setlength command.
% 
% The optional argument is centered on the answer line unless it is too
% long, in which case it extends to the right of the answer line.
% 
%--------------------------------------------------------------------
% Version 2.215$\beta$, 2007/08/24:
% 
% New commands:
% 
%   \pointtable
%   \bonuspointtable
% 
% Both of these take up to two optional arguments:
% 
%   The first can be either [v] or [h].
%   The second can be either [questions] or [pages].
% 
% These commands are similar to the commands
% 
%   \gradetable
%   \bonusgradetable
% 
% except that the new commands print only two columns (or rows),
% omitting the column (or row) for the score.
% 
%--------------------------------------------------------------------
% Version 2.214$\beta$, 2007/07/19:
%
% New commands:
%
%   \questionshook
%   \partshook
%   \subpartshook
%   \subsubpartshook
%   \choiceshook
%
% These are for advanced users who want to customize the list
% parameters (\topsep, \partopsep, \itemsep, \parsep, etc.) for the
% lists that these environments create.  They are all defined to be
% empty, but the user can change them using \renewcommand.
%
%--------------------------------------------------------------------
% Version 2.213$\beta$, 2006/11/27:
% 
%  New documentclass option: addpoints
%  Using this option is equivalent to giving the command
%    \addpoints
%  at the beginning of the document.
% 
% New commands:
% 
%   \bonusquestion
%   \bonustitledquestion
%   \bonuspart
%   \bonussubpart
%   \bonussubsubpart
% 
%   \bonuspointsofquestion
%   \bonuspointsonpage
% 
%   \numbonuspoints
% 
%   \bonuspointpoints
%   \bonuspointformat
%   \thebonuspoints
%   \bonuspoints
%   \bonuspointname
%   \marginbonuspointname
%
%   \bonusgradetable
% 
%   \bhqword
%   \bhpword
%   \bhsword
%   \bhtword
%   \bvqword
%   \bvpword
%   \bvsword
%   \bvtword
% 
%   \bvpgword
%   \bhpgword
% 
% 
% The commands
% 
%    \bonusquestion
%    \bonustitledquestion
%    \bonuspart
%    \bonussubpart
%    \bonussubsubpart
% 
% are the same as the commands
% 
%    \question
%    \titledquestion
%    \part
%    \subpart
%    \subsubpart
% 
% except that any points assigned become ``bonus points'', which by
% default are typeset in the form
% 
%   1. (1 point (bonus))
% 
% or
% 
%   1. (2 points (bonus))
% 
% If no points are assigned, then these ``bonus'' versions of the
% commands are equivalent to the non-bonus versions.
% 
% The command
% 
%   \bonusgradetable
% 
% is analogous to the command \gradetable; it can be used in any of the
% four forms
% 
%   \bonusgradetable[v][questions]
%   \bonusgradetable[h][questions]
%   \bonusgradetable[v][pages]
%   \bonusgradetable[h][pages]
% 
% and it counts only bonus points, while \gradetable counts only
% non-bonus points.
% 
% The commands
% 
%   \bonuspointsofquestion
%   \bonuspointsonpage
%   \numbonuspoints
% 
% are analogous to the commands
% 
%   \pointsofquestion
%   \pointsonpage
%   \numpoints
% 
% The remaining new commands are for customizing the appearance of bonus
% points and bonusgradetable.  The command
% 
%   \bonuspointpoints
% 
% is analogous to the command \pointpoints; it takes two arguments, the
% first of which will appear after 1 or \half points the second to
% appear after any other number of points.  The default was created by
% the equivalent of the command
% 
%   \bonuspointpoints{point (bonus)}{points (bonus)}
% 
% If, for example, you give the command
% 
%   \bonuspointpoints{bonus point}{bonus points}
% 
% then bonus points will look like
% 
%   1. (1 bonus point)
% 
% or
% 
%   1. (2 bonus points)
% 
% (The commands \bracketedpoints, \boxedpoints, and \nobracketedpoints
% have the same effect on bonus points that they have on non-bonus
% points, and the command \marksnotpionts replaces ``point'' with
% ``mark'' in all of these cases.)
% 
% \bonuspointname is analogous to \pointname, and the defaults were
% created by the commands
% 
%   \pointname{ \points}
%   \bonuspointname{ \bonuspoints}
% 
% (Note the intentional space in each of those commands.)
% 
% \marginbonuspointname is analogous to \marginpointname, and the
% default was created by the command
% 
%   \marginbonuspointname{ (bonus)}
% 
% \bonuspointformat is analogous to \pointformat.
% 
% 
% The commands for customizing the words used in \bonusgradetable are
% analogous to those used for customizing the words used in \gradetable,
% except that they begin with a ``b'':
% 
%   \bhqword      is analogous to     \hqword 
%   \bhpword      is analogous to     \hpword 
%   \bhsword      is analogous to     \hsword 
%   \bhtword      is analogous to     \htword 
%   \bvqword      is analogous to     \vqword 
%   \bvpword      is analogous to     \vpword 
%   \bvsword      is analogous to     \vsword 
%   \bvtword      is analogous to     \vtword 
%                 is analogous to             
%   \bvpgword     is analogous to     \vpgword
%   \bhpgword     is analogous to     \hpgword
% 
%
%--------------------------------------------------------------------
% Version 2.212$\beta$, 2006/11/13:
%
% Made \useslantedhalf and \usehorizontalhalf global.
%
%--------------------------------------------------------------------
% Version 2.211$\beta$, 2006/10/29:
%
% New commands:
%
%   \pointformat
%   \themarginpoints
%
% An old command that's also useful here is
%
%   \thepoints
%
% \pointformat: The \pointformat command allows you to change the
% format used to print the points.  It takes one argument, and that
% argument becomes the command to print the points, whether the points
% are being printed at the beginning of the question, in the left
% margin (because of \pointsinmargin), in the right margin (because of
% \pointsinrightmargin), or dropped in the right margin at the end of
% the question (because of \pointsdroppedatright).
%
% The argument to \pointformat should contain either the command
%
%   \thepoints
%
% which expands to the number of points followed by the argument to
% the last \pointname command, or the command
%
%   \themarginpoints
%
% which expands to the number of points followed by the argument to
% the last \marginpointname command.
%
% For example, the command \bracketedpoints is equivalent to
%
%   \pointformat{[\thepoints]}
%
% if points are not being printed in the margin and to
%
%   \pointformat{[\themarginpoints]}
%
% if points are being printed in the margin.
%
% For another example, the command \boxedpoints is equivalent to
%
%   \pointformat{\fbox{\thepoints}}
%
% if points are not being printed in the margin and to
%
%   \pointformat{\fbox{\themarginpoints}}
%
% if points are being printed in the margin.
%
% For another example, if you give the commands
%
%   \pointsinmargin
%   \marginpointname{\%}
%   \pointformat{\slshape (\themarginpoints)}
%
% then the points will be printed in the left margin, followed by the
% symbol `%', surrounded by parentheses, all in slanted type.
%
% For another example, if you give the commands
%
%   \pointsinrightmargin
%   \marginpointname{\%}
%   \pointformat{\fbox{\bfseries \boldmath \themarginpoints}}
%
% then the points will be printed in the right margin, followed by the
% symbol `%', all in bold and surrounded by a box.  (Note: The commands
% \bfseries and \boldmath  are needed here because the ``one half''
% printed when you use half points is printed in math mode while the
% rest of the points are printed in text mode.)
%
%--------------------------------------------------------------------
% Version 2.210$\beta$, 2006/09/28:
%
% Fixed the bug that prevented having two consecutive \correctchoice's
% in a choices or oneparchoices environment.
%
%--------------------------------------------------------------------
% Version 2.209$\beta$, 2006/05/26:
%
% We corrected the problem that \ifcontinuation and \ifincomplete paid
% attention only to parts, subparts, and subsubparts when deciding on
% which page a question ended, but ignored choices.  We corrected this,
% so that a question is now thought to end on the page on which its last
% part, subpart, subsubpart, or choice begins.
%
%--------------------------------------------------------------------
% Version 2.208$\beta$, 2006/01/30:
% 
% We corrected the description of the usage of \ifthenelse in the
% comments describing what's new in version 2.207beta.
% 
%--------------------------------------------------------------------
% Version 2.207$\beta$, 2006/01/29:
% 
% New feature: It's possible to say
% 
%   \ifprintanswers
%     Some stuff
%   \fi
% 
% to insert ``Some stuff'' only when answers are being printed.  It's
% also possible to say
% 
%   \ifprintanswers
%     Some stuff
%   \else
%     Other stuff
%   \fi
% 
% to insert ``Some stuff'' when answers are being printed and ``Other
% stuff'' when answers aren't being printed.
% 
% Alternatively, it's possible to accomplish the same thing by saying
% 
%   \ifthenelse{\boolean{printanswers}}{Some stuff}{Other stuff}
% 
% If you want to ``Stuff'' only when answers aren't being printed, you
% can say either
% 
%   \ifprintanswers
%   \else
%     Stuff
%   \fi
% 
% or
% 
%   \ifthenelse{\boolean{printanswers}}{}{Stuff}
% 
% We accomplished this by changing all uses of \if@printanswers,
% \@printanswerstrue, and \@printanswersfalse to \ifprintanswers,
% \printanswerstrue, and \printanswersfalse.
% 
%--------------------------------------------------------------------
% Version 2.206$\beta$, 2005/08/24:
% 
% New feature: When using a grading table indexed by questions, it's
% possible to replace the question numbers in the table with titles
% for the questions.
%
% 
% There are two new commands: \titledquestion and \thequestiontitle.
% 
% 
% \titledquestion is a replacement for \question; it has one required
% argument (the title) and one optional argument (the point value), as
% in
% 
%   \titledquestion{Question \thequestion: Concepts}
% 
% which sets the question title to ``Question 2: Concepts'' (if this
% is the second question) and doesn't set any pointvalues, or
% 
%   \titledquestion{Design}[10]
%   
% which sets the question title to ``Design'' and sets the pointvalue
% to ``10''.  (Note that the question title doesn't include the number
% of the question unless you put it there using the \thequestion
% command.)
% 
% The title of the question then automatically replaces the question
% number in a grading table indexed by question numbers.
% 
% 
% 
%
% 
% \thequestiontitle: This command expands to the question title.  This
% is for use in the argument of a \qformat command, so that you can make
% the question title appear in the actual question.
% 
% If a question is begun with \question (instead of \titledquestion),
% then the value of \thequestiontitle will automatically be set to the
% number of the question.
% 
% Note: The contents of \thequestiontitle don't appear anywhere in the
% actual question unless you do something to make it appear.  For
% example, the command
% 
% \qformat{\textbf{Question \thequestion: \thequestiontitle}\dotfill\thepoints}
% 
% would insert the number of the question along with the title of the
% question and the point value at the beginning of the question.
% 
% 
% Note: If you use a grading table indexed by questions and you use the
% \titledquestion command, then the number of the question won't appear
% in the grading table unless you include \thequestion in the title of
% the question.
% 
%
% Note: If \thequestion appears in both the argument to \qformat and the
% title of the question, then the question number will be printed
% twice.
% 
% 
% If the command \thequestiontitle is never used, then the only effect
% of using the command \titledquestion is that in a grading table
% indexed by question number, this question will be indexed by the
% number of the question, rather than by the argument to
% \titledquestion, and the title of the question would never appear
% except in the grading table.
%
% 
%--------------------------------------------------------------------
%
% Version 2.205$\beta$, 2005/08/22:
%
% Bug fix: If a question began with a parts environment (i.e., if the
% parts environment began before we entered horizontal mode in the
% question), then a grading table indexed by questions would get the
% part number instead of the question number.  That's fixed now.
%
%--------------------------------------------------------------------
%
% Version 2.204$\beta$, 2005/08/21:
%
% Bug fix: Hyperlinks didn't work on page numbers for horizontal
% grading tables indexed by page numbers.  They do now.
%
%--------------------------------------------------------------------
%
% Version 2.203$\beta$, 2005/08/20:
%
% Eliminated \do@int@lbl, and replaced it with labels for each
% question, part, subpart, and subsubpart the names of which
% tell you what they're labelling.
%
% That allowed us to rewrite the grade table stuff so that, for tables
% indexed by question numbers, the question numbers are inserted with a
% \ref, so that if \usepackage{hyperref} and pdflatex are used, those
% question numbers will be clickable links that take you to the relevant
% question.
%
% We also added a label for the first points to appear on each page, and
% rewrote the grade table stuff for tables indexed by page number so
% that the page numbers are inserted with a \pageref, so that if
% \usepackage{hyperref} and pdflatex are used, those page numbers will
% be clickable links that take you to the relevant page.
%
%--------------------------------------------------------------------
%
% Version 2.202$\beta$, 2005/08/10:
%
% Created \correctchoice as a synonym for \CorrectChoice
%
% Changed \CorrectChoiceDeclarations to \CorrectChoiceEmphasis,
% and created \correctchoiceemphasis as a synonym for that.
%
%--------------------------------------------------------------------
%
% Version 2.201$\beta$, 2005/08/09:
%
% We created a \CorrectChoice command for use in the choices and
% oneparchoices environments.
%
% When solutions are not being printed, \CorrectChoice is equivalent to
% \choice.
%
% When solutions *are* being printed, the choice that was created with
% \CorrectChoice (rather than with \choice) will be printed subject to
% the declarations in the argument of the
%
%   \CorrectChoiceDeclarations
%
% command.  The default is
%
%   \CorrectChoiceDeclarations{\bfseries}
%
% and so, when solutions are being printed, the correct choice is
% printed in boldface by default.  If, e.g., you give the command
%
%   \usepackage{color}
%
% after the \documentclass command and then give the command
%
%  \CorrectChoiceDeclarations{\color{red}}
%
% then the correct choice will be printed in red.  If, e.g., you give
% the command
%
%   \CorrectChoiceDeclarations{\color{red}\bfseries}
%
% then the correct choice will be printed in red and in boldface.
%
% Note added later: \CorrectChoiceDeclarations was changed
% to \CorrectChoiceEmphasis in version 2.202$\beta$.
%
%--------------------------------------------------------------------
%--------------------------------------------------------------------
%--------------------------------------------------------------------

\NeedsTeXFormat{LaTeX2e}

\ProvidesClass{exam}[\filedate\space Version \fileversion\space by
  Philip Hirschhorn]

\RequirePackage{ifthen}

\newif\ifprintanswers
\printanswersfalse
\DeclareOption{answers}{\printanswerstrue}
\DeclareOption{noanswers}{\printanswersfalse}

% The following keeps track of whether the user has requested that we
% add up the points on the exam.  We make the default false so that
% users who put other than numbers into the points argument of a
% question (or part, or subpart) won't get error messages.
% We use \if@printtotalpoints as a flag to signal that we are counting
% points, so that we will know to print the total on the screen (and
% in the log file).  We use this separate flag so that the user can
% use both \addpoints and \noaddpoints to count some points and not
% others, but still have the total printed when we finish the file no
% matter what the state of \if@addpoints.
\newif\if@addpoints
\newif\if@printtotalpoints
\def\addpoints{\global\@addpointstrue\global\@printtotalpointstrue}
\def\noaddpoints{\global\@addpointsfalse}
\@addpointsfalse
\@printtotalpointsfalse
\DeclareOption{addpoints}{\addpoints}


\DeclareOption*{%
  \PassOptionsToClass{\CurrentOption}{article}%
}
\ProcessOptions\relax
\LoadClass{article}




%                         *****************
%                         ** PAGE LAYOUT **
%                         *****************


% We set the parameters in terms of \paperwidth and \paperheight
% so that the options

% a4paper
% a5paper
% b5paper
% letterpaper
% legalpaper
% executivepaper
% landscape

% will all work:

\setlength{\textwidth}{\paperwidth}
\addtolength{\textwidth}{-2in}
\setlength{\oddsidemargin}{0pt}
\setlength{\evensidemargin}{0pt}

\setlength{\headheight}{15pt}
\setlength{\headsep}{15pt}
\setlength{\topmargin}{0in}
\addtolength{\topmargin}{-\headheight}
\addtolength{\topmargin}{-\headsep}
\setlength{\footskip}{29pt}
\setlength{\textheight}{\paperheight}
\addtolength{\textheight}{-2.2in}

\setlength{\marginparwidth}{.5in}
\setlength{\marginparsep}{5pt}

%--------------------------------------------------------------------

%                          ****************
%                          ** EXTRAWIDTH **
%                          ****************

\newlength\@extrawidth

% \@rightmargin is needed for \pointsinrightmargin and
% \pointsdroppedatright, so that we can right justify the points:
\newlength\@rightmargin
\setlength{\@rightmargin}{1in}

% We put the argument of \extrawidth into a length so that it will
% work correctly even if it's negative:

\def\extrawidth#1{%
  \@extrawidth=#1
  \advance \textwidth by \@extrawidth
  \divide\@extrawidth by 2
  \advance\oddsidemargin by -\@extrawidth
  \advance\evensidemargin by -\@extrawidth
  % Bug fix, 13 April 2004: 
  %\advance\@rightmargin by \@extrawidth
  \advance\@rightmargin by -\@extrawidth
}

%--------------------------------------------------------------------
%--------------------------------------------------------------------
%             Making room for large headers and footers

% The following are used to save the effect of any changes to 
% \topmargin and \textheight caused by \extraheadheight or
% \extrafootheight commands.  They hold the values currently in effect.
% We put them into lengths so that it will work correctly even if the
% argument is negative:

\newlength\@extrahead
\newlength\@extrafoot
\setlength{\@extrahead}{0in}
\setlength{\@extrafoot}{0in}

% The following are used to hold the requested values for extrahead and
% extrafoot, first page and all pages after the first, and then the
% similar things requested for the cover pages:
\newlength\run@exhd
\newlength\fp@exhd
\newlength\run@exft
\newlength\fp@exft
\newlength\covrun@exhd
\newlength\covfp@exhd
\newlength\covrun@exft
\newlength\covfp@exft

\setlength{\run@exhd}{0in}
\setlength{\fp@exhd}{0in}
\setlength{\run@exft}{0in}
\setlength{\fp@exft}{0in}
\setlength{\covrun@exhd}{0in}
\setlength{\covfp@exhd}{0in}
\setlength{\covrun@exft}{0in}
\setlength{\covfp@exft}{0in}

\newcommand*\adj@hdht@ftht{%
  \if@coverpages
    \ifnum\value{page}=1
      \@setheadheight{\covfp@exhd}%
      \@setfootheight{\covfp@exft}%
    \else
      \@setheadheight{\covrun@exhd}%
      \@setfootheight{\covrun@exft}%
    \fi
  \else
    \ifnum\value{page}=1
      \@setheadheight{\fp@exhd}%
      \@setfootheight{\fp@exft}%
    \else
      \@setheadheight{\run@exhd}%
      \@setfootheight{\run@exft}%
    \fi
  \fi
}

\newcommand*\extraheadheight{%
  \@ifnextchar[{\@xtrahd}{\@ytrahd}%
}

\def\@xtrahd[#1]#2{%
  \setlength{\fp@exhd}{#1}%
  \setlength{\run@exhd}{#2}%
  \adj@hdht@ftht
}

\def\@ytrahd#1{%
  \setlength{\fp@exhd}{#1}%
  \setlength{\run@exhd}{#1}%
  \adj@hdht@ftht
}

\newcommand*\extrafootheight{%
  \@ifnextchar[{\@xtraft}{\@ytraft}%
}

\def\@xtraft[#1]#2{%
  \setlength{\fp@exft}{#1}%
  \setlength{\run@exft}{#2}%
  \adj@hdht@ftht
}

\def\@ytraft#1{%
  \setlength{\fp@exft}{#1}%
  \setlength{\run@exft}{#1}%
  \adj@hdht@ftht
}

\newcommand*\coverextraheadheight{%
  \@ifnextchar[{\cov@xtrahd}{\cov@ytrahd}%
}

\def\cov@xtrahd[#1]#2{%
  \setlength{\covfp@exhd}{#1}%
  \setlength{\covrun@exhd}{#2}%
  \adj@hdht@ftht
}

\def\cov@ytrahd#1{%
  \setlength{\covfp@exhd}{#1}%
  \setlength{\covrun@exhd}{#1}%
  \adj@hdht@ftht
}

\newcommand*\coverextrafootheight{%
  \@ifnextchar[{\cov@xtraft}{\cov@ytraft}%
}

\def\cov@xtraft[#1]#2{%
  \setlength{\covfp@exft}{#1}%
  \setlength{\covrun@exft}{#2}%
  \adj@hdht@ftht
}

\def\cov@ytraft#1{%
  \setlength{\covfp@exft}{#1}%
  \setlength{\covrun@exft}{#1}%
  \adj@hdht@ftht
}

\def\@appendoutput#1{%
  \output=\expandafter{\the\output #1}%
}

\@appendoutput{\adj@hdht@ftht}

%--------------------------------------------------------------------
%                 \setheadheight and \setfootheight:

\def\@setheadheight#1{%
  \begingroup % Avoid trouble from using \@temp and \@spaces
    % Reset the effect of the most recent change:
    \global\advance\topmargin by -\@extrahead
    \global\advance\textheight by \@extrahead
    % Save the newly set value:
    \def\@temp{#1}
    \def\@spaces{ }
    \ifx\@temp\@empty
      \global\@extrahead=0in
    \else
      \ifx\@temp\@spaces
        \global\@extrahead=0in
      \else
        \global\@extrahead=#1
      \fi
    \fi
    % Set the new values:
    \global\advance\topmargin by \@extrahead
    \global\advance\textheight by -\@extrahead
    % Make it take effect RIGHT NOW!:
    % (The following stuff isn't necessary if \@setheadheight is
    % executed only in the preamble or as we return from the output
    % routine, but we're leaving it in so that this will still work if
    % we use this at some random point in the middle of composing a
    % page). 
    \global\@colht=\textheight
    \global\@colroom=\textheight
    \global\vsize=\textheight
    \global\pagegoal=\textheight
  \endgroup
}

\def\@setfootheight#1{%
  \begingroup % Avoid trouble from using \@temp and \@spaces
    % Reset the effect of the most recent change:
    \global\advance\textheight by \@extrafoot
    % Save the newly set value:
    \def\@temp{#1}
    \def\@spaces{ }
    \ifx\@temp\@empty
      \global\@extrafoot=0in
    \else
      \ifx\@temp\@spaces
        \global\@extrafoot=0in
      \else
        \global\@extrafoot=#1
      \fi
    \fi
    % Set the new values:
    \global\advance\textheight by -\@extrafoot
    % Make it take effect RIGHT NOW!:
    % (The following stuff isn't necessary if \@setfootheight is
    % executed only in the preamble or as we return from the output
    % routine, but we're leaving it in so that this will still work if
    % we use this at some random point in the middle of composing a
    % page). 
    \global\@colht=\textheight
    \global\@colroom=\textheight
    \global\vsize=\textheight
    \global\pagegoal=\textheight
  \endgroup
}




%---------------------------------------------------------------------
%
%                      *************************
%                      ** HEADERS AND FOOTERS **
%                      *************************
% 
% The pagestyles available are head, foot, headandfoot, and empty.
% \pagestyle{head} prints the head, and gives an empty foot.
% \pagestyle{foot} prints the foot, and gives an empty head.
% \pagestyle{headandfoot} prints both the head and the foot.
% \pagestyle{empty} gives an empty head and an empty foot.
% 

%                            Pagestyles:

\newcommand*\ps@head{%
  \@dohead
  \@nofoot
}

\newcommand*\ps@headandfoot{%
  \@dohead
  \@dofoot
}

\newcommand*\ps@foot{%
  \@nohead
  \@dofoot
}

% \ps@empty is already defined by article.cls, so we'll
% say \def instead of \newcommand*:
\def\ps@empty{%
  \@nohead
  \@nofoot
}

\newif\if@coverpages
\@coverpagesfalse

\newenvironment{coverpages}{%
    \ifnum \value{numquestions}>0
      \ClassError{exam}{%
        Coverpages cannot be used after questions have begun.\MessageBreak
      }{%
        All question, part, subpart, and subsubpart environments
        \MessageBreak
        must begin after the cover pages are complete.\MessageBreak
      }%
    \fi
    \@coverpagestrue
    \pagenumbering{roman}%
    \adj@hdht@ftht
  }{%
    \clearpage
    \pagenumbering{arabic}%
    \adj@hdht@ftht
}

\newcommand*\cover@question@error{%
  \ClassError{exam}{%
    No questions are allowed in the cover pages.\MessageBreak
  }{%
    All question, part, subpart, and subsubpart environments
    \MessageBreak
    must begin after the cover pages are complete.\MessageBreak
  }%
}

\newcommand*\@dohead{%
  \def\@oddhead{%
    \if@coverpages
      \ifnum\value{page}=1
        \cov@fullhead
      \else
        \covrun@fullhead
      \fi
    \else
      \ifnum\value{page}=1
        \@fullhead
      \else
        \run@fullhead
      \fi
    \fi
  }% @oddhead
  \let\@evenhead=\@oddhead
}

\newcommand*\@dofoot{%
  \def\@oddfoot{%
    \if@coverpages
      \ifnum\value{page}=1
        \cov@fullfoot
      \else
        \covrun@fullfoot
      \fi
    \else
      \ifnum\value{page}=1
        \@fullfoot
      \else
        \run@fullfoot
      \fi
    \fi
  }% @oddfoot
  \let\@evenfoot=\@oddfoot
}

\newcommand*\@nohead{%
  \def\@oddhead{}%
  \let\@evenhead=\@oddhead
}

\newcommand*\@nofoot{%
  \def\@oddfoot{}%
  \let\@evenfoot=\@oddfoot
}

%--------------------------------------------------------------------
%       \@fullhead, \run@fullhead, \@fullfoot, and \run@fullfoot:

\newcommand*\@fullhead{%
  \vbox to \headheight{%
    \vss
    \hbox to \textwidth{%
      \normalfont\rlap{\parbox[b]{\textwidth}{\raggedright\@lhead\strut}}%
        \hss\parbox[b]{\textwidth}{\centering\@chead\strut}\hss
        \llap{\parbox[b]{\textwidth}{\raggedleft\@rhead\strut}}%
    }% hbox
    \if@headrule
      \hrule
    \else
      % an invisible hrule, to keep positioning constant:
      \hrule width 0pt
    \fi
  }% vbox
}

\newcommand*\run@fullhead{%
  \vbox to \headheight{%
    \vss
    \hbox to \textwidth{%
      \normalfont\rlap{\parbox[b]{\textwidth}{\raggedright\run@lhead\strut}}%
        \hss\parbox[b]{\textwidth}{\centering\run@chead\strut}\hss
        \llap{\parbox[b]{\textwidth}{\raggedleft\run@rhead\strut}}%
    }% hbox
    \ifrun@headrule
      \hrule
    \else
      % an invisible hrule, to keep positioning constant:
      \hrule width 0pt
    \fi
  }% vbox
}

% We arrange it so that the very top of first line of text in the
% foot is at a fixed position on the page, whether or not there's
% a footrule:

\newcommand*\@fullfoot{%
  \vbox to 0pt{%
    \if@footrule
      \hrule
    \else
      % an invisible hrule, to keep positioning constant:
      \hrule width 0pt
    \fi
    \vskip 3pt
    \hbox to \textwidth{%
      \normalfont\rlap{\parbox[t]{\textwidth}{\raggedright\@lfoot}}%
        \hss\parbox[t]{\textwidth}{\centering\@cfoot}\hss
        \llap{\parbox[t]{\textwidth}{\raggedleft\@rfoot}}%
    }% hbox
    \vss
  }% vbox
}

\newcommand*\run@fullfoot{%
  \vbox to 0pt{%
    \ifrun@footrule
      \hrule
    \else
      % an invisible hrule, to keep positioning constant:
      \hrule width 0pt
    \fi
    \vskip 3pt
    \hbox to \textwidth{%
      \normalfont\rlap{\parbox[t]{\textwidth}{\raggedright\run@lfoot}}%
        \hss\parbox[t]{\textwidth}{\centering\run@cfoot}\hss
        \llap{\parbox[t]{\textwidth}{\raggedleft\run@rfoot}}%
    }% hbox
    \vss
  }% vbox
}

%--------------------------------------------------------------------
%       \cov@fullhead, \covrun@fullhead, \cov@fullfoot, and
%       \covrun@fullfoot: 

\newcommand*\cov@fullhead{%
  \vbox to \headheight{%
    \vss
    \hbox to \textwidth{%
      \normalfont\rlap{\parbox[b]{\textwidth}{\raggedright\cov@lhead\strut}}%
        \hss\parbox[b]{\textwidth}{\centering\cov@chead\strut}\hss
        \llap{\parbox[b]{\textwidth}{\raggedleft\cov@rhead\strut}}%
    }% hbox
    \ifcov@headrule
      \hrule
    \else
      % an invisible hrule, to keep positioning constant:
      \hrule width 0pt
    \fi
  }% vbox
}

\newcommand*\covrun@fullhead{%
  \vbox to \headheight{%
    \vss
    \hbox to \textwidth{%
      \normalfont\rlap{\parbox[b]{\textwidth}{\raggedright\covrun@lhead\strut}}%
        \hss\parbox[b]{\textwidth}{\centering\covrun@chead\strut}\hss
        \llap{\parbox[b]{\textwidth}{\raggedleft\covrun@rhead\strut}}%
    }% hbox
    \ifcovrun@headrule
      \hrule
    \else
      % an invisible hrule, to keep positioning constant:
      \hrule width 0pt
    \fi
  }% vbox
}

% We arrange it so that the very top of first line of text in the
% foot is at a fixed position on the page, whether or not there's
% a footrule:

\newcommand*\cov@fullfoot{%
  \vbox to 0pt{%
    \ifcov@footrule
      \hrule
    \else
      % an invisible hrule, to keep positioning constant:
      \hrule width 0pt
    \fi
    \vskip 3pt
    \hbox to \textwidth{%
      \normalfont\rlap{\parbox[t]{\textwidth}{\raggedright\cov@lfoot}}%
        \hss\parbox[t]{\textwidth}{\centering\cov@cfoot}\hss
        \llap{\parbox[t]{\textwidth}{\raggedleft\cov@rfoot}}%
    }% hbox
    \vss
  }% vbox
}

\newcommand*\covrun@fullfoot{%
  \vbox to 0pt{%
    \ifcovrun@footrule
      \hrule
    \else
      % an invisible hrule, to keep positioning constant:
      \hrule width 0pt
    \fi
    \vskip 3pt
    \hbox to \textwidth{%
      \normalfont\rlap{\parbox[t]{\textwidth}{\raggedright\covrun@lfoot}}%
        \hss\parbox[t]{\textwidth}{\centering\covrun@cfoot}\hss
        \llap{\parbox[t]{\textwidth}{\raggedleft\covrun@rfoot}}%
    }% hbox
    \vss
  }% vbox
}

%--------------------------------------------------------------------
%--------------------------------------------------------------------
%
%            ********************************************
%            ** COMMANDS TO DEFINE HEADERS AND FOOTERS **
%            ********************************************
%
% \lhead[#1]{#2} sets the first page left head to #1, and the
%   running left head to #2
% 
% \lhead{#1} sets both the first page left head and the running
%   left head to #1
% 
% \chead, \rhead, \lfoot, \cfoot, and \rfoot work similarly.
% 
% 
% \@lhead is the left head for Page 1
% \run@lhead is the running left head
% (i.e., for all pages other than the first)
% 
% \@chead is the center head for Page 1
% \run@chead is the running center head
% (i.e., for all pages other than the first)
% 
% etc.
% 
% Alternative commands are:
% \firstpageheader{LEFT}{CENTER}{RIGHT}
% \runningheader{LEFT}{CENTER}{RIGHT}
% or
% \header{LEFT}{CENTER}{RIGHT}
% which is equivalent to the two commands
%          \firstpageheader{LEFT}{CENTER}{RIGHT}
%          \runningheader{LEFT}{CENTER}{RIGHT}
% 
% Alternative commands are:
% \firstpagefooter{LEFT}{CENTER}{RIGHT}
% \runningfoother{LEFT}{CENTER}{RIGHT}
% or
% \footer{LEFT}{CENTER}{RIGHT}
% which is equivalent to the two commands
%          \firstpagefooter{LEFT}{CENTER}{RIGHT}
%          \runningfoother{LEFT}{CENTER}{RIGHT}

\def\firstpageheader#1#2#3{%
  \def\@lhead{#1}%
  \def\@chead{#2}%
  \def\@rhead{#3}%
}

\def\runningheader#1#2#3{%
  \def\run@lhead{#1}%
  \def\run@chead{#2}%
  \def\run@rhead{#3}%
}

\def\header#1#2#3{%
  \firstpageheader{#1}{#2}{#3}%
  \runningheader{#1}{#2}{#3}%
}

\def\firstpagefooter#1#2#3{%
  \def\@lfoot{#1}%
  \def\@cfoot{#2}%
  \def\@rfoot{#3}%
}

\def\runningfooter#1#2#3{%
  \def\run@lfoot{#1}%
  \def\run@cfoot{#2}%
  \def\run@rfoot{#3}%
}

\def\footer#1#2#3{%
  \firstpagefooter{#1}{#2}{#3}%
  \runningfooter{#1}{#2}{#3}%
}

\def\lhead{\@ifnextchar[{\@xlhead}{\@ylhead}}
\def\@xlhead[#1]#2{\def\@lhead{#1}\def\run@lhead{#2}}
\def\@ylhead#1{\def\run@lhead{#1}\def\@lhead{#1}}

\def\chead{\@ifnextchar[{\@xchead}{\@ychead}}
\def\@xchead[#1]#2{\def\@chead{#1}\def\run@chead{#2}}
\def\@ychead#1{\def\run@chead{#1}\def\@chead{#1}}

\def\rhead{\@ifnextchar[{\@xrhead}{\@yrhead}}
\def\@xrhead[#1]#2{\def\@rhead{#1}\def\run@rhead{#2}}
\def\@yrhead#1{\def\run@rhead{#1}\def\@rhead{#1}}

\def\lfoot{\@ifnextchar[{\@xlfoot}{\@ylfoot}}
\def\@xlfoot[#1]#2{\def\@lfoot{#1}\def\run@lfoot{#2}}
\def\@ylfoot#1{\def\run@lfoot{#1}\def\@lfoot{#1}}

\def\cfoot{\@ifnextchar[{\@xcfoot}{\@ycfoot}}
\def\@xcfoot[#1]#2{\def\@cfoot{#1}\def\run@cfoot{#2}}
\def\@ycfoot#1{\def\run@cfoot{#1}\def\@cfoot{#1}}

\def\rfoot{\@ifnextchar[{\@xrfoot}{\@yrfoot}}
\def\@xrfoot[#1]#2{\def\@rfoot{#1}\def\run@rfoot{#2}}
\def\@yrfoot#1{\def\run@rfoot{#1}\def\@rfoot{#1}}


%                    Initialize head and foot:

\pagestyle{headandfoot}

\lhead{}
\chead{}
\rhead{}
\lfoot{}
\cfoot[]{Page \thepage}
\rfoot{}

%--------------------------------------------------------------------
%                    Coverpage headers and footers
%
% \coverlhead[#1]{#2} sets the first cover page left head to #1, and the
%   running cover left head to #2
% 
% \coverlhead{#1} sets both the first cover page left head and the running
%   cover left head to #1
% 
% \coverchead, \coverrhead, \coverlfoot, \covercfoot, and \coverrfoot
% work similarly.
% 
% 
% \cov@lhead is the left head for Page 1
% \covrun@lhead is the running left head
% (i.e., for all pages other than the first)
% 
% \cov@chead is the center head for Page 1
% \covrun@chead is the running center head
% (i.e., for all pages other than the first)
% 
% etc.
% 
% Alternative commands are:
% \coverfirstpageheader{LEFT}{CENTER}{RIGHT}
% \coverrunningheader{LEFT}{CENTER}{RIGHT}
% or
% \coverheader{LEFT}{CENTER}{RIGHT}
% which is equivalent to the two commands
%          \coverfirstpageheader{LEFT}{CENTER}{RIGHT}
%          \coverrunningheader{LEFT}{CENTER}{RIGHT}
% 
% Alternative commands are:
% \coverfirstpagefooter{LEFT}{CENTER}{RIGHT}
% \coverrunningfoother{LEFT}{CENTER}{RIGHT}
% or
% \coverfooter{LEFT}{CENTER}{RIGHT}
% which is equivalent to the two commands
%          \coverfirstpagefooter{LEFT}{CENTER}{RIGHT}
%          \coverrunningfoother{LEFT}{CENTER}{RIGHT}

\def\coverfirstpageheader#1#2#3{%
  \def\cov@lhead{#1}%
  \def\cov@chead{#2}%
  \def\cov@rhead{#3}%
}

\def\coverrunningheader#1#2#3{%
  \def\covrun@lhead{#1}%
  \def\covrun@chead{#2}%
  \def\covrun@rhead{#3}%
}

\def\coverheader#1#2#3{%
  \coverfirstpageheader{#1}{#2}{#3}%
  \coverrunningheader{#1}{#2}{#3}%
}

\def\coverfirstpagefooter#1#2#3{%
  \def\cov@lfoot{#1}%
  \def\cov@cfoot{#2}%
  \def\cov@rfoot{#3}%
}

\def\coverrunningfooter#1#2#3{%
  \def\covrun@lfoot{#1}%
  \def\covrun@cfoot{#2}%
  \def\covrun@rfoot{#3}%
}

\def\coverfooter#1#2#3{%
  \coverfirstpagefooter{#1}{#2}{#3}%
  \coverrunningfooter{#1}{#2}{#3}%
}

\def\coverlhead{\@ifnextchar[{\cov@xlhead}{\cov@ylhead}}
\def\cov@xlhead[#1]#2{\def\cov@lhead{#1}\def\covrun@lhead{#2}}
\def\cov@ylhead#1{\def\covrun@lhead{#1}\def\cov@lhead{#1}}

\def\coverchead{\@ifnextchar[{\cov@xchead}{\cov@ychead}}
\def\cov@xchead[#1]#2{\def\cov@chead{#1}\def\covrun@chead{#2}}
\def\cov@ychead#1{\def\covrun@chead{#1}\def\cov@chead{#1}}

\def\coverrhead{\@ifnextchar[{\cov@xrhead}{\cov@yrhead}}
\def\cov@xrhead[#1]#2{\def\cov@rhead{#1}\def\covrun@rhead{#2}}
\def\cov@yrhead#1{\def\covrun@rhead{#1}\def\cov@rhead{#1}}

\def\coverlfoot{\@ifnextchar[{\cov@xlfoot}{\cov@ylfoot}}
\def\cov@xlfoot[#1]#2{\def\cov@lfoot{#1}\def\covrun@lfoot{#2}}
\def\cov@ylfoot#1{\def\covrun@lfoot{#1}\def\cov@lfoot{#1}}

\def\covercfoot{\@ifnextchar[{\cov@xcfoot}{\cov@ycfoot}}
\def\cov@xcfoot[#1]#2{\def\cov@cfoot{#1}\def\covrun@cfoot{#2}}
\def\cov@ycfoot#1{\def\covrun@cfoot{#1}\def\cov@cfoot{#1}}

\def\coverrfoot{\@ifnextchar[{\cov@xrfoot}{\cov@yrfoot}}
\def\cov@xrfoot[#1]#2{\def\cov@rfoot{#1}\def\covrun@rfoot{#2}}
\def\cov@yrfoot#1{\def\covrun@rfoot{#1}\def\cov@rfoot{#1}}


%                 Initialize coverpage head and foot:

\coverlhead{}
\coverchead{}
\coverrhead{}
\coverlfoot{}
\covercfoot{}
\coverrfoot{}




%--------------------------------------------------------------------
%--------------------------------------------------------------------

%                      Headrules and footrules:

\newif\if@headrule
\newif\ifrun@headrule

\def\firstpageheadrule{\@headruletrue}
\def\nofirstpageheadrule{\@headrulefalse}

\def\runningheadrule{\run@headruletrue}
\def\norunningheadrule{\run@headrulefalse}

\def\headrule{\@headruletrue\run@headruletrue}
\def\noheadrule{\@headrulefalse\run@headrulefalse}

\newif\if@footrule
\newif\ifrun@footrule

\def\firstpagefootrule{\@footruletrue}
\def\nofirstpagefootrule{\@footrulefalse}

\def\runningfootrule{\run@footruletrue}
\def\norunningfootrule{\run@footrulefalse}

\def\footrule{\@footruletrue\run@footruletrue}
\def\nofootrule{\@footrulefalse\run@footrulefalse}

%                             Initialize:

\noheadrule
\nofootrule

%                 Cover page headrules and footrules:

\newif\ifcov@headrule
\newif\ifcovrun@headrule

\def\coverfirstpageheadrule{\cov@headruletrue}
\def\nocoverfirstpageheadrule{\cov@headrulefalse}

\def\coverrunningheadrule{\covrun@headruletrue}
\def\nocoverrunningheadrule{\covrun@headrulefalse}

\def\coverheadrule{\cov@headruletrue\covrun@headruletrue}
\def\nocoverheadrule{\cov@headrulefalse\covrun@headrulefalse}

\newif\ifcov@footrule
\newif\ifcovrun@footrule

\def\coverfirstpagefootrule{\cov@footruletrue}
\def\nocoverfirstpagefootrule{\cov@footrulefalse}

\def\coverrunningfootrule{\covrun@footruletrue}
\def\nocoverrunningfootrule{\covrun@footrulefalse}

\def\coverfootrule{\cov@footruletrue\covrun@footruletrue}
\def\nocoverfootrule{\cov@footrulefalse\covrun@footrulefalse}

%                             Initialize:

\nocoverheadrule
\nocoverfootrule

%--------------------------------------------------------------------
%--------------------------------------------------------------------

%                \numpages, \iflastpage, and \oddeven
%     Also: \numpoints, \numquestions, \numparts, and \numsubparts
%                    Also also: \pointsofquestion

% Make the number of pages available as the macro \numpages,
% the number of points as \numpoints,
% the number of questions as \numquestions,
% the number of parts as \numparts, and
% the number of subparts as \numsubparts

% This was previously done with \pageref commands.  When I stopped
% using \pageref for this (in order to make this compatible with
% hyperref.sty), this stuff was created:

% \gdef commands for exam@lastpage, exam@numpoints,
% exam@numbonuspoints, exam@numquestions, exam@numparts,
% exam@numsubparts and exam@numsubsubparts are written to the .aux
% file via \AtEndDocument.

% \gdef commands for pointsofq@i, pointsofq@ii, etc. and
% bonuspointsofq@i, bonuspointsofq@ii, etc.  are written to the .aux
% file as each question is completed (see the definition of the
% questions environment).

% \gdef commands for pointsonpage@i, pointsonpage@ii, etc. and
% bonuspointsonpage@i, bonuspointsonpage@ii, etc. are written to the
% .aux file as we encounter points defined for a later page, and for
% the last such page with AtEndDocument.

\def\numpages{\@ifundefined{exam@lastpage}%
  {\mbox{\normalfont\bf ??}}%
  \exam@lastpage
}% numpages

\def\numpoints{\@ifundefined{exam@numpoints}%
  {\mbox{\normalfont\bf ??}}%
  \exam@numpoints
}% numpoints
\def\numbonuspoints{\@ifundefined{exam@numbonuspoints}%
  {\mbox{\normalfont\bf ??}}%
  \exam@numbonuspoints
}% numbonuspoints

\def\numquestions{\@ifundefined{exam@numquestions}%
  {\mbox{\normalfont\bf ??}}%
  \exam@numquestions
}% numquestions

\def\numparts{\@ifundefined{exam@numparts}%
  {\mbox{\normalfont\bf ??}}%
  \exam@numparts
}% numparts

\def\numsubparts{\@ifundefined{exam@numsubparts}%
  {\mbox{\normalfont\bf ??}}%
  \exam@numsubparts
}% numsubparts

\def\numsubsubparts{\@ifundefined{exam@numsubsubparts}%
  {\mbox{\normalfont\bf ??}}%
  \exam@numsubsubparts
}% numsubsubparts

\def\pointsofquestion#1{\@ifundefined{pointsofq@\romannumeral #1}%
  {\mbox{\normalfont\bf ??}}%
  {\csname pointsofq@\romannumeral #1\endcsname}%
}% pointsofquestion
\def\bonuspointsofquestion#1{\@ifundefined{bonuspointsofq@\romannumeral #1}%
  {\mbox{\normalfont\bf ??}}%
  {\csname bonuspointsofq@\romannumeral #1\endcsname}%
}% bonuspointsofquestion

\def\pointsonpage#1{\@ifundefined{pointsonpage@\romannumeral #1}%
  {\mbox{\normalfont\bf ??}}%
  {\csname pointsonpage@\romannumeral #1\endcsname}%
}% pointsonpage
\def\bonuspointsonpage#1{\@ifundefined{bonuspointsonpage@\romannumeral #1}%
  {\mbox{\normalfont\bf ??}}%
  {\csname bonuspointsonpage@\romannumeral #1\endcsname}%
}% bonuspointsonpage


\newif\if@pointschanged
\@pointschangedfalse

\newcommand*{\CheckIfChanged@hlf}[2]{%
  % The first argument is the name of a half counter.
  % The second argument expands to the name (without the escape
  % character, and not assumed to be defined) of the control sequence
  % holding the previous value.
  \@ifundefined{#2}%
    {\global\@pointschangedtrue}%
    {%
    % OK; it's defined.  See if it's changed:
    \begingroup
      \set@hlfcntr{tmp@hlfcntr}{\csname #2\endcsname}%
      \edef\othpt@check{\prtaux@hlfcntr{tmp@hlfcntr}}%
      \edef\pt@check{\prtaux@hlfcntr{#1}}%
      \ifx \pt@check \othpt@check
        % Do nothing
      \else
        \global\@pointschangedtrue
      \fi
    \endgroup
    }%
}% CheckIfChanged@hlf


%%%\let\@realenddocument=\enddocument
%%%\def\enddocument{\clearpage
%%%   \if@filesw 
%%%     {\advance\c@page-1 \immediate\write\@mainaux
%%%       {\string\newlabel{@lastpage}{{}{\arabic{page}}}}%
%%%     }
%%%   \fi
%%%   \@realenddocument
%%%}

\AtEndDocument{%
  \clearpage
  \if@filesw
    \advance\c@page-1
    \immediate\write\@mainaux
      {\string\gdef\string\exam@lastpage{\arabic{page}}}%
    \advance\c@page+1 % In case some other package looks at \c@page
    \immediate\write\@mainaux
        {\string\gdef\string\exam@numpoints{%
                            \prtaux@hlfcntr{numpoints}}}%
    % See if this has changed from the last run of LaTeX:
    \CheckIfChanged@hlf{numpoints}{exam@numpoints}%
    \immediate\write\@mainaux
        {\string\gdef\string\exam@numbonuspoints{%
                            \prtaux@hlfcntr{numbonuspoints}}}%
    % See if this has changed from the last run of LaTeX:
    \CheckIfChanged@hlf{numbonuspoints}{exam@numbonuspoints}%
    \immediate\write\@mainaux
      {\string\gdef\string\exam@numquestions{\thenumquestions}}%
    \immediate\write\@mainaux
      {\string\gdef\string\exam@numparts{\thenumparts}}%
    \immediate\write\@mainaux
      {\string\gdef\string\exam@numsubparts{\thenumsubparts}}%
    \immediate\write\@mainaux
      {\string\gdef\string\exam@numsubsubparts{\thenumsubsubparts}}%
    \ifnum \thepageof@pagepoints > 0\relax
      \immediate\write\@mainaux
          {\string\gdef\string\pointsonpage@\romannumeral
                          \csname c@pageof@pagepoints\endcsname
             {\prtaux@hlfcntr{@pagepoints}}}%
      % See if this has changed from the last run of LaTeX:
      \CheckIfChanged@hlf{@pagepoints}{pointsonpage@\romannumeral
                          \csname c@pageof@pagepoints\endcsname}%
    \fi
    \ifnum \thepageof@pagebonuspoints > 0\relax
      \immediate\write\@mainaux
          {\string\gdef\string\bonuspointsonpage@\romannumeral
                          \csname c@pageof@pagebonuspoints\endcsname
             {\prtaux@hlfcntr{@pagebonuspoints}}}%
      \CheckIfChanged@hlf{@pagebonuspoints}{bonuspointsonpage@\romannumeral
                          \csname c@pageof@pagebonuspoints\endcsname}%
    \fi
    \immediate\write\@mainaux
      {\string\gdef\string\lastpage@withpoints{\page@withpoints}}%
    % See if this has changed from the last run of LaTeX:
    \@ifundefined{lastpage@withpoints}%
      {\global\@pointschangedtrue}%
      {%
      % OK; it's defined.  See if it's changed:
      \begingroup
        \edef\othpt@check{\page@withpoints}%
        \edef\pt@check{\lastpage@withpoints}%
        \ifx \pt@check \othpt@check
          % Do nothing
        \else
          \global\@pointschangedtrue
        \fi
      \endgroup
      }%
    \immediate\write\@mainaux
      {\string\gdef\string\lastpage@withbonuspoints{\page@withbonuspoints}}%
    % See if this has changed from the last run of LaTeX:
    \@ifundefined{lastpage@withbonuspoints}%
      {\global\@pointschangedtrue}%
      {%
      % OK; it's defined.  See if it's changed:
      \begingroup
        \edef\othpt@check{\page@withbonuspoints}%
        \edef\pt@check{\lastpage@withbonuspoints}%
        \ifx \pt@check \othpt@check
          % Do nothing
        \else
          \global\@pointschangedtrue
        \fi
      \endgroup
      }%
  \fi
  % Echo numbers of questions, parts, and subparts:
  \typeout{This exam contains \thenumquestions\space questions
    with \thenumparts\space parts, \thenumsubparts\space subparts,
    and \thenumsubsubparts\space subsubparts.}
  % If counting points, echo total points:
  \if@printtotalpoints
    \begingroup
      \def\typ@expnd{%
        \thenumpoints
        \ifnumpoints@half
          \space and a half%
        \fi
      }
      \typeout{This exam has a total of \typ@expnd\space points.}
      \def\typ@expnd{%
        \thenumbonuspoints
        \ifnumbonuspoints@half
          \space and a half%
        \fi
      }
      \typeout{This exam has a total of \typ@expnd\space bonus points.}
    \endgroup
  \fi
  \if@pointschanged
    \ClassWarningNoLine{exam}{Point totals have changed.
               Rerun to get point totals right}%
  \fi
}% AtEndDocument


% We define \iflastpage so that it can safely be used
% in headers and footers:
\def\iflastpage#1#2{%
  \@ifundefined{exam@lastpage}{\def\@@lastpage{-1}}%
          {\edef\@@lastpage{\exam@lastpage}}%
  \ifnum\value{page}=\@@lastpage\relax
    #1%
  \else
    #2%
  \fi
}% iflastpage


% The macro \oddeven takes two arguments.  If the page number is odd,
% then you get the first argument; otherwise, you get the second
% argument.
\def\oddeven#1#2{%
  \ifodd\value{page}%
    #1
  \else
    #2
  \fi
}% oddeven



%--------------------------------------------------------------------
%--------------------------------------------------------------------
%                 \ifcontinuation, \ContinuedQuestion,
%                \ifincomplete, and \IncompleteQuestion

% The commands \ifcontinuation, \ContinuedQuestion, \ifincomplete, and
% \IncompleteQuestion assume that there is only one questions
% environment in the entire document.  (Actually, \ContinuedQuestion
% should work even if there are multiple questions environments, but
% none of the other three will work in general.)



% \PgInfo@write, \PgInfo and \PgInfo@get are our replacements
% for \label, \newlabel, and \pageref.  (We're avoiding using
% \label, \newlabel, and \pageref so that we will be compatible
% with hyperref.sty, which redefines those commands.)

% We use \PgInfo, \PgInfo@write, and \PgInfo@get to know on which page
% each question, part, subpart, subsubpart, and choice appears.

% We use \PgInfo@write to write \PgInfo commands to the .aux file.  The
% \PgInfo command takes two arguments: A question (or part, or subpart,
% or subsubpart) label, and the number of the page on which it appears.

% The label for a question is of the form `question@2' (if it's question
% 2).

% The label for a part is of the form `part@2@1' (if it's part a of
% question 2).

% The label for a subpart is of the form `subpart@2@1@3' (if it's
% subpart iii of part a of question 2).

% The label for a subsubpart is of the form `subsubpart@2@1@3@4' (if
% it's subsubpart $\delta$ of subpart iii of part a of question 2).

% Each question, part, subpart, subsubpart, and choice also gets a
% \PgInfo@write command using a label of the form question2@object3 (if
% it's the third object of the second question).

% The \PgInfo command defines a control sequence of the form `Pg@label'
% that expands to the page number for the corresponding question.  For
% example, \PgInfo{subsubpart@2@1@3@4}{7} defines 
%   \csname Pg@subsubpart@2@1@3@4\endcsname 
% to expand to 7.

% The \PgInfo@get{label} command returns the value of the macro Pg@label,
% but it *doesn't* check whether that macro is defined.  Thus, it's
% important to check that the macro Pg@label is defined before giving the
% command \PgInfo@get{label}.



% The token list to a \write command isn't expanded until
% it's shipped out.  Since the argument to PgInfo@write
% generally contains macros, we want to expand those macros
% now, rather than waiting until this is shipped out, at which
% point the macros may have different values.  Thus, we use
% \edef to force expansion of the argument, and we put
% a \noexpand in front of \thepage so that the \thepage
% will not be expanded now.  (This may not get shipped out
% until a later page, and so we want the \thepage to be expanded
% only when it's shipped out.)
% We use the \begingroup \endgroup pair so that our use
% of \reserved@a won't affect its use anywhere else.
\def\PgInfo@write#1{%
  \begingroup
    \edef\reserved@a{\write\@mainaux
      {\string\PgInfo{#1}{\noexpand\thepage}}}%
    \reserved@a
  \endgroup
}

%\PgInfo commands are written to the .aux file by the \PgInfo@write
%command; that's the only place that \PgInfo commands appear.
\def\PgInfo#1#2{\expandafter\gdef\csname Pg@#1\endcsname{#2}}

% Note: PgInfo@get assumes that the control sequence being
% constructed is already defined; you have to make sure of this
% *before* calling \Pginfo@get
\def\PgInfo@get#1{\csname Pg@#1\endcsname}

% \set@counter@to@pageof takes two arguments: The first is the name of a
% counter, and the second (expands to) the label of a question, part,
% subpart, subsubpart, or choice.  If that label exists, then we set the
% counter equal to the page on which the question (or part, etc.)
% appears.  If that label doesn't exist, we set the counter equal to -1.
% (No labels exist on the first run of LaTeX on the file, and if a new
% question (or part, etc.) was created by editing the file, then the
% label will not exist until the run of LaTeX after that.)
\def\set@counter@to@pageof#1#2{%
  \@ifundefined{Pg@#2}%
  {\setcounter{#1}{-1}}%
  {\setcounter{#1}{\csname Pg@#2\endcsname}}%
}


%--------------------------------------------------------------------

% \ifcontinuation#1#2 expands to #2 if either: (1) The current page is
% before the page containing question number 1, or (2) A question begins
% on this page before any part, subpart, subsubpart, or choice begins,
% or (3) The current page is later than a page with the \nomorequestions
% command.  Otherwise, it expands to #1.


\def\ifcontinuation#1#2{%
  % We need to first check whether we're on a page *before* the page on
  % which the first question appears.  If we don't yet know which page
  % has question number 1, then we must be doing an early run of LaTeX,
  % and we'll assume we're not a continuation.
  \expandafter\ifx\csname Pg@question@1\endcsname\relax
    % No page info yet; assume not a continuation
    #2%
  \else
    % Note: The ``\relax'' at the end of the following \ifnum
    % serves an entirely different purpose from the one at the
    % end of the above \expandafter\ifx.  That one (above)
    % is one of the things being compared, whereas the
    % one we're about to use is just to clearly mark the
    % end of the second number being compared by the \ifnum
    % (since it's conceivable that the ``#2'' would begin
    % with a digit).
    \ifnum \thepage < \csname Pg@question@1\endcsname\relax
      % We're before the page with question 1:
      #2%
    \else
      % The current page begins a new question if Contin@\thepage
      % has been defined as a macro that expands to \relax
      % (Note that this is different from if Contin@\thepage
      % has never been defined at all, in which case it will
      % be let equal to \relax (temporarily) by the \csname command.)
      \expandafter\ifx\csname Contin@\thepage\endcsname\ref@relax
        #2%
      \else
        % See if we're after a \nomorequestions command:
        \@ifundefined{Pg@@endquestions}%
        {#1}%
        {\ifnum \thepage > \PgInfo@get{@endquestions}\relax
          % We're after a \nomorequestions:
          #2
         \else
           % We actually are incomplete:
           #1
         \fi
        }%
      \fi
    \fi 
  \fi
}

\def\nomorequestions{
  \PgInfo@write{@endquestions}%
}

%--------------------------------------------------------------------
% \ContinuedQuestion is for use in headers and footers, where we can
% assume that \thepage is the number of the page on which we'll
% actually appear.

% \ContinuedQuestion expands to the number of the question that
% continues onto this page, or to -1 if this page begins with a new
% question.

% ACTUALLY: \ContinuedQuestion expands to a positive number if either
% (1) this page doesn't contain the beginning of any question, part,
% subpart, subsubpart, or choice, or (2) this page has a part, subpart,
% subsubpart, or choice that appears before any question.  That means
% that if the current page actually begins with space for a continuation
% of the previous question (but doesn't begin any part, subpart,
% subsubpart, or choice of that question) and then has a question, then
% we'll be asserting that this page begins with a new question, but the
% actual top of the page will begin with some blank space that's
% intended for the previous question.

% \ContinuedQuestion works by examining the value of the macro
% Contin@\thepage.  If this page starts with a question (i.e., if no
% question continues onto this page), then the macro Contin@\thepage
% will be defined, and will expand to `\relax' (and so an \ifx between
% \csname Contin@\thepage\endcsname and \ref@relax will be true).

% If Contin@\thepage is undefined, then when it is used in an \ifx
% command it will be temporarily set equal to \relax (which is
% *different* from being a macro that expands to \relax); in this case,
% there is no question, part, subpart, subsubpart, or choice that begins
% on this page, and so \ContinuedQuestion will be set equal to the last
% question that was begun on a page before this one.

% The last possibility is that this page begins with either a part,
% subpart, subsubpart, or choice.  In this case, Contin@\thepage is
% defined, and it expands to the number of the question that is
% continues onto this page.


\def\ref@relax{\relax}

\def\ContinuedQuestion{%
  \expandafter\ifx\csname Contin@\thepage\endcsname\relax
    % We get here if there's no question, part, subpart,
    % subsubpart, or choice on this page, and so Contin@\thepage has
    % never been defined at all.  In that case, this page
    % continues whichever question was last begun on or 
    % before this page.
    \find@latestques
    \thelatest@ques
  \else
    \expandafter\ifx\csname Contin@\thepage\endcsname\ref@relax
      % We get here if this page begins with a new question,
      % which is why Contin@\thepage has been defined to be
      % a macro that expands to \relax.
      % ACTUALLY: We get here if this page has a question that
      % appears before any part, subpart, subsubpart, or choice.  That
      % means that if the current page actually begins with space
      % for a continuation of the previous question but doesn't begin
      % any part, subpart, subsubpart, or choice of that question, then
      % we'll be asserting that this page begins with a new question,
      % but the actual top of the page will begin with some space
      % that's intended for the previous question.
      -1\relax
    \else
      % We get here if we didn't get anywhere above.  This happens
      % if Contin@\thepage has been defined to be a macro that expands
      % to something other than \relax, in which case it has been
      % defined to be a macro that expands to the number of the
      % question that continues onto this page.
      \csname Contin@\thepage\endcsname
    \fi
  \fi
}

%--------------------------------------------------------------------
% \find@latestques is for use in headers and footers, where we can
% assume that \thepage actually equals the page on which we'll appear.
% We find the last question that was started on or before the current
% page.

\newcounter{latest@ques}

\newcommand\find@latestques{%
  % \find@latestques is for use in headers and footers.
  % \find@latestques will set the counter latest@ques
  % to the number of the last question
  % that was begun on the exam from page 1 through the current
  % page.  This may well be the value of the question counter,
  % but it may be less than that if the page following this one
  % begins a new question and that question beginning was
  % typeset before the present page was shipped out.
  % Note: This macro is called both by \ContinuedQuestion and by
  % \find@quesend, which is why it has to find the last question
  % begun on or before the current page, rather than just before
  % the current page.
  \ifnum 1 > \arabic{question}\relax
    % Oops; probably because we're before the first question
    % Just set latest@ques to -1:
    \setcounter{latest@ques}{-1}%
  \else
    % If question latest@ques actually begins on this page (rather
    % than on the next page, but early enough on the next page
    % that the counter was advanced before we ran off into the
    % output routine to output the page and set the header and 
    % footer), then that's the correct question number.
    \expandafter\ifx\csname Pg@question@\arabic{question}\endcsname\relax
      % We don't know what page that question is on;
      % this must be an early run, before the aux file
      % is helpful.  Just set it equal to -1 and wait until the next
      % run to get it right.
      \setcounter{latest@ques}{-1}%
    \else
      % We now know that \PgInfo@get can tell us the page number
      % of \arabic{question} and of all earlier questions.
      % Set latest@ques equal to the current question number, and
      % then call \decr@latest@ques to recursively decrement
      % latest@ques as needed to find a question that begins on
      % or before the current page:
      \setcounter{latest@ques}{\arabic{question}}%
      \decr@latest@ques
    \fi
  \fi
}

\def\decr@latest@ques{%
  % If we get here, then we've already checked that the reference
  % Pg@question@\thelatest@ques is defined at least for a value of
  % \thelatest@ques greater than or equal to it's present value,
  % so we assume it's defined for all lesser values as well:
  \ifnum \thepage < \PgInfo@get{question@\thelatest@ques}\relax
    % Nope; latest@ques starts on a later page
    % Decrement latest@ques and see if that one's right:
    \addtocounter{latest@ques}{-1}%
    \ifnum \thelatest@ques < 1\relax
      \setcounter{latest@ques}{-1}%
      \let\next@dlq=\relax
    \else
      \let\next@dlq=\decr@latest@ques
    \fi
  \else
    % latest@ques starts on this page or earlier, so
    % that's the correct question number!  Exit:
    \let\next@dlq=\relax
  \fi
  \next@dlq
}

%--------------------------------------------------------------------
%--------------------------------------------------------------------
%--------------------------------------------------------------------
\newcounter{ques@end}
\newcounter{last@object}

\def\find@quesend{%
  % We find the last question started on or before the current page
  % and then find the page containing the last part (or subpart, or
  % subsubpart, or choice) of that question, and set the counter
  % ques@end to that page number.
  % Set latest@ques equal to the correct question number:
  \find@latestques
  \ifnum \value{latest@ques} < 0\relax
    % This must be an early run of LaTeX, before we have
    % \PgInfo commands in the .aux file:
    \setcounter{ques@end}{-1}%
  \else
    % We now know that this question has at least one object (since
    % we know that latest@ques isn't negative).
    % We'll find its highest numbered object by setting last@object
    % equal to 2 and then calling \find@lastobject to recursively
    % test whether that object number exists and, if so, incrementing
    % last@object to test for a higher numbered one:
    \setcounter{last@object}{2}%
    \find@lastobject
    \setcounter{ques@end}{\PgInfo@get{question\thelatest@ques
               @object\thelast@object}}%
  \fi
}% find@quesend

\def\find@lastobject{%
  % We check whether this question has an object numbered last@object
  % and recursively increment last@object to find the highest
  % numbered value for which the object exists:
  \@ifundefined{Pg@question\thelatest@ques @object\thelast@object}%
    {\addtocounter{last@object}{-1}%
      \let\nextfind@lastobject=\relax
    }%
    {\addtocounter{last@object}{1}%
      \let\nextfind@lastobject=\find@lastobject
    }%
  \nextfind@lastobject
}% find@lastobject



%--------------------------------------------------------------------
%--------------------------------------------------------------------
%--------------------------------------------------------------------

\newcounter{incmp@ques}

\def\IncompleteQuestion{%
  \Find@Incmp@ques
  \theincmp@ques
}

\def\Find@Incmp@ques{%
  \iflastpage{\setcounter{incmp@ques}{-1}}{\chk@incomp}%
}
\newcounter{next@ques}
\newcounter{nextq@page}
\def\chk@incomp{%
  \find@quesend
  \ifnum \theques@end > \thepage\relax
    % This question has a part (or sub...) starting on a later page
    \setcounter{incmp@ques}{\value{latest@ques}}%
  \else
    \setcounter{next@ques}{\thelatest@ques}%
    \addtocounter{next@ques}{1}%
    \expandafter\ifx\csname Pg@question@\thenext@ques \endcsname\relax
      % This isn't the last page but there is no next question:
      \setcounter{incmp@ques}{\thelatest@ques}%
    \else
      % This isn't the last page and there is a next question:
      \setcounter{nextq@page}{\PgInfo@get{question@\thenext@ques}}%
      \addtocounter{nextq@page}{-1}%
      \ifnum \thenextq@page > \thepage\relax
        \setcounter{incmp@ques}{\thelatest@ques}%
      \else
        \setcounter{incmp@ques}{-1}%
      \fi
    \fi
  \fi
}

\def\ifincomplete#1#2{%
  \def\incomp@first{#1}%
  \def\incomp@second{#2}%
  \Find@Incmp@ques
  \ifnum \theincmp@ques < 0\relax
    \incomp@second
  \else
        \@ifundefined{Pg@@endquestions}%
        {\incomp@first}%
        {\ifnum \thepage < \PgInfo@get{@endquestions}%
           \incomp@first
         \else
           \incomp@second
         \fi
        }%
  \fi
}

%--------------------------------------------------------------------
% These are the commands for dealing with hlfcntr's, i.e., the things
% used to count points.
%
% A point value is a nonnegative integer with an optional half integer.
% A hlfcntr consists of a regular counter together with an \if: If the
% regular counter is called ``counter'', then the \if is called
% ``\ifcounter@half''; it's set true by ``\counter@halftrue'' and set
% false by ``\counter@halffalse''.
%
% The commands:
%
% \new@hlfcntr{countername}
% \set@hlfcntr{countername}{value}
% \copy@hlfcntr{tocounter}{fromcounter}
% \addto@hlfcntr{countername}{value}
% \add@hlfcntrtohlfcntr{getsaddedto}{whatsadded}
% \ifhlfcntr@pos{countername}
% \prtaux@hlfcntr{countername}
% \prt@hlfcntr{countername}
%
% ``value'' can be either a (nonnegative) integer, an integer followed by
% ``\half'', or just plain ``\half''.  (Actually, ``value'' can be empty
% (although the braces must be present), in which case it's interpreted
% as ``0''.)
%
% Examples of valid values:
%   0
%   0\half
%   1
%   1\half
%   2
%   2\half
% etc.

% Note on using ``\global'': LaTeX's \setcounter and \addtocounter
% commands are already \global (i.e., you don't have to say
% ``\global''), but \somethingtrue and \somethingfalse (used to set
% \ifsomething) aren't.  Thus, we need to say ``\global'' when setting
% these things.

% To create a hlfcntr:
\newcommand*\new@hlfcntr[1]{%
  \newcounter{#1}%
  \expandafter\newif\csname if#1@half\endcsname
}% new@hlfcntr


% A scratch hlfcntr:
\new@hlfcntr{tmp@hlfcntr}

\newcommand*\horiz@half{$\frac{1}{2}$}
\newcommand*\slanted@half{%
  $\raise0.6ex\hbox{$\scriptstyle 1$}\kern -.2em/\kern -.2em
     \raise-0.5ex\hbox{$\scriptstyle 2$}$%
}% slanted@half
\newcommand*\useslantedhalf{\global\let\half\slanted@half}
\newcommand*\usehorizontalhalf{\global\let\half\horiz@half}
\newcommand*\half{\slanted@half}


\newcommand*\set@hlfcntr[2]{%
  \begingroup
    \global\csname #1@halffalse\endcsname
    % If there as a `\half' present, it will be executed
    % right after the assignment of the digit part of #2
    % to the counter #1.
    \def\half{%
      \global\csname #1@halftrue\endcsname
    }%
    % We insert a `0' in case there are no digits present:
    % We avoid using \setcounter, because calc.sty redefines
    % \setcounter in a way that conflicts with the \half trick
    % we're using:
    %    \setcounter{#1}{0#2}\relax
    \global\csname c@#1\endcsname 0#2\relax
  \endgroup
}% set@hlfcntr

\newcommand*\copy@hlfcntr[2]{%
  % We set #1 to the value of #2
  \setcounter{#1}{\value{#2}}%
  \csname if#2@half\endcsname
    \global\csname #1@halftrue\endcsname
  \else
    \global\csname #1@halffalse\endcsname
  \fi
}% copy@hlfcntr

\newcommand*\addto@hlfcntr[2]{%
  % We add the valueandhalf #2 to hlfcntr #1
  \begingroup
    \def\half{\add@half{#1}}%
    % We insert a `0' in case there are no digits present:
    % We avoid using \addtocounter, because calc.sty redefines
    % \addtocounter in a way that conflicts with the \half trick
    % we're using:
    %    \addtocounter{#1}{0#2}\relax
    \global\advance\csname c@#1\endcsname 0#2\relax
  \endgroup
}% addto@hlfcntr

\newcommand*\add@hlfcntrtohlfcntr[2]{%
  % We add the hlfcntr #2 to the hlfcntr #1
  \addtocounter{#1}{\value{#2}}%
  \csname if#2@half\endcsname
    \add@half{#1}%
  \fi
}% add@hlfcntrtohlfcntr

\newcommand*\add@half[1]{%
  % We add one half to hlfcntr #1:
  \csname if#1@half\endcsname
    \addtocounter{#1}{1}%
    \global\csname #1@halffalse\endcsname
  \else
    \global\csname #1@halftrue\endcsname
  \fi
}% add@half

\newcounter{ifpos@cntr}
\def\ifhlfcntr@pos#1{%
  % The argument must be a hlfcntr (which, of course,
  % can never be negative); we'll be true if and only if
  % that halfcntr is positive:
  \setcounter{ifpos@cntr}{\value{#1}}%
  \csname if#1@half\endcsname
    \addtocounter{ifpos@cntr}{1}%
  \fi
  \ifnum \value{ifpos@cntr} > 0
}% ifhlfnctr@pos

% \prtaux@hlfcntr is used inside the argument of a \write command for
% writing to the .aux file:
\newcommand*\prtaux@hlfcntr[1]{%
  % We don't want a \relax after the 0 in the following
  % line, because it would sometimes appear in the aux file:
  \ifnum \value{#1} = 0 
    % We have to make the following a macro, because if we
    % don't do this part, the \fi will cause confusion, since
    % there's no \if visible until the \csname is expanded:
    \prtaux@halforzero{#1}%
  \else
    \arabic{#1}%
    % We have to make the following a macro, because if we
    % don't do this part, the \fi will cause confusion, since
    % there's no \if visible until the \csname is expanded:
    \prtaux@halforblank{#1}%
  \fi
}% prtaux@hlfcntr
\newcommand*\prtaux@halforzero[1]{%
  \csname if#1@half\endcsname
    \string\half
  \else
    0%
  \fi
}% prtaux@hlforzero
\newcommand*\prtaux@halforblank[1]{%
  \csname if#1@half\endcsname
    \string\half
  \fi
}% prtaux@halforblank

\newcommand*\prt@hlfcntr[1]{%
  % We don't want a \relax after the 0 in the following
  % line, because it would sometimes appear in the aux file:
  \ifnum \value{#1} = 0 
    % We have to make the following a macro, because if we
    % don't do this part, the \fi will cause confusion, since
    % there's no \if visible until the \csname is expanded:
    \prt@halforzero{#1}%
  \else
    \arabic{#1}%
    % We have to make the following a macro, because if we
    % don't do this part, the \fi will cause confusion, since
    % there's no \if visible until the \csname is expanded:
    \prt@halforblank{#1}%
  \fi
}% prt@hlfcntr
\newcommand*\prt@halforzero[1]{%
  \csname if#1@half\endcsname
    \half
  \else
    0%
  \fi
}% prt@hlforzero
\newcommand*\prt@halforblank[1]{%
  \csname if#1@half\endcsname
    \half
  \fi
}% prt@halforblank

% End of the commands for dealing with hlfcntr's

%--------------------------------------------------------------------
%---------------------------------------------------------------------
%
%                    ***************************
%                    ** QUESTION ENVIRONMENTS **
%                    ***************************
%
%
%

% We define the command \part only inside of a parts environment, so
% that we don't interfere with the meaning of the standard article
% documentclass command \part if that is used inside of a questions
% environment.  The commands \question, \subpart, and \subsubpart are
% defined everywhere inside of a questions environment.  If the user
% accidentally gives a \subpart command outside of a subparts
% environment, then an error will be created.




% We use the counter name `partno' for the parts environment so that
% we will not interfere with the counter `part' used by the article
% document class.

\newcounter{question}
\newcounter{partno}
\newcounter{subpart}
\newcounter{subsubpart}
\newcounter{choice}
\new@hlfcntr{numpoints}
\set@hlfcntr{numpoints}{0}
\new@hlfcntr{numbonuspoints}
\set@hlfcntr{numbonuspoints}{0}
\new@hlfcntr{pointsof@thisquestion}
\set@hlfcntr{pointsof@thisquestion}{0}
\new@hlfcntr{bonuspointsof@thisquestion}
\set@hlfcntr{bonuspointsof@thisquestion}{0}
\newcounter{numquestions}
\newcounter{numparts}
\newcounter{numsubparts}
\newcounter{numsubsubparts}
\newcounter{Curr@Page}

% @pagepoints accumulates the points on a single page:
\new@hlfcntr{@pagepoints}
\set@hlfcntr{@pagepoints}{0}
\new@hlfcntr{@pagebonuspoints}
\set@hlfcntr{@pagebonuspoints}{0}
\newcounter{pageof@pagepoints}
\setcounter{pageof@pagepoints}{0}
\newcounter{pageof@pagebonuspoints}
\setcounter{pageof@pagebonuspoints}{0}

% latest@points is a holding area for points until we know
% whether they'll land on the same page as the points
% currently counted in @pagepoints:
\new@hlfcntr{latest@points}
\set@hlfcntr{latest@points}{0}
\new@hlfcntr{latest@bonuspoints}
\set@hlfcntr{latest@bonuspoints}{0}

% Whenever we meet a new page on which points are defined, we'll
% redefine \page@withpoints to expand to that page.  At the end of the
% document, it will hold the last page that has points, and we'll write
% a \gdef\lastpage@withpoints command to the .aux file.
% We initialize \page@withpoints here:
\def\page@withpoints{0}%
\def\page@withbonuspoints{0}%

% \pageinfo@commands is used by each question, part, subpart, and
% subsubpart to insert into everypar the \PgInfo@write command to put
% its page number into the .aux file, the \PgInfo@get command to read
% the page number into the counter Curr@Page, and to test and set
% \Contin@\theCurr@Page.  \temp@toks is used by part, subpart, and
% subsubpart to append all that to \pageinfo@commands, rather than
% deleting whatever may have been put into \pageinfo@commands by the
% current question and/or part and/or subpart.
\newtoks\pageinfo@commands
\newtoks\temp@toks

% \pagepoint@commands holds the commands to manage the counting of the
% number of points defined on each page.
\newtoks\pagepoint@commands

% \point@toks holds the commands to print the points at the proper
% location on the page (except that it's not used by the \qformat
% option).
\newtoks\point@toks

% We'll use \greeknum to number subsubparts
\def\greeknum#1{\expandafter\lc@greek\csname c@#1\endcsname}
\def\lc@greek#1{%
  \ifcase #1\or $\alpha$\or $\beta$\or $\gamma$\or $\delta$\or
  $\epsilon$\or $\zeta$\or $\eta$\or $\theta$\or $\iota$\or
  $\kappa$\or $\lambda$\or $\mu$\or $\nu$\or $\xi$\or o\or $\pi$\or
  $\rho$\or $\sigma$\or $\tau$\or $\upsilon$\or $\phi$\or $\chi$\or
  $\psi$\or $\omega$\else \@ctrerr
  \fi
}% lc@greek


% The following macros are a variation on a trick from Victor
% Eijkhout's ``TeX by Topic'', page 142:
% Both \prepend@toklist and \append@toklist take two arguments,
% both of which should be token lists.
% \prepend@toklist prepends #2 to #1
% \append@toklist appends #2 to #1

\def\prepend@toklist#1#2{%
  \edef\do@it{\noexpand#1={\the#2\the#1}}%
  \do@it
}% prepend@toklist

\def\append@toklist#1#2{%
  \edef\do@it{\noexpand#1={\the#1\the#2}}%
  \do@it
}% append@toklist


% The command \qformat is provided for the user who wants to
% design a nonstandard question line.  If this command is used,
% then the usual line containing the question number and the beginning
% of the question will be replaced by the line specified by the
% \qformat command, and the question will begin on the following
% line.
% Within the argument of the \qformat command:
% \thequestion will be replaced by the question number, and
% \thepoints will be replaced by ``\@points \@pointname'' if the
% number of points has been specified for this question, and otherwise
% it inserts nothing at all.  (The conditional @placepoints is used to
% determine if there were points specified for this question.)
% The argument to the \qformat command *must* contain some
% stretch, i.e., at least one \hfil or \dotfill or ...
\newif\if@qformat
\@qformatfalse

\def\qformat#1{%
  \global\@qformattrue
  \gdef\@questionformat{#1}%
}% qformat

\newcommand\noqformat{%
  \global\@qformatfalse
}% noqformat

% \thepoints is for use in either a \qformat command
% or a \pointformat command.  It needs to have the
% \if@placepoints so that if it's used in a \qformat command
% it won't print anything if there are no points:
%\newcommand\thepoints{%
%  \if@placepoints
%    \@points \@pointname
%  \fi
%}
\newcommand\thepoints{%
  \if@placepoints
    \if@bonus
      \@points \@bonuspointname
    \else
      \@points \@pointname
    \fi
  \fi
}% thepoints

% \themarginpoints is for use only in a \pointformat command,
% and so it doesn't need the \if@placepoints bit in \thepoints:
%\newcommand\themarginpoints{%
%  \@points \@marginpointname
%}% themarginpoints
\newcommand\themarginpoints{%
  \if@bonus
    \@points \@marginbonuspointname
  \else
    \@points \@marginpointname
  \fi
}% themarginpoints

% We define the \subpart and \subsubpart commands when we enter a
% questions environment (rather than waiting until we enter a subparts
% of subsubparts environment) so that we can signal an error if a
% \subpart or \subsubpart command appears outside of the corresponding
% environment.  (We don't do this for the \part command so that the user
% can use the standard sectioning \part command outside of a parts
% environment.)

% The counter ques@object will count the items in each question, where
% an item is defined as either the question itself, or a part, or a
% subpart, or a subsubpart, or a choice.  This will be used by
% \find@quesend to find the last page occupied by the last question
% begun on or before the current page:
\newcounter{ques@object}

% if@bonus will be true when we're doing a bonusquestion or bonuspart
% or etc., and it will also be used also to distinguish between
% \gradetable and \bonusgradetable (and between \pointtable and
% \bonuspointtable, etc.):
\newif\if@bonus
\@bonusfalse

% The following are for advanced users who want to customize the list
% parameters (\topsep, \partopsep, \itemsep, \parsep, etc.) for the
% lists that these environments create.  They are all defined to be
% empty, but the user can change them using \renewcommand.
\newcommand\questionshook{}
\newcommand\partshook{}
\newcommand\subpartshook{}
\newcommand\subsubpartshook{}
\newcommand\choiceshook{}


\newenvironment{questions}{%
  % \@queslevel is used for two purposes:
  % (1) We check that every \question, \part, \subpart, and 
  % \subsubpart command appears inside the appropriate environment,
  % and generate an error if one appears in the wrong place.
  % (2) If a \qformat is being used and if \@queslevel tells us
  % that we're currently processing a question, then we set
  % \global \point@toks={} to avoid setting the points for a 
  % question other than via the qformat command.
  \def\@queslevel{question}%
  \def\titledquestion##1{%
    \@bonusfalse
    \def\thequestiontitle{##1}%
    \process@question
  }%
  \def\bonustitledquestion##1{%
    \@bonustrue
    \def\thequestiontitle{##1}%
    \process@question
  }%
  \def\question{%
    \@bonusfalse
    \def\thequestiontitle{\csname p@question\endcsname
                          \csname thequestion\endcsname}%
    \process@question
  }%
  \def\bonusquestion{%
    \@bonustrue
    \def\thequestiontitle{\csname p@question\endcsname
                          \csname thequestion\endcsname}%
    \process@question
  }%
  \def\process@question{%
    \if@coverpages
      \cover@question@error
    \fi
    \@checkqueslevel{question}%
    \addtocounter{numquestions}{1}%
    % Write the sum of points of the previous question (if any)
    % to the .aux file.  (At this point, the question counter
    % has not yet been incremented, so \arabic{question} has the
    % number of the question that was just completed.)
    \if@filesw
      \ifnum \arabic{question} > 0\relax
        % First do regular points:
        \immediate\write\@mainaux
          {\string\gdef\string\pointsofq@
            \romannumeral \csname c@question\endcsname
              {\prtaux@hlfcntr{pointsof@thisquestion}}}%
        % See if this has changed from the last run of LaTeX:
        \CheckIfChanged@hlf{pointsof@thisquestion}{pointsofq@\romannumeral
                            \csname c@question\endcsname}%
        % Now do bonus points:
        \immediate\write\@mainaux
          {\string\gdef\string\bonuspointsofq@
            \romannumeral \csname c@question\endcsname
              {\prtaux@hlfcntr{bonuspointsof@thisquestion}}}%
        % See if this has changed from the last run of LaTeX:
        \CheckIfChanged@hlf{bonuspointsof@thisquestion}%
                           {bonuspointsofq@\romannumeral
                             \csname c@question\endcsname}%
      \fi
    \fi
    \set@hlfcntr{pointsof@thisquestion}{0}%
    \set@hlfcntr{bonuspointsof@thisquestion}{0}%
    % If there was a question with points immediately preceding
    % this question (i.e., there were no parts in the previous
    % question), then @placepoints will still be true, and we need to
    % cancel it.  (We used to do this inside of the \thepoints macro,
    % but that allowed for an error if the user specified points for a
    % question but had a \qformat that didn't mention \thepoints.)  We
    % also set @placepoints to be false when entering a parts
    % environment. 
    \global \@placepointsfalse
    % point@toks will normally be empty at this point, but it might be
    % nonempty if there were points somewhere in the previous question
    % that never made it onto the page because we never entered
    % horizontal mode (perhaps because the user was weird and let the
    % text of a question (or part, etc.) consist entirely of an
    % enumerate environment, or description environment, or etc.).
    \global \point@toks={}%
    % Important: Don't leave any blank lines inside of
    % \pageinfo@commands!!  This token list will be dumped into
    % horizontal mode by \everypar, and so any blank lines will
    % cause paragraph breaks. 
    \pageinfo@commands={%
      \edef\@queslabel{question@\arabic{question}}%
      \PgInfo@write{\@queslabel}%
      \setcounter{ques@object}{1}%
      \edef\q@object@label{%
            question\arabic{question}@object\arabic{ques@object}}%
      \PgInfo@write{\q@object@label}%
      % In addition to the \PgInfo@write we use an actual \label
      % command.  We do this in order to make the question numbers in
      % the grade tables into \ref's, so that if the user says
      % \usepackage{hyperref}, those question numbers will be clickable.
      % 
      % A further purpose of these labels (which we actually do for all
      % questions, parts, subparts, and subsubparts) is that if a
      % question (or part, etc.) is, e.g., moved from one page to
      % another, LaTeX will notice this and warn the user that LaTeX
      % must be run one more time to be sure everything is correct.
      % 
      % We need to do this even though we've already included code to
      % check when point totals change because questions (and parts,
      % etc.) know what page they're on from reading the info written to
      % the .aux file on the previous run.  Thus, if a question (or
      % part, etc.) is moved to a different page, then the pointsonpage
      % totals won't notice until the *second* subsequent run of LaTeX,
      % and so there'll be no warning to the user on the *first* run.
      % Including these labels gives the user a warning on that first
      % run.
      %
      % Further futzing required: Since this is being put into the
      % token list \pageinfo@commands, the contents of which won't
      % actually be  executed until we enter horizontal mode (which
      % may well be in the first part of a parts environment), we need
      % to make sure that \@currentlabel is the number of the
      % question:
      \begingroup % to confine the change to \@currentlabel
%        \def\@currentlabel{\csname p@question\endcsname
%                           \csname thequestion\endcsname}%
        \def\@currentlabel{\thequestiontitle}%
        \label{\@queslabel}%
      \endgroup
      \set@counter@to@pageof{Curr@Page}{\@queslabel}%
      \expandafter\ifx\csname Contin@\theCurr@Page\endcsname\relax
        % We're the first \question, \part, \subpart, \subsubpart,
        % or choice on this page:
        \global\expandafter\edef
               \csname Contin@\theCurr@Page\endcsname{\relax}%
      \fi
      \the\pagepoint@commands
      \global \pageinfo@commands={}%
    }% pageinfo@commands
    \ifhmode
      % Remove any skips at the end of the previous paragraph
      % that might cause a blank line, and then end that paragraph:
      \unskip\unskip \par
    \fi
    \@doitem
  }% process@question
  \def\subpart{%
    \@bonusfalse
    \process@subpart
  }%
  \def\bonussubpart{%
    \@bonustrue
    \process@subpart
  }%
  \def\process@subpart{%
    \@bonusfalse
    \if@coverpages
      \cover@question@error
    \fi
    \@checkqueslevel{subpart}%
    \addtocounter{numsubparts}{1}%
    % Important: Don't leave any blank lines inside of
    % \pageinfo@commands!!  This token list will be dumped into
    % horizontal mode by \everypar, and so any blank lines will
    % cause paragraph breaks. 
    \temp@toks={%
      \edef\@subpartlabel{subpart@\arabic{question}%
        @\arabic{partno}@\arabic{subpart}}%
      \PgInfo@write{\@subpartlabel}%
      \addtocounter{ques@object}{1}%
      \edef\q@object@label{%
            question\arabic{question}@object\arabic{ques@object}}%
      \PgInfo@write{\q@object@label}%
      % In addition to the \PgInfo@write we use an actual \label
      % command.  We do this in order to make the question numbers in
      % the grade tables into \ref's, so that if the user says
      % \usepackage{hyperref}, those question numbers will be clickable.
      % 
      % A further purpose of these labels (which we actually do for all
      % questions, parts, subparts, and subsubparts) is that if a
      % question (or part, etc.) is, e.g., moved from one page to
      % another, LaTeX will notice this and warn the user that LaTeX
      % must be run one more time to be sure everything is correct.
      % 
      % We need to do this even though we've already included code to
      % check when point totals change because questions (and parts,
      % etc.) know what page they're on from reading the info written to
      % the .aux file on the previous run.  Thus, if a question (or
      % part, etc.) is moved to a different page, then the pointsonpage
      % totals won't notice until the *second* subsequent run of LaTeX,
      % and so there'll be no warning to the user on the *first* run.
      % Including these labels gives the user a warning on that first
      % run.
      \label{\@subpartlabel}%
      \set@counter@to@pageof{Curr@Page}{\@subpartlabel}%
      \expandafter\ifx\csname Contin@\theCurr@Page\endcsname\relax
        % We're the first \question, \part, \subpart, \subsubpart,
        % or choice on this page:
        \global\expandafter\edef\csname
                       Contin@\theCurr@Page\endcsname{\arabic{question}}%
      \fi
      \the\pagepoint@commands
      \global \pageinfo@commands={}%
    }% temp@toks
    \append@toklist \pageinfo@commands \temp@toks
    \ifhmode
      % Remove any skips at the end of the previous paragraph
      % that might cause a blank line, and then end that paragraph:
      \unskip\unskip \par
    \fi
    \@doitem
  }% process@subpart
  \def\subsubpart{%
    \@bonusfalse
    \process@subsubpart
  }%
  \def\bonussubsubpart{%
    \@bonustrue
    \process@subsubpart
  }%
  \def\process@subsubpart{%
    \@bonusfalse
    \if@coverpages
      \cover@question@error
    \fi
    \@checkqueslevel{subsubpart}%
    \addtocounter{numsubsubparts}{1}%
    % Important: Don't leave any blank lines inside of
    % \pageinfo@commands!!  This token list will be dumped into
    % horizontal mode by \everypar, and so any blank lines will
    % cause paragraph breaks. 
    \temp@toks={%
      \edef\@subsubpartlabel{subsubpart@\arabic{question}%
        @\arabic{partno}@\arabic{subpart}@\arabic{subsubpart}}%
      \PgInfo@write{\@subsubpartlabel}%
      \addtocounter{ques@object}{1}%
      \edef\q@object@label{%
            question\arabic{question}@object\arabic{ques@object}}%
      \PgInfo@write{\q@object@label}%
      % In addition to the \PgInfo@write we use an actual \label
      % command.  We do this in order to make the question numbers in
      % the grade tables into \ref's, so that if the user says
      % \usepackage{hyperref}, those question numbers will be clickable.
      % 
      % A further purpose of these labels (which we actually do for all
      % questions, parts, subparts, and subsubparts) is that if a
      % question (or part, etc.) is, e.g., moved from one page to
      % another, LaTeX will notice this and warn the user that LaTeX
      % must be run one more time to be sure everything is correct.
      % 
      % We need to do this even though we've already included code to
      % check when point totals change because questions (and parts,
      % etc.) know what page they're on from reading the info written to
      % the .aux file on the previous run.  Thus, if a question (or
      % part, etc.) is moved to a different page, then the pointsonpage
      % totals won't notice until the *second* subsequent run of LaTeX,
      % and so there'll be no warning to the user on the *first* run.
      % Including these labels gives the user a warning on that first
      % run.
      \label{\@subsubpartlabel}%
      \set@counter@to@pageof{Curr@Page}{\@subsubpartlabel}%
      \expandafter\ifx\csname Contin@\theCurr@Page\endcsname\relax
        % We're the first \question, \part, \subpart, \subsubpart,
        % or choice on this page:
        \global\expandafter\edef\csname
                       Contin@\theCurr@Page\endcsname{\arabic{question}}%
      \fi
      \the\pagepoint@commands
      \global \pageinfo@commands={}%
    }% temp@toks
    \append@toklist \pageinfo@commands \temp@toks
    \ifhmode
      % Remove any skips at the end of the previous paragraph
      % that might cause a blank line, and then end that paragraph:
      \unskip\unskip \par
    \fi
    \@doitem
  }% process@subsubpart
  \list{\question@number}%
    {\usecounter{question}%
    % We use the default definition of \makelabel
    % so as not to interfere with \qformat commands.
    % \def\makelabel##1{\hss\llap{##1}}%
    \settowidth{\leftmargin}{10.\hskip\labelsep}%
    \labelwidth\leftmargin\advance\labelwidth-\labelsep
    \partopsep=0pt
    \questionshook
    }%
  }% End of the first argument of \newenvironment{questions}
  {%
    \endlist
    % Write the number of points of the final question
    % to the .aux file:
    \if@filesw
      \ifnum \arabic{question} > 0\relax
        % First do the regular points:
        \immediate\write\@mainaux
          {\string\gdef\string\pointsofq@\romannumeral
                                \csname c@question\endcsname
            {\prtaux@hlfcntr{pointsof@thisquestion}}}%
        % See if this has changed from the last run of LaTeX:
        \CheckIfChanged@hlf{pointsof@thisquestion}%
                           {pointsofq@\romannumeral
                            \csname c@question\endcsname}%
        % Now do the bonus points:
        \immediate\write\@mainaux
          {\string\gdef\string\bonuspointsofq@\romannumeral
                                \csname c@question\endcsname
            {\prtaux@hlfcntr{bonuspointsof@thisquestion}}}%
        % See if this has changed from the last run of LaTeX:
        \CheckIfChanged@hlf{bonuspointsof@thisquestion}%
                           {bonuspointsofq@\romannumeral
                            \csname c@question\endcsname}%
      \fi
    \fi
  }% End of the second argument of \newenvironment{questions}
  
% \question@number is used as the label in the question list (instead
% of \questionlabel) so that if the user uses a \qformat command,
% we'll use the \@questionformat specified by the \qformat command:
\def\question@number{%
  \if@qformat
    \makebox[\hsize][s]{\@questionformat}\hskip-\labelsep
  \else
    \questionlabel
  \fi
}
\newcommand\questionlabel{\thequestion.}
     
% We want the \part command to be defined *only* inside of a parts
% environment, so that the user can use the standard sectioning \part
% command inside of a questions environment (as long as it's outside of
% a parts environment).

\newenvironment{parts}{%
  \def\@queslevel{part}%
  % If the question numbers are being inserted via a \qformat,
  % and if a question is beginning with a parts environment, then
  % we need to enter horizonal mode to get the qformat printed
  % on the page, rather than saving up the question label (and
  % possible points) to be combined with the label of the first
  % part.  (\if@inlabel tells us if we are still waiting to enter
  % horizontal mode after seeing a \question command.)
  \if@qformat
    \if@inlabel
      \leavevmode
      \@inlabelfalse
    \fi
    % The following is just in case the question had points,
    % in which case @placepoints will still be true.
    % (We used to do this inside of the \thepoints macro,
    % but that allowed for an error if the user specified points for
    % a question but had a \qformat that didn't mention \thepoints.)
    % We also set @placepoints to be false in the \question command,
    % in case one queation follows a previous one that had no parts.
    \global \@placepointsfalse
  \fi
  \def\part{%
    \@bonusfalse
    \process@part
  }%
  \def\bonuspart{%
    \@bonustrue
    \process@part
  }%
  \def\process@part{%
    \if@coverpages
      \cover@question@error
    \fi
    \@checkqueslevel{part}%
    \addtocounter{numparts}{1}%
    % Important: Don't leave any blank lines inside of
    % \pageinfo@commands!!  This token list will be dumped into
    % horizontal mode by \everypar, and so any blank lines will
    % cause paragraph breaks. 
    \temp@toks={%
      \edef\@partlabel{part@\arabic{question}@\arabic{partno}}%
      \PgInfo@write{\@partlabel}%
      \addtocounter{ques@object}{1}%
      \edef\q@object@label{%
            question\arabic{question}@object\arabic{ques@object}}%
      \PgInfo@write{\q@object@label}%
      % In addition to the \PgInfo@write we use an actual \label
      % command.  We do this in order to make the question numbers in
      % the grade tables into \ref's, so that if the user says
      % \usepackage{hyperref}, those question numbers will be clickable.
      % 
      % A further purpose of these labels (which we actually do for all
      % questions, parts, subparts, and subsubparts) is that if a
      % question (or part, etc.) is, e.g., moved from one page to
      % another, LaTeX will notice this and warn the user that LaTeX
      % must be run one more time to be sure everything is correct.
      % 
      % We need to do this even though we've already included code to
      % check when point totals change because questions (and parts,
      % etc.) know what page they're on from reading the info written to
      % the .aux file on the previous run.  Thus, if a question (or
      % part, etc.) is moved to a different page, then the pointsonpage
      % totals won't notice until the *second* subsequent run of LaTeX,
      % and so there'll be no warning to the user on the *first* run.
      % Including these labels gives the user a warning on that first
      % run.
      \label{\@partlabel}%
      \set@counter@to@pageof{Curr@Page}{\@partlabel}%
      \expandafter\ifx\csname Contin@\theCurr@Page\endcsname\relax
        \global\expandafter\edef\csname
            Contin@\theCurr@Page\endcsname{\arabic{question}}%
      \fi
      \the\pagepoint@commands
      \global \pageinfo@commands={}%
    }%
    \append@toklist \pageinfo@commands \temp@toks
    \ifhmode
      % Remove any skips at the end of the previous paragraph
      % that might cause a blank line, and then end that paragraph:
      \unskip\unskip \par
    \fi
    \@doitem
  }% process@part
  \list{\partlabel}%
    {%
    \usecounter{partno}\def\makelabel##1{\hss\llap{##1}}%
    \settowidth{\leftmargin}{(m)\hskip\labelsep}%
    \labelwidth\leftmargin\advance\labelwidth-\labelsep
    \topsep=0pt
    \partopsep=0pt
    \partshook
    }%
  }% newenvironment{parts}
  {\endlist}
\newcommand\partlabel{(\thepartno)}
\def\thepartno{\alph{partno}}

\newenvironment{subparts}{%
  \def\@queslevel{subpart}%
  \list{\subpartlabel}%
    {%
    \usecounter{subpart}\def\makelabel##1{\hss\llap{##1}}%
    \settowidth{\leftmargin}{vii.\hskip\labelsep}%
    \labelwidth\leftmargin\advance\labelwidth-\labelsep
    \topsep=0pt
    \partopsep=0pt
    \subpartshook
    }%
  }%
  {\endlist}
\newcommand\subpartlabel{\thesubpart.}
\def\thesubpart{\roman{subpart}}

\newenvironment{subsubparts}{%
  \def\@queslevel{subsubpart}%
  \list{\subsubpartlabel}%
    {%
    \usecounter{subsubpart}\def\makelabel##1{\hss\llap{##1}}%
    \settowidth{\leftmargin}{($\psi$)\hskip\labelsep}%
    \labelwidth\leftmargin\advance\labelwidth-\labelsep
    \topsep=0pt
    \partopsep=0pt
    \subsubpartshook
    }%
  }%
  {\endlist}
\newcommand\subsubpartlabel{\thesubsubpart)}
\def\thesubsubpart{\greeknum{subsubpart}}




\pagepoint@commands={%
  \ifhlfcntr@pos{latest@points}%
    % We're putting a question (or part, etc.)
    % with points onto this page: 
    \ifnum \theCurr@Page > \thepageof@pagepoints\relax
      % These points go on a later page than
      % the points currently counted in @pagepoints:
      \ifnum \thepageof@pagepoints = 0\relax
        % Do nothing...
      \else
        \immediate\write\@mainaux
          {\string\gdef\string\pointsonpage@
           \romannumeral \csname c@pageof@pagepoints\endcsname
             {\prtaux@hlfcntr{@pagepoints}}}%
        % See if this has changed from the last run of LaTeX:
        \CheckIfChanged@hlf{@pagepoints}{pointsonpage@\romannumeral
                            \csname c@pageof@pagepoints\endcsname}%
      \fi
      % The following is a macro because \theCurr@Page and
      % \thepageof@pagepoints might differ by more than 1:
      \increment@pageof@pagepoints
      % The following label is so that we can make the page
      % numbers in a grade table indexed by page into \pageref's
      % so that \usepackage{hyperref} and pdflatex will
      % make them clickable:
      \label{firstpoints@onpage@\arabic{Curr@Page}}%
    \else
      % These points go on the same page as the points
      % currently counted in @pagepoints:
      \add@hlfcntrtohlfcntr{@pagepoints}{latest@points}%
      \set@hlfcntr{latest@points}{0}%
    \fi
  \fi
  \ifhlfcntr@pos{latest@bonuspoints}%
    % We're putting a question (or part, etc.)
    % with bonus points onto this page: 
    \ifnum \theCurr@Page > \thepageof@pagebonuspoints\relax
      % These bonus points go on a later page than
      % the points currently counted in @pagebonuspoints:
      \ifnum \thepageof@pagebonuspoints = 0\relax
        % Do nothing...
      \else
        \immediate\write\@mainaux
          {\string\gdef\string\bonuspointsonpage@
           \romannumeral \csname c@pageof@pagebonuspoints\endcsname
             {\prtaux@hlfcntr{@pagebonuspoints}}}%
        % See if this has changed from the last run of LaTeX:
        \CheckIfChanged@hlf{@pagebonuspoints}%
                           {bonuspointsonpage@\romannumeral
                            \csname c@pageof@pagebonuspoints\endcsname}%
      \fi
      % The following is a macro because \theCurr@Page and
      % \thepageof@pagebonuspoints might differ by more than 1:
      \increment@pageof@pagebonuspoints
      % The following label is so that we can make the page
      % numbers in a bonus grade table indexed by page into \pageref's
      % so that \usepackage{hyperref} and pdflatex will
      % make them clickable:
      \label{firstbonuspoints@onpage@\arabic{Curr@Page}}%
    \else
      % These points go on the same page as the points
      % currently counted in @pagebonuspoints:
      \add@hlfcntrtohlfcntr{@pagebonuspoints}{latest@bonuspoints}%
      \set@hlfcntr{latest@bonuspoints}{0}%
    \fi
  \fi
}% pagepoint@commands
\def\increment@pageof@pagepoints{%
  \addtocounter{pageof@pagepoints}{1}%
  \ifnum \theCurr@Page > \thepageof@pagepoints\relax
    \immediate\write\@mainaux
        {\string\gdef\string\pointsonpage@
         \romannumeral \csname c@pageof@pagepoints\endcsname{0}}%
    % See if this has changed from the last run of LaTeX:
    \@ifundefined{pointsonpage@\romannumeral
                        \csname c@pageof@pagepoints\endcsname}
      {\global\@pointschangedtrue}%
      {%
      % OK; it's defined.  See if it's changed:
      \begingroup
        \set@hlfcntr{tmp@hlfcntr}{\csname pointsonpage@\romannumeral 
                  \csname c@pageof@pagepoints\endcsname\endcsname}%
        \edef\othpt@check{\prtaux@hlfcntr{tmp@hlfcntr}}%
        \def\pt@check{0}%
        \ifx \pt@check \othpt@check
          % Do nothing
        \else
          \global\@pointschangedtrue
        \fi
      \endgroup
      }%
    \let\next@incr@pageof = \increment@pageof@pagepoints
  \else
    \copy@hlfcntr{@pagepoints}{latest@points}%
    \set@hlfcntr{latest@points}{0}%
    % \page@withpoints will be used to find the last
    % page that has points, which will be written to
    % the .aux file via \AtEndDocument:
    \global\edef\page@withpoints{\thepageof@pagepoints}%
    \let\next@incr@pageof = \relax
  \fi
  \next@incr@pageof
}% increment@pageof@pagepoints
\def\increment@pageof@pagebonuspoints{%
  \addtocounter{pageof@pagebonuspoints}{1}%
  \ifnum \theCurr@Page > \thepageof@pagebonuspoints\relax
    \immediate\write\@mainaux
        {\string\gdef\string\bonuspointsonpage@
         \romannumeral \csname c@pageof@pagebonuspoints\endcsname{0}}%
    % See if this has changed from the last run of LaTeX:
    \@ifundefined{bonuspointsonpage@\romannumeral
                        \csname c@pageof@pagebonuspoints\endcsname}
      {\global\@pointschangedtrue}%
      {%
      % OK; it's defined.  See if it's changed:
      \begingroup
        \set@hlfcntr{tmp@hlfcntr}{\csname bonuspointsonpage@\romannumeral 
                  \csname c@pageof@pagebonuspoints\endcsname\endcsname}%
        \edef\othpt@check{\prtaux@hlfcntr{tmp@hlfcntr}}%
        \def\pt@check{0}%
        \ifx \pt@check \othpt@check
          % Do nothing
        \else
          \global\@pointschangedtrue
        \fi
      \endgroup
      }%
    \let\next@incr@pageof = \increment@pageof@pagebonuspoints
  \else
    \copy@hlfcntr{@pagebonuspoints}{latest@bonuspoints}%
    \set@hlfcntr{latest@bonuspoints}{0}%
    % \page@withbonuspoints will be used to find the last
    % page that has bonus points, which will be written to
    % the .aux file via \AtEndDocument:
    \global\edef\page@withbonuspoints{\thepageof@pagebonuspoints}%
    \let\next@incr@pageof = \relax
  \fi
  \next@incr@pageof
}% increment@pageof@pagebonuspoints






\def\@checkqueslevel#1{%
  \begingroup
    \def\@temp{#1}%
    \ifx\@temp\@queslevel
      % Everything's fine; do nothing.
    \else
      \ClassError{exam}{%
        I found a #1 where I expected to find a
        \@queslevel\MessageBreak
      }{%
        Both #1 and \@queslevel \space can be used only inside the
        correct \MessageBreak \space \space
        environment and outside of any smaller environment
        \MessageBreak
      }%
    \fi
  \endgroup
}

\def\@doitem{\@ifnextchar[{\@readpoints}%
                          {\item@points@pageinfo}%
}

\def\@readpoints[#1]{%
% We use \def for \@points instead of \edef because we don't want
% \half (if present) to be expanded yet, so that the command \points
% can figure out how to deal with it:
  \def\@points{#1}%
  \global \@placepointstrue
  \if@addpoints
    \if@bonus
      \addto@hlfcntr{numbonuspoints}{\@points}%
      \addto@hlfcntr{bonuspointsof@thisquestion}{\@points}%
      % latest@bonuspoints is a holding area for bonus points to be
      % added to @pagepoints after we check whether they're
      % on the same page as the points currently counted
      % by @pagepoints:
      \addto@hlfcntr{latest@bonuspoints}{\@points}%
    \else
      \addto@hlfcntr{numpoints}{\@points}%
      \addto@hlfcntr{pointsof@thisquestion}{\@points}%
      % latest@points is a holding area for points to be
      % added to @pagepoints after we check whether they're
      % on the same page as the points currently counted
      % by @pagepoints:
      \addto@hlfcntr{latest@points}{\@points}%
    \fi
  \fi
  \item@points@pageinfo
}




% Bug fix, 5 April 2004: \item@points@pageinfo
% Appending \point@toks and \pageinfo@commands to \everypar:
% Instead of appending the contents of \point@toks and
% \pageinfo@commands to \everypar using \append@toklist,
% we instead want to append only the two tokens
%   \the\point@toks
% and the two tokens
%   \the\pageinfo@commands
% to \everypar.  We need to do this because if a questions environment
% immediately follows a \section command, then @nobreak will be true,
% and so the \if@nobreak inside of \everypar will *not* execute the
% \everypar={} that we had been counting on to keep the points from
% being inserted a second time in the second paragraph of a question.
% Since we've put the command \global \point@toks={} inside of 
% \point@toks and the command \pageinfo@commands={} inside of
% \pageinfo@commands, when the contents of \point@toks and of
% \pageinfo@commands are executed (when we enter horizontal mode and
% \everypar is dumped in), the contents of \point@toks and
% \pageinfo@commands will be made empty, and so if
% the second paragraph also gets \the\point@toks and
% \the\pageinfo@commands, it won't matter.

\def\item@points@pageinfo{%
  \item
  % If @qformat is true, and if we're currently doing a question
  % (rather than a part, subpart, or subsubpart), then we don't want
  % to set the points (if any), since the points of a question will
  % appear only if the user chooses to cause that by putting a
  % \thepoints in the argument of the \qformat command.
  % 
  % Also: We need to do this here, *after* the \item command, rather
  % than inside the macro \@readpoints, because the \item command
  % puts the result of the \qformat command into an \hbox (with the
  % command ``\sbox\@tempboxa{\makelabel{#1}}%''), expanding the
  % argument of \qformat as it does so.  Thus, @placepoints will be
  % true when the argument of \qformat is expanded, and so if the
  % user put a \thepoints command inside that argument it will
  % correctly expand to the number of points.  (When @placepoints is
  % false, \thepoints expands to nothing at all).
  \if@qformat
    \ifx\ques@ref\@queslevel
      \global \@placepointsfalse
    \fi
  \fi
  \if@placepoints
    % Since we want the user to be able to say \thepoints in the
    % argument to a \pointformat command, we need \@placepointstrue
    % when \point@block is expanded so that \thepoints will actually
    % print something.  (After setting up \point@toks, we do
    % \@placepointsfalse, but \point@block isn't actually expanded
    % until we enter horizontal mode.)  Thus, we define
    % \padded@point@block, and use that instead of \point@block.  We
    % put  \begingroup and \endgroup around this to confine the
    % effect of \@placepointstrue and also to confine the effect of
    % any declarations like, e.g., \bfseries that the user might put
    % in the argument of a \pointformat command.
    %
    % Note: We first tried using an \edef to expand \point@block right
    % here, while @placepoints is true, but that causes problems if
    % the user puts a \boldmath declaration in the argument of a
    % \pointformat command.  Apparently, expanding \boldmath (without 
    % executing anything) gives you bunches of undefined control
    % sequence errors.
    \if@bonus
      \def\padded@point@block{%
        \begingroup
          \@placepointstrue
          \bonuspoint@block
        \endgroup
      }%
    \else
      \def\padded@point@block{%
        \begingroup
          \@placepointstrue
          \point@block
        \endgroup
      }%
    \fi
    % \setup@point@toks puts commands into \point@toks to place
    % \padded@point@block at the correct spot.  It doesn't append
    % anything to \everypar (we do that in this macro, below). 
    \if@pointsdropped
      % Do nothing!
    \else
      \setup@point@toks
    \fi
    \global \@placepointsfalse
  \fi
  % We *don't* use \append@toklist; see Bug fix note above
  % We can append the tokens ``\the\point@toks'' whether or not we're
  % setting any points because if we're not setting them, \point@toks
  % will be empty.
  % Also: It's important to do this *after* the \item command above,
  % since the \item command discards the previous contents of
  % \everypar.
  % Version 2.217-beta changes:
  % Instead of appending stuff to \everypar, we insert
  % \the \pageinfo@commands and \the \point@toks 
  % into the box \@labels:
  \global\setbox\@labels\hbox{\unhbox\@labels
    \the \pageinfo@commands
    \the \point@toks}%
  %   \edef\append@everypar{\noexpand\everypar={\the\everypar
  %                         \noexpand\the \noexpand\pageinfo@commands
  %                         \noexpand\the \noexpand\point@toks}}%
  %   \append@everypar
}







% Initialize \@points:
% (The only reason I think this is necessary is in case the user uses
% a \qformat command, puts \themarginpoints into the format (which is
% *not* the intended use of \themarginpoints), and then doesn't have
% any points for the first question.)
\def\@points{0}


\def\setup@point@toks{%
% We set the token list \point@toks equal to the sequence of commands
% needed to put \padded@point@block at the correct location, followed by the
% tokens ``\global \point@toks={}''.  The \question, \part, \subpart,
% or \subsubpart command then adds the two tokens ``\the\point@toks''
% to \everypar.
%
% Note: It is not the *contents* of \point@toks that is added to
% \everypar; just the two tokens ``\the\point@toks''.  This difference
% is the bug fix of 2 April 2004, described above (the bug was that in
% earlier versions, we used to append the contents).
%
% The result of this is that whenever we finally enter horizontal mode
% (because we finally encountered the text of a question, part,
% subpart, or subsubpart) the contents of \point@toks will be dumped
% into horizontal mode and executed, and so the points will be placed
% and the token list \point@toks will be set to empty.  Thus, in the
% occasional circumstances in which \everypar is *not* set to empty
% after being added to the first paragraph (which occurs when a
% questions environment immediately follows a \section command), and
% so \everypar will still contain ``\the\point@toks'' when it
% encounters a possible second paragraph of the first question, the
% tokens ``\the\point@toks'' will insert an *empty* token list, which
% will do no harm.
%
  \if@pointsinleftmargin
    \point@toks={%
          \llap{\padded@point@block 
                \hskip\@totalleftmargin
                \hskip\marginpointssep
          }%
          \global \point@toks={}%
    }%
  \else
    \if@pointsinrightmargin
      \point@toks={%
            \rlap{\hskip-\@totalleftmargin
                  \hskip\textwidth
                  \hskip\@rightmargin
                  \hskip-\rightpointsmargin
                  \llap{\padded@point@block}%
            }%
            \global \point@toks={}%
      }%
    \else
      % The points just go after the question number:
      \point@toks={%
            \padded@point@block
            \enspace
            \global \point@toks={}%
      }%
    \fi
  \fi
}% setup@point@toks



\def\droppoints{%
  \leavevmode\unskip\nobreak\hfill
  \rlap{\hskip\rightmargin  % Defined by the list environment
        \hskip\@rightmargin % Defined by exam.cls
        \hskip-\rightpointsmargin
        \llap{\padded@point@block}%
  }% rlap
  \par
}


\def\droptotalpoints{%
  \leavevmode\unskip\nobreak\hfill
  \rlap{\hskip\rightmargin  % Defined by the list environment
        \hskip\@rightmargin % Defined by exam.cls
        \hskip-\rightpointsmargin
        \llap{\total@block}%
  }% rlap
  \par
}% droptotalpoints
\def\droptotalbonuspoints{%
  \leavevmode\unskip\nobreak\hfill
  \rlap{\hskip\rightmargin  % Defined by the list environment
        \hskip\@rightmargin % Defined by exam.cls
        \hskip-\rightpointsmargin
        \llap{\bonustotal@block}%
  }% rlap
  \par
}% droptotalbonuspoints

% The following is the default definition;
% it can be changed by a \totalformat command.
\def\total@block{%
  Total for Question \thequestion: \totalpoints\@marginpointname
}% total@block
\def\bonustotal@block{%
  Total for Question \thequestion: \totalbonuspoints\@marginbonuspointname
}% bonustotal@block

\def\totalformat#1{%
  \gdef\total@block{\begingroup #1\endgroup}%
}% totalformat
\def\bonustotalformat#1{%
  \gdef\bonustotal@block{\begingroup #1\endgroup}%
}% bonustotalformat
% The following is for use in the argument to a \totalformat command:
\def\totalpoints{\pointsofquestion{\arabic{question}}}
\def\totalbonuspoints{\bonuspointsofquestion{\arabic{question}}}



% @placepoints is set true when we encounter a question (or part, etc.)
% that has points.  It is set to false (1) when we set \point@toks equal
% to the sequence of commands required to put the properly formatted
% points onto the page (this happens only if @qformat is false or if
% @qformat is true but we're not doing a question), or (2) by a
% \question command or entering a parts environment (since if we're
% doing a question and @qformat is true, we need to leave @placepoints
% true so that the \thepoints command can tell if it should expand to
% points or to nothing, and encountering a \question command or parts
% environment tells us that we no longer have to deal with a possible
% \thepoints, since we won't be expanding a qformat).
\newif\if@placepoints
\@placepointsfalse


% \marginpointssep will be used if the user says
% \pointsinleftmargin.  It will be the distance from whatever encloses
% the points (parentheses, brackets, or a box) to the left margin:
\newlength\marginpointssep
\setlength{\marginpointssep}{5pt}

% \rightpointsmargin will be used if the user says \pointsinrightmargin.
% It will be the distance from whatever encloses the point (parentheses,
% brackets, or a box) to the right edge of the paper:
\newlength\rightpointsmargin
\setlength{\rightpointsmargin}{1cm}


\newif\if@pointsdropped
\newif\if@pointsinleftmargin
\newif\if@pointsinrightmargin
\def\pointsinleftmargin{\global\@pointsinleftmargintrue 
                    \global\@pointsinrightmarginfalse
                    \global\@pointsdroppedfalse
                    \gdef\pt@name{\@marginpointname}%
                    \gdef\bnspt@name{\@marginbonuspointname}}
\def\pointsinrightmargin{\global\@pointsinrightmargintrue
                         \global\@pointsinleftmarginfalse
                         \global\@pointsdroppedfalse
                         \gdef\pt@name{\@marginpointname}%
                         \gdef\bnspt@name{\@marginbonuspointname}}
\def\nopointsinmargin{\global\@pointsinleftmarginfalse
                      \global\@pointsinrightmarginfalse
                      \global\@pointsdroppedfalse
                      \gdef\pt@name{\@pointname}%
                      \gdef\bnspt@name{\@bonuspointname}}
\def\pointsdroppedatright{\global\@pointsdroppedtrue
                          \global\@pointsinleftmarginfalse
                          \global\@pointsinrightmarginfalse
                          \gdef\pt@name{\@marginpointname}%
                          \gdef\bnspt@name{\@marginbonuspointname}}
\let\pointsinmargin\pointsinleftmargin
\let\nopointsinrightmargin\nopointsinmargin
\let\nopointsinleftmargin\nopointsinmargin

\nopointsinmargin


% Will the points be displayed inside parentheses (the default), or
% will they be boxed or bracketed, or customized using pointformat:
\def\boxedpoints{%
  \gdef\point@block{\fbox{\@points\pt@name}}%
  \gdef\bonuspoint@block{\fbox{\@points\bnspt@name}}%
}
\def\noboxedpoints{%
  \gdef\point@block{(\@points\pt@name)}%
  \gdef\bonuspoint@block{(\@points\bnspt@name)}%
}
\def\bracketedpoints{%
  \gdef\point@block{[\@points\pt@name]}%
  \gdef\bonuspoint@block{[\@points\bnspt@name]}%
}
\let\nobracketedpoints=\noboxedpoints

\def\pointformat#1{%
  % We don't have to worry about the user putting things
  % like \bfseries, etc. into \point@block, because
  % \padded@point@block encloses \point@block in a group,
  % which confines the effects of anything here:
  \gdef\point@block{#1}%
}

\def\bonuspointformat#1{%
  % We don't have to worry about the user putting things
  % like \bfseries, etc. into \point@block, because
  % \padded@point@block encloses \point@block in a group,
  % which confines the effects of anything here:
  \gdef\bonuspoint@block{#1}%
}
\def\thebonuspoints{\@points \@bonuspointname}

%Initialize:
\noboxedpoints




\def\pointname#1{\gdef\@pointname{#1}}
\def\bonuspointname#1{\gdef\@bonuspointname{#1}}
% Initialize to leave a space, and then the word `points':
%%\pointname{ points}
% The following improvement was contributed by 
% Mate Wierdl <mw@wierdlmpc.msci.memphis.edu> 
% If the number of points is ``1'', then the default value of
% \pointname will print `` point'' instead of `` points'' (and this
% version of the command doesn't generate an error message if the
% points entry is something other than a number):
% Note the space before the \points in the following; it's
% intentional!)
\pointname{ \points}
\bonuspointname{ \bonuspoints}
\newcommand\point@sing{point}
\newcommand\point@plur{points}
\newcommand\pointpoints[2]{%
  \renewcommand\point@sing{#1}%
  \renewcommand\point@plur{#2}%
}
%\newcommand\bonuspoint@sing{bonus point}
%\newcommand\bonuspoint@plur{bonus points}
\newcommand\bonuspoint@sing{point (bonus)}
\newcommand\bonuspoint@plur{points (bonus)}
\newcommand\bonuspointpoints[2]{%
  \renewcommand\bonuspoint@sing{#1}%
  \renewcommand\bonuspoint@plur{#2}%
}



% The command \points:
% We use \ifthenelse and \equal so that if the user types something
% other than a legit point value, there still won't be any error
% messages.  We rig it so that if the point value looks like it's
% intended to be One or one or ONE, or some strange way of attempting
% one half, then it will expand to the singular value.  Alas, this is
% only useful for English, but I'm hoping few or no users will try doing
% this anyway.

% 0 points, one half point, 1 point, 1 and a half points, etc.:
\newcommand\points{%
  \begingroup
    \let\half=\relax
    \edef\pt@string{\@points}%
    \ifthenelse{\equal{\pt@string}{1} \or \equal{\pt@string}{\half}}
          {\point@sing}{\point@plur}%
  \endgroup
}% \points
\newcommand\bonuspoints{%
  \begingroup
    \let\half=\relax
    \edef\pt@string{\@points}%
    \ifthenelse{\equal{\pt@string}{1} \or \equal{\pt@string}{\half}}
          {\bonuspoint@sing}{\bonuspoint@plur}%
  \endgroup
}% \bonuspoints
%\newcommand\points{%
%  \begingroup
%    \let\half=\relax
%    \edef\pt@string{\@points}%
%    \ifthenelse{\equal{\pt@string}{1} \or \equal{\pt@string}{\half} \or
%      \equal{\pt@string}{0\half} \or \equal{\pt@string}{0 \half}
%      \equal{\pt@string}{one} \or \equal{\pt@string}{One} \or
%      \equal{\pt@string}{ONE}}
%        {\point@sing}{\point@plur}%
%  \endgroup
%}

%\newcommand\points{\ifthenelse{\equal{\@points}{1}}{\point@sing}{\point@plur}}
% If we used the following line instead, then you'd get an error
% message if the point value contained something other than a valid
% integer:
%\pointname{ \ifthenelse{\@points = 1}{point}{points}}

% We used to define a command named \marks that works like \points,
% except that it expands to either ``mark'' or ``marks'', but that
% conflicts with some package or other.  Thus, we'll implement
% \marksnotpoints using the \pointpoints command instead:
\newcommand\marksnotpoints{%
  \pointpoints{mark}{marks}%
  \bonuspointpoints{mark (bonus)}{marks (bonus)}%
}% \marksnotpoints


% \@marginpointname is used in place of \@pointname if any of
% \@pointsinmargin, \@pointsinrightmargin, and \@pointsdropped are
% true:
\def\marginpointname#1{\gdef\@marginpointname{#1}}
\marginpointname{}
\def\marginbonuspointname#1{\gdef\@marginbonuspointname{#1}}
\marginbonuspointname{ (bonus)}


%--------------------------------------------------------------------
%                   choices (for multiple choice)


\renewcommand\thechoice{\Alph{choice}}
\newcommand\choicelabel{\thechoice.}

% We will have \@correctchoicetrue when we're printing solutions
% and we're printing the correct choice of a choices or
% oneparchoices environment.
% We'll say \begingroup before saying \@correctchoicetrue
% and we'll say \endgroup at either the next \choice or \correctchoice
% or the end of the choices or oneparchoices environment.
% Thus, we'll never again need to say \@correctchoicefalse
\newif\if@correctchoice
\@correctchoicefalse

\newcommand\CorrectChoiceEmphasis[1]{%
  \def\CorrectChoice@Emphasis{#1}%
}
\CorrectChoiceEmphasis{\bfseries}
\let\correctchoiceemphasis\CorrectChoiceEmphasis


\newtoks\choice@toks
\def\do@choice@pageinfo{%
  \choice@toks={%
    \addtocounter{ques@object}{1}%
    \edef\q@object@label{%
          question\arabic{question}@object\arabic{ques@object}}%
    \PgInfo@write{\q@object@label}%
    \set@counter@to@pageof{Curr@Page}{\q@object@label}%
      \expandafter\ifx\csname Contin@\theCurr@Page\endcsname\relax
        % We're the first \question, \part, \subpart, \subsubpart,
        % or choice on this page:
        \global\expandafter\edef\csname
                       Contin@\theCurr@Page\endcsname{\arabic{question}}%
      \fi
    \choice@toks={}%
  }%
  % Version 2.217-beta changes:
  % Instead of appending stuff to \everypar, we insert
  % \the \pageinfo@commands and \the \point@toks 
  % into the box \@labels:
  \global\setbox\@labels\hbox{\unhbox\@labels
    \the \choice@toks}%
  %   \edef\append@everypar{\noexpand\everypar={\the\everypar
  %                         \noexpand\the \noexpand\choice@toks}}%
  %   \append@everypar
}% do@choice@pageinfo



% Added 22 April 2004: Increased the \leftmargin by 2.5em,
% so the choices will be visibly indented.
\newenvironment{choices}%
  {\list{\choicelabel}%
     {\usecounter{choice}\def\makelabel##1{\hss\llap{##1}}%
       \settowidth{\leftmargin}{W.\hskip\labelsep\hskip 2.5em}%
       \def\choice{%
         \if@correctchoice
           \endgroup
         \fi
         \item
         \do@choice@pageinfo
       } % choice
       \def\CorrectChoice{%
         \if@correctchoice
           \endgroup
         \fi
         \ifprintanswers
           % We can't say \choice here, because that would
           % insert an \endgroup:
           \begingroup \@correctchoicetrue
           \CorrectChoice@Emphasis
         \fi
         \item
         \do@choice@pageinfo
       } % CorrectChoice
       \let\correctchoice\CorrectChoice
       \labelwidth\leftmargin\advance\labelwidth-\labelsep
       \topsep=0pt
       \partopsep=0pt
       \choiceshook
     }%
  }%
  {\if@correctchoice \endgroup \fi \endlist}

\newenvironment{oneparchoices}%
  {%
    \setcounter{choice}{0}%
    \def\choice{%
      \if@correctchoice \endgroup \fi
      \refstepcounter{choice}%
      \ifnum\value{choice}>1
        \penalty -50\hskip 1em plus 1em\relax
      \fi
      \choicelabel
      % No need to put the following into a token string; we just put
      % the choicelabel onto the page, so we're at the spot whose page
      % number we want to record:
      \addtocounter{ques@object}{1}%
      \edef\q@object@label{%
            question\arabic{question}@object\arabic{ques@object}}%
      \PgInfo@write{\q@object@label}%
      \set@counter@to@pageof{Curr@Page}{\q@object@label}%
        \expandafter\ifx\csname Contin@\theCurr@Page\endcsname\relax
          % We're the first \question, \part, \subpart, \subsubpart,
          % or choice on this page:
          \global\expandafter\edef\csname
                         Contin@\theCurr@Page\endcsname{\arabic{question}}%
        \fi
        \nobreak\enskip
    }% choice
    \def\CorrectChoice{%
      \if@correctchoice \endgroup \fi
      \refstepcounter{choice}%
      \ifprintanswers
        \begingroup \@correctchoicetrue 
        \CorrectChoice@Emphasis
      \fi
      \ifnum\value{choice}>1
        \penalty -50\hskip 1em plus 1em\relax
      \fi
      \choicelabel
      % No need to put the following into a token string; we just put
      % the choicelabel onto the page, so we're at the spot whose page
      % number we want to record:
      \addtocounter{ques@object}{1}%
      \edef\q@object@label{%
            question\arabic{question}@object\arabic{ques@object}}%
      \PgInfo@write{\q@object@label}%
      \set@counter@to@pageof{Curr@Page}{\q@object@label}%
        \expandafter\ifx\csname Contin@\theCurr@Page\endcsname\relax
          % We're the first \question, \part, \subpart, \subsubpart,
          % or choice on this page:
          \global\expandafter\edef\csname
                         Contin@\theCurr@Page\endcsname{\arabic{question}}%
        \fi
        \nobreak\enskip
    }% CorrectChoice
    \let\correctchoice\CorrectChoice
    \let\par\@empty
    % If we're continuing the paragraph containing the question,
    % then leave a bit of space before the first choice:
    \ifvmode\else\enskip\fi
    \ignorespaces
  }%
  {\if@correctchoice \endgroup \fi}


%--------------------------------------------------------------------
%             Answer Lines (for short answer questions)

% Note: \ques@ref is also used in \item@points@pageinfo

\def\ques@ref{question}
\def\part@ref{part}
\def\subpart@ref{subpart}
\def\subsubpart@ref{subsubpart}

\newlength\answerlinelength
\newlength\answerskip
\newlength\answerclearance
\setlength\answerlinelength{1in}
\setlength\answerskip{2ex}
\setlength\answerclearance{0.2ex}

\newcommand\answerline[1][{}]{%
  % One optional argument, the default value of which is empty.
  \ifx\@queslevel\ques@ref
    \let\ans@l=\questionlabel
  \else
    \ifx\@queslevel\part@ref
      \let\ans@l=\partlabel
    \else
      \ifx\@queslevel\subpart@ref
        \let\ans@l=\subpartlabel
      \else
        \ifx\@queslevel\subsubpart@ref
          \let\ans@l=\subsubpartlabel
        \else
          % Oops; no question level defined.
          % We must be outide of the questions environment.
          % Just leave out the label, I guess:
          \def\ans@l{}%
        \fi
      \fi
    \fi
  \fi
  \par \nobreak \vskip \answerskip
  \hfill 
  \ifprintanswers
    \ans@l~\hbox to 0pt{\hbox to \answerlinelength{\hrulefill}\hss}%
    \raise \answerclearance\hbox to \answerlinelength{%
      \CorrectChoice@Emphasis \hfil #1\hss}%
  \else
    \ans@l~\hbox to \answerlinelength{\hrulefill}%
  \fi
  \par
}% answerline

%--------------------------------------------------------------------
%                            \fillwithlines


% \fillwithlines takes one argument, which is either a length or \fill,
% and it fills that much vertical space with horizontal lines that run
% the length of the current line.  That is, they extend from the
% current left margin (which depends on whether we're in a question,
% part, subpart, or subsubpart) to the right margin.
%
% The distance between the lines is \linefillheight, whose default value
% is set with the command
%
% \setlength\linefillheight{.25in}
%
% This value can be changed by giving a new \setlength command.
%
% The thickness of the lines is \linefillthickness, whose default value
% is set with the command
%
% \setlength\linefillthickness{.1pt}
%
% This value can be changed by giving a new \setlength command.


\newlength\linefillheight
\newlength\linefillthickness
\setlength\linefillheight{.25in}
\setlength\linefillthickness{0.1pt}

\newcommand\linefill{\leavevmode
    \leaders\hrule height \linefillthickness \hfill\kern\z@}


\def\fillwithlines#1{%
  \begingroup
  \ifhmode
    \par
  \fi
  \hrule height \z@
  \nobreak
  \setbox0=\hbox to \hsize{\hskip \@totalleftmargin
          \vrule height \linefillheight depth \z@ width \z@
          \linefill}%
  % We use \cleaders (rather than \leaders) so that a given
  % vertical space will always produce the same number of lines
  % no matter where on the page it happens to start:
  \cleaders \copy0 \vskip #1 \hbox{}%
  \endgroup
}

%--------------------------------------------------------------------
%                         \fillwithdottedlines


% \fillwithdottedlines is similar to \fillwithlines, except that it
% fills the space with dotted lines (created by \dotfill) rather than
% with solid lines.

% \fillwithdottedlines takes one argument, which is either a length or
% \fill, and it fills that much vertical space with dotted lines that
% run the length of the current line.  That is, they extend from the
% current left margin (which depends on whether we're in a question,
% part, subpart, or subsubpart) to the right margin.
%
% The distance between the lines is \dottedlinefillheight, whose
% default value is set with the command
%
% \setlength\dottedlinefillheight{.25in}
%
% This value can be changed by giving a new \setlength command.

\newlength\dottedlinefillheight
\setlength\dottedlinefillheight{.25in}

\def\fillwithdottedlines#1{%
  \begingroup
  \ifhmode
    \par
  \fi
  \hrule height \z@
  \nobreak
  \setbox0=\hbox to \hsize{\hskip \@totalleftmargin
          \vrule height \dottedlinefillheight depth \z@ width \z@
          \dotfill}%
  % We use \cleaders (rather than \leaders) so that a given
  % vertical space will always produce the same number of lines
  % no matter where on the page it happens to start:
  \cleaders \copy0 \vskip #1 \hbox{}%
  \endgroup
}

%--------------------------------------------------------------------
%                      \uplevel and \fullwidth:

% \uplevel is used to print text at the indentation level of the 
% enclosing environment.  For example, to precede a question with
% directions about how that question should be answered, you would
% say \uplevel{Answer this question correctly.}
% 
% \fullwidth is similar, but uses the full page of text on the page.

\long\def\uplevel#1{%
  \par\bigskip
  \vbox{%
    % We set \leftskip to provide the correct left margin for whatever
    % text is in the argument of the \uplevel command:
    \leftskip=\@totalleftmargin
    \advance\leftskip-\leftmargin
    % We adjust \@totalleftmargin (and linewidth?) in case there's a
    % solution environment inside of the argument to the \uplevel:
    \advance\@totalleftmargin-\leftmargin
    \advance\linewidth\leftmargin
    #1%
  }% vbox
  \nobreak
}

\long\def\fullwidth#1{%
  \par\bigskip
  \vbox{%
    \leftskip=0pt \rightskip=0pt
    \advance\linewidth\@totalleftmargin
    \@totalleftmargin=0pt
    #1%
  }% vbox
  \nobreak
}


%--------------------------------------------------------------------
%--------------------------------------------------------------------
%
%                        ********************
%                        ** GRADING TABLES **
%                        ********************



\newcounter{@iterator}
\newlength\@cellwidth

\def\cellwidth#1{\@cellwidth=#1}
\def\gradetablestretch#1{\def\@gtblstretch{#1}}

% All of the following that begin with `h' are for horizontal tables,
% and all of them that begin with `v' are for vertical tables:
\def\hqword#1{\def\@hqword{#1}}
\def\hpword#1{\def\@hpword{#1}}
\def\hsword#1{\def\@hsword{#1}}
\def\htword#1{\def\@htword{#1}}
\def\vqword#1{\def\@vqword{#1}}
\def\vpword#1{\def\@vpword{#1}}
\def\vsword#1{\def\@vsword{#1}}
\def\vtword#1{\def\@vtword{#1}}

\def\vpgword#1{\def\@vpgword{#1}}
\def\hpgword#1{\def\@hpgword{#1}}

% The following are the versions for bonusgradetable:
\def\bhqword#1{\def\@bhqword{#1}}
\def\bhpword#1{\def\@bhpword{#1}}
\def\bhsword#1{\def\@bhsword{#1}}
\def\bhtword#1{\def\@bhtword{#1}}
\def\bvqword#1{\def\@bvqword{#1}}
\def\bvpword#1{\def\@bvpword{#1}}
\def\bvsword#1{\def\@bvsword{#1}}
\def\bvtword#1{\def\@bvtword{#1}}

\def\bvpgword#1{\def\@bvpgword{#1}}
\def\bhpgword#1{\def\@bhpgword{#1}}


% Initialize:
\cellwidth{2em}
\gradetablestretch{1.5}
\hpword{Points:}
\hsword{Score:}
\htword{Total}
\vpword{Points}
\vsword{Score}
\vtword{Total:}

\bhpword{Bonus Points:}
\bhsword{Score:}
\bhtword{Total}
\bvpword{Bonus Points}
\bvsword{Score}
\bvtword{Total:}

% For tables indexed by question number:
\vqword{Question}
\hqword{Question:}
\bvqword{Question}
\bhqword{Question:}

% For tables indexed by page number:
\vpgword{Page}
\hpgword{Page:}
\bvpgword{Page}
\bhpgword{Page:}



% The only commands here accessible to the user are \gradetable,
% \bonusgradetable, \pointtable, \bonuspointtable, \partialgradetable,
% \partialbonusgradetable, \partialpointtable,
% \partialbonuspointtable, \begingradingrange, and \endgradingrange.

% The possibilities are

%   \gradetable[v][questions]
%   \gradetable[v][pages]
%   \gradetable[h][questions]
%   \gradetable[h][pages]

%   \bonusgradetable[v][questions]
%   \bonusgradetable[v][pages]
%   \bonusgradetable[h][questions]
%   \bonusgradetable[h][pages]

%   \pointtable[v][questions]
%   \pointtable[v][pages]
%   \pointtable[h][questions]
%   \pointtable[h][pages]

%   \bonuspointtable[v][questions]
%   \bonuspointtable[v][pages]
%   \bonuspointtable[h][questions]
%   \bonuspointtable[h][pages]

%   \partialgradetable{whatever}[v][questions]
%   \partialgradetable{whatever}[v][pages]
%   \partialgradetable{whatever}[h][questions]
%   \partialgradetable{whatever}[h][pages]

%   \partialbonusgradetable{whatever}[v][questions]
%   \partialbonusgradetable{whatever}[v][pages]
%   \partialbonusgradetable{whatever}[h][questions]
%   \partialbonusgradetable{whatever}[h][pages]

%   \partialpointtable{whatever}[v][questions]
%   \partialpointtable{whatever}[v][pages]
%   \partialpointtable{whatever}[h][questions]
%   \partialpointtable{whatever}[h][pages]

%   \partialbonuspointtable{whatever}[v][questions]
%   \partialbonuspointtable{whatever}[v][pages]
%   \partialbonuspointtable{whatever}[h][questions]
%   \partialbonuspointtable{whatever}[h][pages]

%   \begingradingrange{whatever}
%   \endgradingrange{whatever}
%
% where ``whatever'' is a label chosen by the user.

% If one or both optional arguments are omitted, the defaults are
% `[v]' and `[questions]'.

% \@scorestrue means we're doing \gradetable
% \@scoresfalse mans we're doing \pointtable
\newif\if@scores

% \@partialtrue means we're doing \partialgradetable,
% \partialbonusgradetable, \partialpointtable, or
% \partialbonuspointtable:
\newif\if@partial


% It's OK to use the counter num@cols as a scratch counter
% in \begingradingrange and \endgradingrange because
% it's only used in typesetting tables:
\def\begingradingrange#1{%
  \setcounter{num@cols}{\value{question}}%
  \addtocounter{num@cols}{1}%
  \immediate\write\@mainaux
  {\string\expandafter\string\gdef
    \string\csname\space tbl@#1@firstq\string\endcsname
      {\arabic{num@cols}}}%
  \write\@mainaux
  {\string\expandafter\string\gdef
    \string\csname\space tbl@#1@firstp\string\endcsname
      {\thepage}}%
}% begingradingrange

\def\endgradingrange#1{%
  \setcounter{num@cols}{\value{question}}%
  \immediate\write\@mainaux
  {\string\expandafter\string\gdef
    \string\csname\space tbl@#1@lastq\string\endcsname
      {\arabic{num@cols}}}%
  \write\@mainaux
  {\string\expandafter\string\gdef
    \string\csname\space tbl@#1@lastp\string\endcsname
      {\thepage}}%
}% endgradingrange




% Now that grading tables may be for only part of the exam,
% we need the counter tbl@points to add up the total points
% for the questions (or pages) that appear on the table:
\new@hlfcntr{tbl@points}


\def\partialgradetable#1{%
  \@scorestrue
  \@bonusfalse
  \@partialtrue
  \def\tbl@range{#1}%
  % If the user doesn't include the optional argument
  % choosing between vertical and horizontal,
  % we give them vertical:
  \@ifnextchar[{\i@gtable}{\i@gtable[v]}%
}% partialgradetable

\def\partialbonusgradetable#1{%
  \@scorestrue
  \@bonustrue
  \@partialtrue
  \def\tbl@range{#1}%
  % If the user doesn't include the optional argument
  % choosing between vertical and horizontal,
  % we give them vertical:
  \@ifnextchar[{\i@gtable}{\i@gtable[v]}%
}% partialbonusgradetable

\def\partialpointtable#1{%
  \@scoresfalse
  \@bonusfalse
  \@partialtrue
  \def\tbl@range{#1}%
  % If the user doesn't include the optional argument
  % choosing between vertical and horizontal,
  % we give them vertical:
  \@ifnextchar[{\i@gtable}{\i@gtable[v]}%
}% partialpointtable

\def\partialbonuspointtable#1{%
  \@scoresfalse
  \@bonustrue
  \@partialtrue
  \def\tbl@range{#1}%
  % If the user doesn't include the optional argument
  % choosing between vertical and horizontal,
  % we give them vertical:
  \@ifnextchar[{\i@gtable}{\i@gtable[v]}%
}% partialbonuspointtable

%--------------------------------------------------------------------

\def\gradetable{%
  \@scorestrue
  \@bonusfalse
  \@partialfalse
  % If the user doesn't include the optional argument
  % choosing between vertical and horizontal,
  % we give them vertical:
  \@ifnextchar[{\i@gtable}{\i@gtable[v]}%
}% gradetable

\def\bonusgradetable{%
  \@scorestrue
  \@bonustrue
  \@partialfalse
  % If the user doesn't include the optional argument
  % choosing between vertical and horizontal,
  % we give them vertical:
  \@ifnextchar[{\i@gtable}{\i@gtable[v]}%
}% bonusgradetable

\def\pointtable{%
  \@scoresfalse
  \@bonusfalse
  \@partialfalse
  % If the user doesn't include the optional argument
  % choosing between vertical and horizontal,
  % we give them vertical:
  \@ifnextchar[{\i@gtable}{\i@gtable[v]}%
}% pointtable

\def\bonuspointtable{%
  \@scoresfalse
  \@bonustrue
  \@partialfalse
  % If the user doesn't include the optional argument
  % choosing between vertical and horizontal,
  % we give them vertical:
  \@ifnextchar[{\i@gtable}{\i@gtable[v]}%
}% bonuspointtable

%--------------------------------------------------------------------

% \i@gtable and \ii@gtable insert any missing optional arguments
% (the defaults being [v] and [questions]) and then make sure
% that the user said \addpoints and that this isn't the
% first run of LaTeX.
% \do@table then branches, depending on whether the user
% selected [questions] or [pages].

\def\i@gtable[#1]{%
  % If the user doesn't include the second optional argument,
  % which chooses between questions and pages,
  % we give them questions:
  \@ifnextchar[{\ii@gtable{#1}}{\ii@gtable{#1}[questions]}%
}
\def\ii@gtable#1[#2]{%
  % We make sure the user said \addpoints, and then make sure
  % that this isn't the first run of LaTeX (by checking that
  % \exam@numpoints is defined).  If both of those are OK,
  % we go on to \do@table to see whether we're doing a table
  % indexed by questions or by pages.
  \if@addpoints
    \@ifundefined{exam@numpoints}%
      {\ClassWarning{exam}%
        {%
          You must run LaTeX again to produce the
            table.\MessageBreak
        }%
        \fbox{Run \LaTeX{} again to produce the table}%
      }%
      {\do@table{#1}{#2}}%
  \else
    \ClassError{exam}{%
      You must give the command \protect\addpoints\MessageBreak
      \space\space in order to create a grade table.\MessageBreak
      }{%
      If you don't give the command \protect\addpoints\MessageBreak
      \space\space then we're not keeping track of point values.
      \MessageBreak
      }%
  \fi
}% ii@gtable


\def\@questionsref{questions}
\def\@pagesref{pages}
\def\do@table#1#2{%
  % See whether we're doing a table indexed by
  % questions or by pages:
  \begingroup % avoid trouble from using \@temp
    \def\@temp{#2}%
    \ifx\@temp\@questionsref
      \find@qrange{#1}%
    \else
      \ifx\@temp\@pagesref
        \find@prange{#1}%
      \else
        \ClassError{exam}{%
          The second optional argument to a\MessageBreak
           \space\space  grade table or point table command\MessageBreak 
            \space \space must be either `questions' or
            `pages',\MessageBreak
            \space\space not `#2'.\MessageBreak
        }{%
          Grade tables and point tables can be indexed by questions or
          pages;\MessageBreak
          \space\space for others, you're on your own.\MessageBreak
        }%
        \fbox{Error: grade or point table: Invalid second
                          optional argument `#2'.}%
      \fi
    \fi
  \endgroup
}% do@table


\def\range@undefined{%
  \fbox{Warning: grading range `\tbl@range ' not defined;
                               run \LaTeX{} again.}%
  \ClassWarning{exam}{%
    Grading range `\tbl@range ' not defined.\MessageBreak
    \space\space Run LaTeX again to produce the table.\MessageBreak
  }%
}% range@undefined


%--------------------------------------------------------------------
%--------------------------------------------------------------------
% Grade and point tables indexed by question numbers:

% \find@qrange makes sure the grading range is defined and that
% its last question isn't before its first question.
% \@tblquestions branches, depending on whether the user
% selected [v] or [h].

\def\find@qrange#1{%
  % We're doing a table indexed by question numbers.
  \if@partial
    \@ifundefined{tbl@\tbl@range @firstq}%
      {%
        \range@undefined
      }%
      {%
        \@ifundefined{tbl@\tbl@range @lastq}%
          {%
            \range@undefined
          }%
          {%
            \edef\tbl@firstq{\csname tbl@\tbl@range @firstq\endcsname}%
            \edef\tbl@lastq{\csname tbl@\tbl@range @lastq\endcsname}%
            % Check that firstq precedes or equals lastq:
            \ifnum \tbl@firstq > \tbl@lastq
              \fbox{Error: Grading Range `\tbl@range ':
                      Last question precedes first question.}%
              \ClassError{exam}{%
                In grading range `\tbl@range ',
                                the last question\MessageBreak
                \space\space comes before the first question.\MessageBreak
                }{%
                  \string\begingradingrange \space must precede
                  \string\endgradingrange \space by at
                             least one question.\MessageBreak
                }%
            \else
              \@tblquestions{#1}%
            \fi
          }%
      }%
  \else
    \def\tbl@firstq{1}%
    % \numquestions is always defined, even if this is the first
    % run of LaTeX and \exam@numquestions isn't defined.
    % If it's the first run of LaTeX, then its value isn't useful,
    % but it's never used until a later run (when its value is useful).
    \def\tbl@lastq{\numquestions}%
    \@tblquestions{#1}%
  \fi
}% find@qrange

\def\@tblquestions#1{%
  \if v#1%
    \@vtblquestions
  \else
    \if h#1%
      \@htblquestions
    \else
      \ClassError{exam}{%
        The first optional argument to \protect\gradetable,\MessageBreak
        \space\space \protect\bonusgradetable,
        \protect\pointtable, or\MessageBreak
        \space\space  \protect\bonuspointtable
        \space must be either `h' or `v'\MessageBreak
      }{%
        Grade tables and point tables can be either horizontal or
        vertical;\MessageBreak
        \space\space no diagonals allowed.\MessageBreak
      }%
      \if@scores
        \if@bonus
          \fbox{Error: bonusgradetable: Invalid first optional argument
                                                        `#1'.}%
        \else
          \fbox{Error: gradetable: Invalid first optional argument
                                                        `#1'.}%
        \fi
      \else
        \if@bonus
          \fbox{Error: bonuspointtable: Invalid first optional argument
                                                    `#1'.}%
        \else
          \fbox{Error: pointtable: Invalid first optional argument
                                                    `#1'.}%
        \fi
      \fi
    \fi
  \fi
}% @tblquestions

%--------------------------------------------------------------------
% Vertical, indexed by question numbers:

\def\@vtblquestions{%
  % The table is vertical and indexed by question numbers.
  % See whether it's bonus or non-bonus, and
  % gradetable or pointtable:
  \begingroup
    % Save the current value of question in @iterator, so that
    % we can restore it after doing the table:
    \setcounter{@iterator}{\value{question}}%
    \renewcommand\arraystretch{\@gtblstretch}%
    \if@bonus
      \if@scores
        \@bvgrdtblquestions
      \else
        \@bvpttblquestions
      \fi
    \else
      \if@scores
        \@vgrdtblquestions
      \else
        \@vpttblquestions
      \fi
    \fi
    % Restore the saved value of question:
    \setcounter{question}{\value{@iterator}}%
  \endgroup
}% @vtblquestions

\def\@bvgrdtblquestions{%
  % Vertical bonus gradetable, indexed by questions:
  \set@hlfcntr{tbl@points}{0}%
  \begin{tabular}{|c|c|c|}
    \hline
    {\@bvqword}& {\@bvpword}& {\@bvsword}\\
    \hline
    \setcounter{question}{\tbl@firstq}%
    \addtocounter{question}{-1}\do@bvloop
    {\@bvtword}& \prt@hlfcntr{tbl@points}&\hbox to \@cellwidth{\hfill}\\
    \hline
  \end{tabular}%
}% @bvgrdtblquestions
\def\do@bvloop{%
  % \do@bvloop is used by \@bvgrdtblquestions
  \addtocounter{question}{1}%
  \ref{question@\arabic{question}} &
        \bonuspointsofquestion{\arabic{question}}&\\
  \hline
  \@ifundefined{bonuspointsofq@\romannumeral \c@question}%
    {}%
    {\addto@hlfcntr{tbl@points}
       {\csname bonuspointsofq@\romannumeral \c@question\endcsname}}%
  \ifnum \value{question} < \tbl@lastq\relax
    \let\next@bvloop=\do@bvloop
  \else
    \let\next@bvloop=\relax
  \fi
  \next@bvloop
}% do@bvloop

\def\@bvpttblquestions{%
  % Vertical bonus point table, indexed by questions:
  \set@hlfcntr{tbl@points}{0}%
  \begin{tabular}{|c|c|}
    \hline
    {\@bvqword}& {\@bvpword}\\
    \hline
    \setcounter{question}{\tbl@firstq}%
    \addtocounter{question}{-1}\do@bvptloop
    {\@bvtword}& \prt@hlfcntr{tbl@points}\\
    \hline
  \end{tabular}%
}% @bvpttblquestions
\def\do@bvptloop{%
  % \do@bvptloop is used by \@bvpttblquestions
  \addtocounter{question}{1}%
  \ref{question@\arabic{question}} &
        \bonuspointsofquestion{\arabic{question}}\\
  \hline
  \@ifundefined{bonuspointsofq@\romannumeral \c@question}%
    {}%
    {\addto@hlfcntr{tbl@points}
       {\csname bonuspointsofq@\romannumeral \c@question\endcsname}}%
  \ifnum \value{question} < \tbl@lastq\relax
    \let\next@bvptloop=\do@bvptloop
  \else
    \let\next@bvptloop=\relax
  \fi
  \next@bvptloop
}% do@bvptloop

\def\@vgrdtblquestions{%
  % Vertical non-bonus grade table, indexed by questions:
  \set@hlfcntr{tbl@points}{0}%
  \begin{tabular}{|c|c|c|}
    \hline
    {\@vqword}& {\@vpword}& {\@vsword}\\
    \hline
    \setcounter{question}{\tbl@firstq}%
    \addtocounter{question}{-1}\do@vloop
    {\@vtword}& \prt@hlfcntr{tbl@points}&\hbox to \@cellwidth{\hfill}\\
    \hline
  \end{tabular}%
}% @vgrdtblquestions
\def\do@vloop{%
  % \do@vloop is used by \@vgrdtblquestions
  \addtocounter{question}{1}%
  \ref{question@\arabic{question}} &
        \pointsofquestion{\arabic{question}}&\\
  \hline
  \@ifundefined{pointsofq@\romannumeral \c@question}%
    {}%
    {\addto@hlfcntr{tbl@points}
       {\csname pointsofq@\romannumeral \c@question\endcsname}}%
  \ifnum \value{question} < \tbl@lastq\relax
    \let\next@vloop=\do@vloop
  \else
    \let\next@vloop=\relax
  \fi
  \next@vloop
}% do@vloop

\def\@vpttblquestions{%
  % Vertical non-bonus point table, indexed by questions:
  \set@hlfcntr{tbl@points}{0}%
  \begin{tabular}{|c|c|}
    \hline
    {\@vqword}& {\@vpword}\\
    \hline
    \setcounter{question}{\tbl@firstq}%
    \addtocounter{question}{-1}\do@vptloop
    {\@vtword}& \prt@hlfcntr{tbl@points}\\
    \hline
  \end{tabular}%
}% @vpttblquestions
\def\do@vptloop{%
  % \do@vptloop is used by \@vpttblquestions
  \addtocounter{question}{1}%
  \ref{question@\arabic{question}} &
        \pointsofquestion{\arabic{question}}\\
  \hline
  \@ifundefined{pointsofq@\romannumeral \c@question}%
    {}%
    {\addto@hlfcntr{tbl@points}
       {\csname pointsofq@\romannumeral \c@question\endcsname}}%
  \ifnum \value{question} < \tbl@lastq\relax
    \let\next@vptloop=\do@vptloop
  \else
    \let\next@vptloop=\relax
  \fi
  \next@vptloop
}% do@vptloop


%--------------------------------------------------------------------
% Horizontal, indexed by question numbers:

\def\@htblquestions{%
  % The table is horizontal and indexed by question numbers.
  \@ifundefined{exam@numquestions}%
  {}%
  {%
    \setcounter{num@cols}{\tbl@lastq}%
    \addtocounter{num@cols}{-\tbl@firstq}%
    \addtocounter{num@cols}{1}%
  }%
  % See whether it's bonus or non-bonus, and
  % gradetable or pointtable:
  \begingroup
    % Save the current value of question in @iterator, so that
    % we can restore it after doing the table:
    \setcounter{@iterator}{\value{question}}%
    \renewcommand\arraystretch{\@gtblstretch}%
    \if@bonus
      \set@hlfcntr{tbl@points}{0}%
      \begin{tabular}{|l|*{\thenum@cols}{c|}c|}
        \hline
        {\@bhqword}& \setcounter{question}{\tbl@firstq}%
        \addtocounter{question}{-1}\do@qnumloop
        {\@bhtword}\\
        \hline
        {\@bhpword}& \setcounter{question}{\tbl@firstq}%
        \addtocounter{question}{-1}\do@bptloop
        \prt@hlfcntr{tbl@points}\\
        \hline
        % If it's a grade table, add in the score line:
        \if@scores
          {\@bhsword}& \setcounter{question}{\tbl@firstq}%
          \addtocounter{question}{-1}\do@sloop
          \\
          \hline
        \fi
      \end{tabular}%
    \else
      \set@hlfcntr{tbl@points}{0}%
      \begin{tabular}{|l|*{\thenum@cols}{c|}c|}
        \hline
        {\@hqword}& \setcounter{question}{\tbl@firstq}%
        \addtocounter{question}{-1}\do@qnumloop
        {\@htword}\\
        \hline
        {\@hpword}& \setcounter{question}{\tbl@firstq}%
        \addtocounter{question}{-1}\do@ptloop
        \prt@hlfcntr{tbl@points}\\
        \hline
        % If it's a grade table, add in the score line:
        \if@scores
          {\@hsword}& \setcounter{question}{\tbl@firstq}%
          \addtocounter{question}{-1}\do@sloop
          \\
          \hline
        \fi
      \end{tabular}%
    \fi
    % Restore the saved value of question:
    \setcounter{question}{\value{@iterator}}%
  \endgroup
}% @htblquestions


% \do@qnumloop and \do@sloop are used both by non-bonus gradetable and
% by bonusgradetable:
\def\do@qnumloop{%
  \addtocounter{question}{1}%
  \ref{question@\arabic{question}} &
  \ifnum \value{question} < \tbl@lastq\relax
    \let\next@qnloop=\do@qnumloop
  \else
    \let\next@qnloop=\relax
  \fi
  \next@qnloop
}% do@qnumloop
\def\do@sloop{%
  \addtocounter{question}{1}%
  \hbox to \@cellwidth{\hfill}&
  \ifnum \value{question} < \tbl@lastq\relax
    \let\next@sloop=\do@sloop
  \else
    \let\next@sloop=\relax
  \fi
  \next@sloop
}% do@sloop

%  \do@ptloop is used only by non-bonus gradetable:
\def\do@ptloop{%
  \addtocounter{question}{1}%
  \pointsofquestion{\arabic{question}}&
  \@ifundefined{pointsofq@\romannumeral \c@question}%
    {}%
    {\addto@hlfcntr{tbl@points}
       {\csname pointsofq@\romannumeral \c@question\endcsname}}%
  \ifnum \value{question} < \tbl@lastq\relax
    \let\next@ptloop=\do@ptloop
  \else
    \let\next@ptloop=\relax
  \fi
  \next@ptloop
}% do@ptloop

%  \do@bptloop is used only by bonusgradetable:
\def\do@bptloop{%
  \addtocounter{question}{1}%
  \bonuspointsofquestion{\arabic{question}}&
  \@ifundefined{bonuspointsofq@\romannumeral \c@question}%
    {}%
    {\addto@hlfcntr{tbl@points}
       {\csname bonuspointsofq@\romannumeral \c@question\endcsname}}%
  \ifnum \value{question} < \tbl@lastq\relax
    \let\next@bptloop=\do@bptloop
  \else
    \let\next@bptloop=\relax
  \fi
  \next@bptloop
}% do@bptloop


%--------------------------------------------------------------------
%--------------------------------------------------------------------
% Grade and point tables indexed by page numbers:


% The only pages listed are those on which there is a nonzero number
% of points.  We check pages \tbl@firstp through \tbl@lastp
% Once we've checked that, e.g., \lastpage@withpoints and
% \pointsonpage@\romannumeral{\lastpage@withpoints} are defined, we
% can safely (we think) check \pointsonpage@\romannumeral{n} for all n
% between \tbl@firstp and \tbl@lastp without generating errors.
%
% Actually: Since we added the notion of half points and half counters
% (a long time ago), there won't be any errors even if
% \pointsonpage@\romannumeral{n} isn't defined, since it's tested by the
% lines:
%   \set@hlfcntr{tmp@hlfcntr}{\csname pointsonpage@\romannumeral
%                          \csname c@@iterator\endcsname\endcsname}%
%   \ifhlfcntr@pos{tmp@hlfcntr}%
% and if 
%   \csname pointsonpage@\romannumeral
%             \csname c@@iterator\endcsname\endcsname
% isn't defined, tmp@hlfcntr gets the value zero (because of the way
% that \set@hlfcntr is written).


% \find@prange makes sure the grading range is defined and that
% its last page isn't before its first page.


\def\find@prange#1{%
  % We're doing a table indexed by pages.
  \if@partial
    \@ifundefined{tbl@\tbl@range @firstp}%
      {%
        \range@undefined
      }%
      {%
        \@ifundefined{tbl@\tbl@range @lastp}%
          {%
            \range@undefined
          }%
          {%
            \edef\tbl@firstp{\csname tbl@\tbl@range @firstp\endcsname}%
            \edef\tbl@lastp{\csname tbl@\tbl@range @lastp\endcsname}%
            % Check that firstp precedes or equals lastp:
            \ifnum \tbl@firstp > \tbl@lastp
              \fbox{Error: Grading Range `\tbl@range ':
                      Last page precedes first page.}%
              \ClassError{exam}{%
                In grading range `\tbl@range ', the last page\MessageBreak
                \space\space comes before the first page.\MessageBreak
                }{%
                  \string\begingradingrange \space must precede
                  \string\endgradingrange.\MessageBreak
                }%
            \else
              \@tblpages{#1}%
            \fi
          }%
      }%
  \else
    \def\tbl@firstp{1}%
    % \tbl@lastp isn't used on the first run of LaTeX, and
    % \lastpage@withbonuspoints is defined on the second and later runs.
    \if@bonus
      \def\tbl@lastp{\lastpage@withbonuspoints}%
    \else
      \def\tbl@lastp{\lastpage@withpoints}%
    \fi
    \@tblpages{#1}%
  \fi
}% find@prange



% Check that there's enough info from the .aux file to do a page
% indexed grade table:
\def\@tblpages#1{%
  \@ifundefined{lastpage@withpoints}%
    {\ClassWarning{exam}{%
       You must run LaTeX twice more\MessageBreak
       \space\space to produce the table.\MessageBreak}%
       \fbox{Run \LaTeX{} twice more to produce the table}%
    }%
    {%
      \@ifundefined{pointsonpage@\romannumeral
               \csname lastpage@withpoints\endcsname}%
        {\ClassWarning{exam}{%
           You must run LaTeX again\MessageBreak
           \space\space to produce the table.\MessageBreak}%
           \fbox{Run \LaTeX{} again to produce the table}%
        }%
        {%
          \@whchtblpgs#1
        }%
    }%
}% @tblpages

\def\@whchtblpgs#1{%
  % At this point, we know the table is indexed by pages.
  % It can be vertical or horizontal, 
  % grade or point, and bonus or non-bonus.
  \if v#1%
    \@vtblpages
  \else
    \if h#1%
      \@htblpages
    \else
      \ClassError{exam}{%
        The first optional argument to
          \protect\gradetable,\MessageBreak 
          \space\space \protect\bonusgradetable,
            \protect\pointtable, or\MessageBreak
          \space\space
          \protect\bonuspointtable \space must be either `h' or
          `v'\MessageBreak
      }{%
        Grade tables and point tables can be either horizontal or
        vertical;\MessageBreak
        \space\space no diagonals allowed.\MessageBreak
      }%
      \if@scores
        \if@bonus
          \fbox{Error: bonusgradetable: Invalid first optional argument
                                                  `#1'.}%
        \else
          \fbox{Error: gradetable: Invalid first optional argument
                                                  `#1'.}%
        \fi
      \else
        \if@bonus
          \fbox{Error: bonuspointtable: Invalid first optional argument
                                                  `#1'.}%
        \else
          \fbox{Error: pointtable: Invalid first optional argument
                                                  `#1'.}%
        \fi
      \fi
    \fi
  \fi
}% \@whchtblpgs

%--------------------------------------------------------------------
% Vertical, indexed by pages:

\def\@vtblpages{%
  % At this point, we know it's a vertical table indexed by pages.
  % It can be grade or point, and bonus or non-bonus.
  \begingroup
    \renewcommand\arraystretch{\@gtblstretch}%
    \set@hlfcntr{tbl@points}{0}%
    \if@bonus
      \if@scores
        \begin{tabular}{|c|c|c|}
          \hline
          {\@bvpgword}& {\@bvpword}& {\@bvsword}\\
          \hline
          \setcounter{@iterator}{\tbl@firstp}%
          \addtocounter{@iterator}{-1}\pg@bvloop
          {\@bvtword}& \prt@hlfcntr{tbl@points}&\hbox to \@cellwidth{\hfill}\\
          \hline
        \end{tabular}%
      \else
        \begin{tabular}{|c|c|}
          \hline
          {\@bvpgword}& {\@bvpword}\\
          \hline
          \setcounter{@iterator}{\tbl@firstp}%
          \addtocounter{@iterator}{-1}\pg@ptbvloop
          {\@bvtword}& \prt@hlfcntr{tbl@points}\\
          \hline
        \end{tabular}%
      \fi
    \else
      \if@scores
        \begin{tabular}{|c|c|c|}
          \hline
          {\@vpgword}& {\@vpword}& {\@vsword}\\
          \hline
          \setcounter{@iterator}{\tbl@firstp}%
          \addtocounter{@iterator}{-1}\pg@vloop
          {\@vtword}& \prt@hlfcntr{tbl@points}&\hbox to \@cellwidth{\hfill}\\
          \hline
        \end{tabular}%
      \else
        \begin{tabular}{|c|c|}
          \hline
          {\@vpgword}& {\@vpword}\\
          \hline
          \setcounter{@iterator}{\tbl@firstp}%
          \addtocounter{@iterator}{-1}\pg@ptvloop
          {\@vtword}& \prt@hlfcntr{tbl@points}\\
          \hline
        \end{tabular}%
      \fi
    \fi
  \endgroup
}% @vtblpages


% \pg@ptvloop and \pg@ptvloopline are used only by non-bonus pointtable:
\def\pg@ptvloop{%
  \addtocounter{@iterator}{1}%
  % spanish.ldf redefines \@roman, so we'll avoid using \roman:
  \set@hlfcntr{tmp@hlfcntr}{\csname pointsonpage@\romannumeral
                       \csname c@@iterator\endcsname\endcsname}%
  \ifhlfcntr@pos{tmp@hlfcntr}%
    \add@hlfcntrtohlfcntr{tbl@points}{tmp@hlfcntr}%
    \pg@ptvloopline
  \fi
  \ifnum \the@iterator < \tbl@lastp\relax
    \let\next@pg@ptvloop=\pg@ptvloop
  \else
    \let\next@pg@ptvloop=\relax
  \fi
  \next@pg@ptvloop
}% pg@ptvloop
\def\pg@ptvloopline{%
  % We still don't understand why we need to hide this inside of a
  % macro; there's some weird interaction with the \ifnum checking to
  % see if something is ``>0''; checking that something is ``=0''
  % doesn't cause the ``\ifnum incomplete'' (or whatever) error.
  \pageref{firstpoints@onpage@\arabic{@iterator}} &
                         \pointsonpage{\the@iterator}\\
  \hline
}% pg@ptvloopline

% \pg@vloop and \pg@vloopline are used only by non-bonus gradetable:
\def\pg@vloop{%
  \addtocounter{@iterator}{1}%
  % spanish.ldf redefines \@roman, so we'll avoid using \roman:
  \set@hlfcntr{tmp@hlfcntr}{\csname pointsonpage@\romannumeral
                       \csname c@@iterator\endcsname\endcsname}%
  \ifhlfcntr@pos{tmp@hlfcntr}%
    \add@hlfcntrtohlfcntr{tbl@points}{tmp@hlfcntr}%
    \pg@vloopline
  \fi
  \ifnum \the@iterator < \tbl@lastp\relax
    \let\next@pg@vloop=\pg@vloop
  \else
    \let\next@pg@vloop=\relax
  \fi
  \next@pg@vloop
}% pg@vloop
\def\pg@vloopline{%
  % We still don't understand why we need to hide this inside of a
  % macro; there's some weird interaction with the \ifnum checking to
  % see if something is ``>0''; checking that something is ``=0''
  % doesn't cause the ``\ifnum incomplete'' (or whatever) error.
  \pageref{firstpoints@onpage@\arabic{@iterator}} &
                         \pointsonpage{\the@iterator}&\\
  \hline
}% pg@vloopline

% \pg@bvloop and \pg@bvloopline are used only by bonus gradetable:
\def\pg@bvloop{%
  \addtocounter{@iterator}{1}%
  % spanish.ldf redefines \@roman, so we'll avoid using \roman:
  \set@hlfcntr{tmp@hlfcntr}{\csname bonuspointsonpage@\romannumeral
                          \csname c@@iterator\endcsname\endcsname}%
  \ifhlfcntr@pos{tmp@hlfcntr}%
    \add@hlfcntrtohlfcntr{tbl@points}{tmp@hlfcntr}%
    \pg@bvloopline
  \fi
  \ifnum \the@iterator < \tbl@lastp\relax
    \let\next@pg@bvloop=\pg@bvloop
  \else
    \let\next@pg@bvloop=\relax
  \fi
  \next@pg@bvloop
}% pg@bvloop
\def\pg@bvloopline{%
  % We still don't understand why we need to hide this inside of a
  % macro; there's some weird interaction with the \ifnum checking to
  % see if something is ``>0''; checking that something is ``=0''
  % doesn't cause the ``\ifnum incomplete'' (or whatever) error.
  \pageref{firstbonuspoints@onpage@\arabic{@iterator}} &
                         \bonuspointsonpage{\the@iterator}&\\
  \hline
}% pg@bvloopline

% \pg@ptbvloop and \pg@ptbvloopline are used only by bonus pointtable:
\def\pg@ptbvloop{%
  \addtocounter{@iterator}{1}%
  % spanish.ldf redefines \@roman, so we'll avoid using \roman:
  \set@hlfcntr{tmp@hlfcntr}{\csname bonuspointsonpage@\romannumeral
                          \csname c@@iterator\endcsname\endcsname}%
  \ifhlfcntr@pos{tmp@hlfcntr}%
    \add@hlfcntrtohlfcntr{tbl@points}{tmp@hlfcntr}%
    \pg@ptbvloopline
  \fi
  \ifnum \the@iterator < \tbl@lastp\relax
    \let\next@pg@ptbvloop=\pg@ptbvloop
  \else
    \let\next@pg@ptbvloop=\relax
  \fi
  \next@pg@ptbvloop
}% pg@ptbvloop
\def\pg@ptbvloopline{%
  % We still don't understand why we need to hide this inside of a
  % macro; there's some weird interaction with the \ifnum checking to
  % see if something is ``>0''; checking that something is ``=0''
  % doesn't cause the ``\ifnum incomplete'' (or whatever) error.
  \pageref{firstbonuspoints@onpage@\arabic{@iterator}} &
                         \bonuspointsonpage{\the@iterator}\\
  \hline
}% pg@ptbvloopline

%--------------------------------------------------------------------
% Horizontal, indexed by pages:

% For a horizontal table, before we begin we need to know how many
% pages there are with points on them:
\newcounter{num@cols}
\def\count@pgswpts{%
  % \count@pgswpts is used for horizontal
  % grade tables and point tables, both
  % bonus and non-bonus.
  \setcounter{num@cols}{0}%
  \setcounter{@iterator}{\tbl@firstp}%
  \addtocounter{@iterator}{-1}%
  \if@bonus
    \docount@pgswbpts
  \else
    \docount@pgswpts
  \fi
}% count@pgswpts

% \docount@pgswpts is used for non-bonus gradetable:
\def\docount@pgswpts{%
  \addtocounter{@iterator}{1}%
  % spanish.ldf redefines \@roman, so we'll avoid using \roman:
  \set@hlfcntr{tmp@hlfcntr}{\csname pointsonpage@\romannumeral
                         \csname c@@iterator\endcsname\endcsname}%
  \ifhlfcntr@pos{tmp@hlfcntr}%
    \addtocounter{num@cols}{1}%
  \fi
  \ifnum \the@iterator < \tbl@lastp\relax
    \let\next@docount=\docount@pgswpts
  \else
    \let\next@docount=\relax
  \fi
  \next@docount
}% docount@pgswpts

% \docount@pgswbpts is used for bonusgradetable:
\def\docount@pgswbpts{%
  \addtocounter{@iterator}{1}%
  % spanish.ldf redefines \@roman, so we'll avoid using \roman:
  \set@hlfcntr{tmp@hlfcntr}{\csname bonuspointsonpage@\romannumeral
                           \csname c@@iterator\endcsname\endcsname}%
  \ifhlfcntr@pos{tmp@hlfcntr}%
    \addtocounter{num@cols}{1}%
  \fi
  \ifnum \the@iterator < \tbl@lastp\relax
    \let\next@docount=\docount@pgswbpts
  \else
    \let\next@docount=\relax
  \fi
  \next@docount
}% docount@pgswbpts

%--------------------------------------------------------------------

\def\@htblpages{%
  \begingroup
    \renewcommand\arraystretch{\@gtblstretch}%
    \count@pgswpts
    % Suppress ``extra alignment tab'' errors if \thenum@cols = 0:
    \ifnum \thenum@cols = 0
      \setcounter{num@cols}{1}%
    \fi
    \set@hlfcntr{tbl@points}{0}%
    \if@bonus
      \begin{tabular}{|l|*{\thenum@cols}{c|}c|}
        \hline
        {\@bhpgword}& \setcounter{@iterator}{\tbl@firstp}%
                      \addtocounter{@iterator}{-1}\do@bpgnumloop
        {\@bhtword}\\
        \hline
        {\@bhpword}& \setcounter{@iterator}{\tbl@firstp}%
                     \addtocounter{@iterator}{-1}\do@bpgptloop
        \prt@hlfcntr{tbl@points}\\
        \hline
        % If it's a grade table, do the line for scores:
        \if@scores
          {\@bhsword}& \setcounter{@iterator}{\tbl@firstp}%
                       \addtocounter{@iterator}{-1}\do@bpgsloop
          \\
          \hline
        \fi
      \end{tabular}%
    \else
      \begin{tabular}{|l|*{\thenum@cols}{c|}c|}
        \hline
        {\@hpgword}& \setcounter{@iterator}{\tbl@firstp}%
                     \addtocounter{@iterator}{-1}\do@pgnumloop
        {\@htword}\\
        \hline
        {\@hpword}& \setcounter{@iterator}{\tbl@firstp}%
                    \addtocounter{@iterator}{-1}\do@pgptloop
        \prt@hlfcntr{tbl@points}\\
        \hline
        % If it's a grade table, do the line for scores:
        \if@scores
          {\@hsword}& \setcounter{@iterator}{\tbl@firstp}%
                      \addtocounter{@iterator}{-1}\do@pgsloop
          \\
          \hline
        \fi
      \end{tabular}%
    \fi
  \endgroup
}% @htblpages

% \do@pgnumloop, \pg@line, \do@pgptloop, \pgpt@line, \do@pgsloop, and
% \pg@sline are only for non-bonus gradetable:
\def\do@pgnumloop{%
  \addtocounter{@iterator}{1}%
  % spanish.ldf redefines \@roman, so we'll avoid using \roman:
  \set@hlfcntr{tmp@hlfcntr}{\csname pointsonpage@\romannumeral
                        \csname c@@iterator\endcsname\endcsname}%
  \ifhlfcntr@pos{tmp@hlfcntr}%
    \pg@line
  \fi
  \ifnum \the@iterator < \tbl@lastp\relax
    \let\next@pgnumloop=\do@pgnumloop
  \else
    \let\next@pgnumloop=\relax
  \fi
  \next@pgnumloop
}% \do@pgnumloop
\def\pg@line{%
  \pageref{firstpoints@onpage@\arabic{@iterator}}&
}% \pg@line

\def\do@pgptloop{%
  \addtocounter{@iterator}{1}%
  % spanish.ldf redefines \@roman, so we'll avoid using \roman:
  \set@hlfcntr{tmp@hlfcntr}{\csname pointsonpage@\romannumeral
                        \csname c@@iterator\endcsname\endcsname}%
  \ifhlfcntr@pos{tmp@hlfcntr}%
    \add@hlfcntrtohlfcntr{tbl@points}{tmp@hlfcntr}%
    \pgpt@line
  \fi
  \ifnum \the@iterator < \tbl@lastp\relax
    \let\next@pgptloop=\do@pgptloop
  \else
    \let\next@pgptloop=\relax
  \fi
  \next@pgptloop
}% \do@pgptloop
\def\pgpt@line{%
  % spanish.ldf redefines \@roman, so we'll avoid using \roman:
  \csname pointsonpage@\romannumeral
        \csname c@@iterator\endcsname\endcsname &
}% \pgpt@line

\def\do@pgsloop{%
  \addtocounter{@iterator}{1}%
  % spanish.ldf redefines \@roman, so we'll avoid using \roman:
  \set@hlfcntr{tmp@hlfcntr}{\csname pointsonpage@\romannumeral
                         \csname c@@iterator\endcsname\endcsname}%
  \ifhlfcntr@pos{tmp@hlfcntr}%
    \add@hlfcntrtohlfcntr{tbl@points}{tmp@hlfcntr}%
    \pg@sline
  \fi
  \ifnum \the@iterator < \tbl@lastp\relax
    \let\next@pgsloop=\do@pgsloop
  \else
    \let\next@pgsloop=\relax
  \fi
  \next@pgsloop
}% \do@pgsloop
\def\pg@sline{%
  \hbox to \@cellwidth{\hfill}&
}% \pg@sline

%--------------------------------------------------------------------
% These things are for bonusgradetable:

% \do@bpgnumloop, \bpg@line, \do@bpgptloop, \bpgpt@line, \do@bpgsloop,
% and \bpg@sline are only for bonusgradetable:
\def\do@bpgnumloop{%
  \addtocounter{@iterator}{1}%
  % spanish.ldf redefines \@roman, so we'll avoid using \roman:
  \set@hlfcntr{tmp@hlfcntr}{\csname bonuspointsonpage@\romannumeral
                          \csname c@@iterator\endcsname\endcsname}%
  \ifhlfcntr@pos{tmp@hlfcntr}%
    \bpg@line
  \fi
  \ifnum \the@iterator < \tbl@lastp\relax
    \let\next@bpgnumloop=\do@bpgnumloop
  \else
    \let\next@bpgnumloop=\relax
  \fi
  \next@bpgnumloop
}% do@bpgnumloop
\def\bpg@line{%
  \pageref{firstbonuspoints@onpage@\arabic{@iterator}}&
}% bpg@line

\def\do@bpgptloop{%
  \addtocounter{@iterator}{1}%
  % spanish.ldf redefines \@roman, so we'll avoid using \roman:
  \set@hlfcntr{tmp@hlfcntr}{\csname bonuspointsonpage@\romannumeral
                            \csname c@@iterator\endcsname\endcsname}%
  \ifhlfcntr@pos{tmp@hlfcntr}%
    \add@hlfcntrtohlfcntr{tbl@points}{tmp@hlfcntr}%
    \bpgpt@line
  \fi
  \ifnum \the@iterator < \tbl@lastp\relax
    \let\next@bpgptloop=\do@bpgptloop
  \else
    \let\next@bpgptloop=\relax
  \fi
  \next@bpgptloop
}% do@bpgptloop
\def\bpgpt@line{%
  % spanish.ldf redefines \@roman, so we'll avoid using \roman:
  \csname bonuspointsonpage@\romannumeral
                       \csname c@@iterator\endcsname\endcsname &
}% bpgpt@line

\def\do@bpgsloop{%
  \addtocounter{@iterator}{1}%
  % spanish.ldf redefines \@roman, so we'll avoid using \roman:
  \set@hlfcntr{tmp@hlfcntr}{\csname bonuspointsonpage@\romannumeral
                          \csname c@@iterator\endcsname\endcsname}%
  \ifhlfcntr@pos{tmp@hlfcntr}%
    \add@hlfcntrtohlfcntr{tbl@points}{tmp@hlfcntr}%
    \bpg@sline
  \fi
  \ifnum \the@iterator < \tbl@lastp\relax
    \let\next@bpgsloop=\do@bpgsloop
  \else
    \let\next@bpgsloop=\relax
  \fi
  \next@bpgsloop
}% do@bpgsloop
\def\bpg@sline{%
  \hbox to \@cellwidth{\hfill}&
}% bpg@sline


%--------------------------------------------------------------------
%--------------------------------------------------------------------
%
%                     ***************************
%                     ** SOLUTION ENVIRONMENTS **
%                     ***************************



% If the documentclass options include ``answers'', then the command
% \printanswerstrue is given at the beginning of the run.

% If the documentclass options include ``noanswers'', then the command
% \printanswersfalse is given at the beginning of the run.

\def\printanswers{\printanswerstrue}
\def\noprintanswers{\printanswersfalse}


% If printanswers is true, we print the solution using a TheSolution
% environment.  If printanswers is false, we insert blank vertical
% space equal to the optional argument (the default value of which is
% 0pt).
\newenvironment{solution}[1][0pt]%
  {%
    \ifprintanswers
      \begin{TheSolution}%
    \else
      \par
      \vspace*{#1}%
      \setbox\z@\vbox\bgroup
    \fi
  }{%
    \ifprintanswers
      \end{TheSolution}%
    \else
      \egroup
    \fi
  }%

% If printanswers is true, we print the solution using a TheSolution
% environment.  If printanswers is false, we insert lined vertical
% space equal to the optional argument (the default value of which is
% 0pt).
\newenvironment{solutionorlines}[1][0pt]%
  {%
    \ifprintanswers
      \begin{TheSolution}%
    \else
      \par
      \fillwithlines{#1}%
      \setbox\z@\vbox\bgroup
    \fi
  }{%
    \ifprintanswers
      \end{TheSolution}%
    \else
      \egroup
    \fi
  }%

  
% If printanswers is true, we print the solution using a TheSolution
% environment.  If printanswers is false, we insert dotted lined
% vertical space equal to the optional argument (the default value of
% which is 0pt).
\newenvironment{solutionordottedlines}[1][0pt]%
  {%
    \ifprintanswers
      \begin{TheSolution}%
    \else
      \par
      \fillwithdottedlines{#1}%
      \setbox\z@\vbox\bgroup
    \fi
  }{%
    \ifprintanswers
      \end{TheSolution}%
    \else
      \egroup
    \fi
  }%

  
% The environment TheSolution is called from the solution,
% solutionorlines, and solutionordottedlines environments
% when printanswers is true.  It uses Donald Arseneau's
% framed.sty macros (included at the end if this file) to allow the
% solution to be broken across pages and have each piece enclosed in
% an fbox (or a colorbox, if the user has given the command
% \shadedsolutions).
%
% Of course, the user can change TheSolution with a \renewenvironment
% command.
\newcommand{\solutiontitle}{\noindent\textbf{Solution:}\enspace}
\newenvironment{TheSolution}%
  {%
    \vspace{\parskip}%
    % If we don't set \leftskip and \rightskip to 0pt, then if we
    % appear inside of an \uplevel command we'd have indentation
    % inside of the solution box:
    \leftskip=0pt
    \rightskip=0pt
    \if@framedsolutions
      % Do nothing; we'll use the default \FrameCommand
    \else
      \def\FrameCommand{\colorbox{SolutionColor}}%
    \fi
    \MakeFramed{\advance\hsize-\width}%
    \solutiontitle
    \ignorespaces
  }%
  {%
    \unskip
    \endMakeFramed
  }%

\newif\if@framedsolutions
\@framedsolutionstrue

\def\framedsolutions{\@framedsolutionstrue}
\def\shadedsolutions{%
  \@ifundefined{definecolor}
  {%
    \ClassError{exam}{%
      You must load the color package with the command\MessageBreak
      \space\space\protect\usepackage{color}\MessageBreak
      in order to use the command \protect\shadedsolutions
      \MessageBreak
      }{%
      This command makes use of the package color.sty,\MessageBreak
      and so you have to load color.sty before your\MessageBreak
      \protect\begin{document} command.\MessageBreak
      }%
  }%
  {%
    \definecolor{SolutionColor}{gray}{0.8}
    \@framedsolutionsfalse
  }%
}

%--------------------------------------------------------------------
%--------------------------------------------------------------------

% The following stuff is lifted from:
%
% framed.sty   v 0.8a   21-Jul-2003
% Copyright (C) 1992-2003 by Donald Arseneau
% These macros may be freely transmitted, reproduced, or modified
% provided that this notice is left intact.
%
% The modifications I made are marked with ``psh'' in a comment:
% 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Create framed or shaded regions that can break across pages using 
% \begin{framed} ... \end{framed}    -- ordinary frame box (box at margin)
% \begin{shaded} ... \end{shaded}    -- shaded background (into margin)
%    ... leftbar ...                 -- line on left side
% \begin{MakeFramed}{settings} ... \end{MakeFramed}
%                        -- generic frame (for new environments)
%
% The "framed" environment puts the text into "\fbox" with the
% settings "\fboxrule=\FrameRule" and "\fboxsep=\FrameSep".
% You can change these lengths (using "\setlength") and you
% can even change the definition of "\FrameCommand" to use
% much fancier boxes.
%
% In fact, the "shaded" environment just redefines "\FrameCommand"
% to use "\colorbox{shadecolor}" (and you have to define the
% color "shadecolor": \newcolor{shadecolor}...).
%
% A page break is allowed, and even encouraged, before the framed
% environment.  If you want to attach some text (a box title) to the
% frame, then the text should be inserted by \FrameCommand
%
% The contents of the framed regions are restricted: 
% Floats, footnotes, marginpars and head-line entries will be lost.
% (Some of these may be handled in a later version.)
% This package will not work with the page breaking of multicol.sty,
% or other systems that perform column-balancing.
%
% The MakeFramed environment does the work.  Its "settings" argument
% should contain any adjustments to the text width (applied to \hsize,
% and using the "\width" of the frame itself) as well as a `restore' 
% command -- \@parboxrestore or \FrameRestore or something similar.
% 
% Expert commands:
% \MakeFramed, \endMakeFramed: the "MakeFramed" environment
% \FrameCommand: command to draw the frame around its argument
% \FrameRestore: restore some text settings, but fewer than \@parboxrestore
% \FrameRule: length register; \fboxrule for default "framed".
% \FrameSep: length register; \fboxsep for default "framed".
% \FrameHeightAdjust: macro; height of frame above baseline at top of page
% 
% This is still a `pre-production' version because I can think of many
% features/improvements that should be made.  Nevertheless, starting 
% with version 0.5 it should be bug-free.
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%psh: Commented out \ProvidesPackage:
%\ProvidesPackage{framed}[2003/07/21 v 0.8a: 
%   framed or shaded text with page breaks]

%psh: Created \saved@totalleftmargin and \@sollistdepth:
\newdimen\saved@totalleftmargin
\newcount\@sollistdepth

\newenvironment{framed}% using default \FrameCommand
  {\MakeFramed {\advance\hsize-\width \FrameRestore}}%
  {\endMakeFramed}

\newenvironment{shaded}{%
  \def\FrameCommand{\colorbox{shadecolor}}%
  \MakeFramed {\FrameRestore}}%
 {\endMakeFramed}

\newenvironment{leftbar}{%
  \def\FrameCommand{\vrule width 3pt \hspace{10pt}}%
  \MakeFramed {\advance\hsize-\width \FrameRestore}}%
 {\endMakeFramed}

\chardef\FrameRestore=\catcode`\| % for debug
\catcode`\|=\catcode`\% % (debug: insert space after backslash)

\def\MakeFramed#1{\par
 % measure added width and height; call result \width and \height
 \setbox\z@\vbox{\vskip-1in \hbox{\hskip-1in 
   \FrameCommand{\hbox{\vrule \@height .7in \@depth.3in \@width 1in}}}%
   \vskip\z@skip}%
 \def\width{\wd\z@}\def\height{\ht\z@}%
 \edef\fb@frw{\the\width}\edef\fb@frh{\the\height}%
 % insert pre-penalties and skips
 \begingroup
 \skip@\lastskip
 \if@nobreak\else 
    \penalty9999 % updates \page parameters
    \ifdim\pagefilstretch=\z@ \ifdim\pagefillstretch=\z@
       \edef\@tempa{\the\skip@}%
       \ifx\@tempa\zero@glue \penalty-30
       \else \vskip-\skip@ \penalty-30 \vskip\skip@
    \fi\fi\fi
    \penalty\z@
    % Give a stretchy breakpoint that will always be taken in preference
    % to the \penalty 9999 used to update page parameters.  The cube root
    % of 10000/100 indicates a multiplier of 0.21545, but the maximum 
    % calculated badness is really 8192, not 10000, so the multiplier
    % is 0.2301. 
    \advance\skip@ \z@ plus-.5\baselineskip
    \advance\skip@ \z@ plus-.231\height
    \advance\skip@ \z@ plus-.231\skip@
    \advance\skip@ \z@ plus-.231\topsep
    \vskip-\skip@ \penalty 1800 \vskip\skip@
 \fi
 \addvspace{\topsep}%
 \endgroup
 % clear out pending page break
 \penalty\@M \vskip 2\baselineskip \vskip\height
 \penalty9999 \vskip -2\baselineskip \vskip-\height
 \penalty9999 % updates \pagetotal
|\message{After clearout, \pagetotal=\the\pagetotal, \pagegoal=\the\pagegoal. }%
 \fb@adjheight 
%psh: Added commands:
  \advance\hsize-\@totalleftmargin
  \saved@totalleftmargin=\@totalleftmargin
  \@totalleftmargin=0pt
  \parshape 0
  \let\@listdepth=\@sollistdepth
  \@sollistdepth=0
  \leftmargin=0pt
%psh: end of added commands
 \setbox\@tempboxa\vbox\bgroup
   #1% Modifications to \hsize (can use \width and \height)
   \textwidth\hsize \columnwidth\hsize
%psh: added one line:
   \linewidth=\hsize
}

\def\endMakeFramed{\par
     \kern\z@ \penalty-100 % put depth into height
 \egroup
 \begingroup \put@frame \endgroup
%psh: Added one line:
 \@totalleftmargin=\saved@totalleftmargin
}

% \put@frame takes the contents of \@tempboxa and puts all, or a piece,
% of it on the page with a frame (\FrameCommand).  It recurses until
% all of \@tempboxa has been used up. (\@tempboxa must have zero depth.)

\def\put@frame{\relax
 \ifdim\pagegoal=\maxdimen \pagegoal\vsize \fi
|   \message{=============== Entering putframe ====================^^J
|     \pagegoal=\the\pagegoal,  \pagetotal=\the\pagetotal. }%
 \ifinner \else
    \dimen@\pagegoal \advance\dimen@-\pagetotal % natural space left on page
  \ifdim\dimen@<2\baselineskip 
|   \message{Page has only \the\dimen@\space room left; eject. }%
    \eject \fb@adjheight \put@frame
  \else % there's appreciable room left on the page
|    \message{\string\pagetotal=\the\pagetotal,
|        \string\pagegoal=\the\pagegoal, 
|        \string\pagestretch=\the\pagestretch,
|        \string\pageshrink=\the\pageshrink,
|        \string\fb@frh=\fb@frh. \space}
|    \message{Box of size \the\ht\@tempboxa\space + \fb@frh}%
     \begingroup % temporarily set \dimen@ to be...
     \advance\dimen@.8\pageshrink  % maximum space available on page
     \advance\dimen@-\fb@frh\relax % space available for frame's contents
     \expandafter\endgroup
     % restore \dimen@ to real room left on page
     \ifdim\dimen@>\ht\@tempboxa % whole box does fit
|       \message{fits in \the\dimen@. }%
     \else % box must be split
|       \message{must be split to fit in \the\dimen@. }%
        \setbox\@tempboxa\vbox{% simulate frame and flexiblity of the page:
           \vskip \fb@frh \@plus\pagestretch \@minus.8\pageshrink
           \kern137sp\kern-137sp\penalty-30
           \unvbox\@tempboxa}%
        \edef\fb@resto@set{\boxmaxdepth\the\boxmaxdepth \splittopskip\the\splittopskip}%
        \boxmaxdepth\z@ \splittopskip\z@
        \setbox\tw@\vsplit\@tempboxa to\dimen@
        \setbox\tw@\vbox{\unvbox\tw@}% natural-sized
|       \message{Box of size \the\ht\@tempboxa\space split to \the\dimen@. 
|          Natural height of split box is \the\ht\tw@. }%
        % If the split-to size > (\vsize-\topskip), then set box to full size
        \begingroup
          \advance\dimen@\topskip
          \expandafter\endgroup
        \ifdim\dimen@>\pagegoal
|         \message{Frame is big -- Use up the full column. }%
          \dimen@ii\pagegoal
          \advance\dimen@ii -\topskip
          \advance\dimen@ii \FrameHeightAdjust\relax
        \else  % suspect this is wrong:
          % If the split-to size > feasible room_on_page, rebox it smaller.
          \advance\dimen@.8\pageshrink
          \ifdim\ht\tw@>\dimen@
|           \message{Box too tall; rebox it to \the\dimen@. }%
            \dimen@ii\dimen@
          \else % use natural size
            \dimen@ii\ht\tw@
          \fi
        \fi
        % Re-box contents to desired size \dimen@ii
        \advance\dimen@ii -\fb@frh
        \setbox\tw@\vbox to\dimen@ii \bgroup
        % remove simulated frame and page flexibility:
        \vskip -\fb@frh \@plus-\pagestretch \@minus-.8\pageshrink
        \unvbox\tw@ \unpenalty\unpenalty
        \ifdim\lastkern=-137sp % whole box went to next page
|          \message{box split at beginning! }%
           \egroup \fb@resto@set \eject % (\vskip for frame size was discarded) 
           \fb@adjheight
        \else %
           \egroup \fb@resto@set
           \ifvoid\@tempboxa % it all fit after all
|             \message{box split at end! }%
              \setbox\@tempboxa\box\tw@
           \else % it really did split
|             \message{box split as expected. Its reboxed height is \the\ht\tw@. }%
              \ifdim\wd\tw@>\z@
%psh: Changed the command that inserts the box:
%     Instead of \centerline, we shift right by \saved@totalleftmargin:
%              \centerline{\FrameCommand{\box\tw@}}%  ??? \centerline bad idea
       \hbox{\hskip \saved@totalleftmargin\FrameCommand{\box\tw@}}%
              \else
|               \message{Zero width means likely blank. Don't frame it (guess)}%
                \box\tw@
              \fi
              \hrule \@height\z@
              \eject
              \fb@adjheight
              \put@frame
  \fi\fi\fi\fi\fi
  \ifvoid\@tempboxa\else
%psh: Changed the command that inserts the box:
%     Instead of \centerline, we shift right by \saved@totalleftmargin:
%    \centerline{\FrameCommand{\box\@tempboxa}}%
    \hbox{\hskip\saved@totalleftmargin\FrameCommand{\box\@tempboxa}}%
    \nointerlineskip \null %{\showoutput \showlists}
    \penalty-30 \vskip\topsep
  \fi}

\def\fb@adjheight{%
  \vbox to\FrameHeightAdjust{}% get proper baseline skip from above.
  \penalty\@M \nointerlineskip
  \vskip-\FrameHeightAdjust
  \penalty\@M} % useful for tops of pages

\edef\zero@glue{\the\z@skip}

\catcode`\|=\FrameRestore

% Provide configuration commands:
\providecommand\FrameCommand{\fboxrule=\FrameRule \fboxsep=\FrameSep \fbox}
\@ifundefined{FrameRule}{\newdimen\FrameRule \FrameRule=\fboxrule}{}
\@ifundefined{FrameSep} {\newdimen\FrameSep  \FrameSep =3\fboxsep}{}

% Height of frame above first baseline when frame starts a page:
\providecommand\FrameHeightAdjust{6pt}

% \FrameRestore has parts of \@parboxrestore.  See how it is used in the 
% "settings" argument of \MakeFrame.  Previous behavior can be restored by 
% using \@parboxrestore there, or redefining:
% \makeatletter \renewcommand\FrameRestore{\@parboxrestore} \makeatother
\def\FrameRestore{%
  \let\if@nobreak\iffalse
  \let\if@noskipsec\iffalse
%  \let\par\@@par  ??
  \let\-\@dischyph
  \let\'\@acci\let\`\@accii\let\=\@acciii
%  \parindent\z@ \parskip\z@skip    Definitely omit!
%  \everypar{}%  ??
  \linewidth\hsize
%  \@totalleftmargin\z@
%  \leftskip\z@skip \rightskip\z@skip \@rightskip\z@skip
%  \parfillskip\@flushglue \lineskip\normallineskip
%  \baselineskip\normalbaselineskip
  \sloppy
%  \let\\\@normalcr
}

%  Compatibility with previous versions (temporary!):
\let\fram@d=\MakeFramed  \let\endfram@d=\endMakeFramed

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% This ends the stuff that's lifted from:
% % framed.sty   v 0.8a   21-Jul-2003
% % Copyright (C) 1992-2003 by Donald Arseneau


%--------------------------------------------------------------------
%--------------------------------------------------------------------

\endinput
%---------------------------------------------------------------------
%---------------------------------------------------------------------
%---------------------------------------------------------------------
%---------------------------------------------------------------------
%---------------------------------------------------------------------
