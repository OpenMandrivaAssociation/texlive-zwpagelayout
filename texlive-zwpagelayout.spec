%global tl_name zwpagelayout
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4e
Release:	%{tl_revision}.1
Summary:	Page layout and crop-marks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/zwpagelayout
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/zwpagelayout.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/zwpagelayout.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package was developed as a typographers' toolbox offering important
basic features for everyday work. It allows setting the paper size and
the page layout; it can print crop marks; and it can reflect pages both
horizontally and vertically. The package facilities work with TeX
(output via dvips or (x)dvipdfm(x)), and with pdfTeX.

