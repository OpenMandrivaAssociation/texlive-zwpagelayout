# revision 23812
# category Package
# catalog-ctan /macros/latex/contrib/zwpagelayout
# catalog-date 2011-09-04 18:51:51 +0200
# catalog-license lppl
# catalog-version 1.2
Name:		texlive-zwpagelayout
Version:	1.2
Release:	1
Summary:	Page layout and crop-marks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/zwpagelayout
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zwpagelayout.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zwpagelayout.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This package was developed as a typographers' toolbox offering
important basic features for everyday work. It allows setting
the paper size and the page layout; it can print crop marks
both; and it can reflect pages both horizontally and
vertically. The package facilities work with TeX + dvips or
(x)dvipdfm(x), and with pdfTeX.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/zwpagelayout/zwpagelayout.sty
%doc %{_texmfdistdir}/doc/latex/zwpagelayout/License
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
