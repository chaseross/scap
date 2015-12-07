\NeedsTeXFormat{LaTeX2e}[1994/06/01]

\ProvidesClass{tufte-handout2}[2010/03/28 v3.5.1 Tufte-handout class]

%%
% Declare we're tufte-handout
\newcommand{\@tufte@class}{article}% the base LaTeX class (defaults to the article/handout style)
\newcommand{\@tufte@pkgname}{tufte-handout}% the name of the package (defaults to tufte-handout)

%%
% Load the common style elements
\input{tufte-common2.def}


%%
% Set up any handout-specific stuff now

%%
% Abstract

% TODO The abstract should be printed on its own page of the `titlepage'
% option was specified.
\renewenvironment{abstract}
  {\begin{quotation}\if@tufte@sfsidenotes\begin{sffamily}\fi}
  {\if@tufte@sfsidenotes\end{sffamily}\fi\end{quotation}}
  
\usepackage{lmodern}

\renewcommand{\familydefault}{\sfdefault}

\usepackage{longtable}
\usepackage{booktabs} % book-quality tables
\usepackage{amsmath} % extended mathematics
\usepackage{enumitem}
\usepackage{units} % non-stacked fractions and better unit s%pacing
\usepackage{multicol} % multiple column layout facilities
\usepackage{lipsum} % filler text
\usepackage{fancyvrb} % extended verbatim environments
\usepackage{graphicx} % allow embedded images
\usepackage[parfill]{parskip}
%\setlength{\parindent}{0pt}
%\setlength{\parskip}{\baselineskip}
 \setkeys{Gin}{width=\linewidth,totalheight=\textheight,keepaspectratio}




 \fvset{fontsize=\normalsize}% default font size for fancy-verbatim environments

%%
% If there is a `tufte-handout-local.tex' file, load it.

\IfFileExists{tufte-handout-local.tex}{%
  \input{tufte-handout-local}%
  \@tufte@info@noline{Loading tufte-handout-local.tex}%
}{}


%%
% End of file
\endinput
