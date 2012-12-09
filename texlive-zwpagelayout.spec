# revision 26549
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-zwpagelayout
Version:	20120809
Release:	1
Summary:	TeXLive zwpagelayout package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zwpagelayout.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zwpagelayout.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive zwpagelayout package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/zwpagelayout/zwpagelayout.sty
%doc %{_texmfdistdir}/doc/latex/zwpagelayout/License.txt
%doc %{_texmfdistdir}/doc/latex/zwpagelayout/LoremIpsumDolor.tex
%doc %{_texmfdistdir}/doc/latex/zwpagelayout/README
%doc %{_texmfdistdir}/doc/latex/zwpagelayout/adjustfoot.pdf
%doc %{_texmfdistdir}/doc/latex/zwpagelayout/adjustfoot.tex
%doc %{_texmfdistdir}/doc/latex/zwpagelayout/adjusthead.pdf
%doc %{_texmfdistdir}/doc/latex/zwpagelayout/adjusthead.tex
%doc %{_texmfdistdir}/doc/latex/zwpagelayout/coversample.pdf
%doc %{_texmfdistdir}/doc/latex/zwpagelayout/coversample.tex
%doc %{_texmfdistdir}/doc/latex/zwpagelayout/zwpagelayout.pdf
%doc %{_texmfdistdir}/doc/latex/zwpagelayout/zwpagelayout.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Aug 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120809-1
+ Revision: 813205
- Update to latest release.

* Thu Jan 19 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2a-1
+ Revision: 762753
- Update to latest upstream package

* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2-3
+ Revision: 757786
- Rebuild to reduce used resources

* Fri Dec 09 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.2-2
+ Revision: 739947
- texlive-zwpagelayout

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.2-1
+ Revision: 719977
- texlive-zwpagelayout
- texlive-zwpagelayout
- texlive-zwpagelayout

