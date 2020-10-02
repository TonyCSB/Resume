\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{resume}[Tony's Resume]
\LoadClass[12pt]{article}

\setlength{\parindent}{0pt}

\RequirePackage{titlesec}
\RequirePackage{hyperref}
\hypersetup{hidelinks}
\RequirePackage{url}
\urlstyle{tt}
\RequirePackage{fontawesome}
\RequirePackage{changepage}

\usepackage{mathptmx}

\RequirePackage[
	letterpaper,
	left=1in,
	right=1in,
	top=1in,
	bottom=1in,
	nohead
]{geometry}

%\titlespacing*{\section} {0pt}{2.5ex plus 1ex minus .2ex}{1.3ex plus .2ex}
\titlespacing*{\subsection} {0pt}{2.25ex plus 1ex minus .2ex}{0.5ex plus .2ex}

\titleformat{\section}
    {\Large\scshape\raggedright\bfseries}
    {}{0em}
    {}
    [\titlerule]

\titleformat{\subsection}
    {\large\scshape\raggedright\bfseries}
    {}{0em}
    {}

\newcommand{\datedsection}[2]{%
    \section[#1]{#1 \hfill #2}%
}

\newcommand{\datedsubsection}[2]{%
    \subsection[#1]{#1 \hfill {\normalsize{\textnormal{#2}}}}%
}

\newcommand{\name}[1]{%
    \centerline{\Huge{#1}\vspace{.25in}}
}

\newcommand{\email}[1]{\faEnvelope\ \href{mailto:#1}{#1}}

\newcommand{\phone}[1]{\faPhone\ {#1}}

\newcommand{\linkedin}[2]{\faLinkedin\ \href{#2}{#1}}

\newcommand{\github}[2]{\faGithub\ \href{#2}{#1}}

\newcommand{\basicInfo}[1]{
  \centerline{#1}
}

\newcommand{\role}[2]{
  {\par \textit{#1} ~ #2 \par}
}

\newenvironment{jobitemize}{\vspace{-1.25\topsep}\begin{itemize}\setlength\itemsep{-0.25em}}{\end{itemize}}
\newenvironment{myitemize}{\begin{itemize}\setlength\itemsep{0em}}{\end{itemize}}
\newenvironment{ind}{\begin{adjustwidth}{4ex}{}}{\end{adjustwidth}}