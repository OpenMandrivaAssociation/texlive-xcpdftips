Name:		texlive-xcpdftips
Version:	50449
Release:	2
Summary:	Natbib citations with PDF tooltips
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/xcpdftips
License:	gpl3+
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xcpdftips.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xcpdftips.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xcpdftips.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX package uses pdfcomment and bibentry to surround
natbib citations with PDF tooltips.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/xcpdftips
%{_texmfdistdir}/tex/latex/xcpdftips
%doc %{_texmfdistdir}/doc/latex/xcpdftips

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
