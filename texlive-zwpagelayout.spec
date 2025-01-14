Name:		texlive-zwpagelayout
Epoch:		1
Version:	63074
Release:	2
Summary:	Page layout and crop-marks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/zwpagelayout
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zwpagelayout.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zwpagelayout.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package was developed as a typographers' toolbox offering
important basic features for everyday work. It allows setting
the paper size and the page layout; it can print crop marks;
and it can reflect pages both horizontally and vertically. The
package facilities work with TeX + dvips or (x)dvipdfm(x), and
with pdfTeX.

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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
