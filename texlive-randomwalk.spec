%global tl_name randomwalk
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.6
Release:	%{tl_revision}.1
Summary:	Random walks using TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/randomwalk
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/randomwalk.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/randomwalk.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/randomwalk.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The randomwalk package provides a user command, \RandomWalk, to draw
random walks with a given number of steps. Lengths and angles of the
steps can be customized in various ways. The package uses lcg for its
'random' numbers and PGF/TikZ for its graphical output.

