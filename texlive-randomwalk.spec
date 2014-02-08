# revision 27517
# category Package
# catalog-ctan /macros/latex/contrib/randomwalk
# catalog-date 2012-08-24 11:37:59 +0200
# catalog-license lppl
# catalog-version 0.2b
Name:		texlive-randomwalk
Version:	0.2b
Release:	2
Summary:	Random walks using TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/randomwalk
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/randomwalk.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/randomwalk.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/randomwalk.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The randomwalk package provides a user command, \RandomWalk, to
draw random walks with a given number of steps. Lengths and
angles of the steps can be customized in various ways. The
package uses PGF/TikZ for its graphical output.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/randomwalk/randomwalk.sty
%doc %{_texmfdistdir}/doc/latex/randomwalk/README
%doc %{_texmfdistdir}/doc/latex/randomwalk/randomwalk.pdf
#- source
%doc %{_texmfdistdir}/source/latex/randomwalk/randomwalk.dtx
%doc %{_texmfdistdir}/source/latex/randomwalk/randomwalk.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Oct 30 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.2b-1
+ Revision: 820800
- Update to latest release.

* Wed Aug 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.2-3
+ Revision: 812814
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.2-2
+ Revision: 755575
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.2-1
+ Revision: 719429
- texlive-randomwalk
- texlive-randomwalk
- texlive-randomwalk
- texlive-randomwalk

