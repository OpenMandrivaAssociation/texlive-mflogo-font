Name:		texlive-mflogo-font
Version:	54512
Release:	1
Summary:	Metafont logo font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mflogo-font
License:	knuth
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mflogo-font.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mflogo-font.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
These fonts were created in Metafont by Knuth, for his own
publications. At some stage, the letters 'P' and 'S' were
added, so that the MetaPost logo could also be expressed. The
fonts were originally issued (of course) as Metafont source;
they have since been autotraced and reissued in Adobe Type 1
format by Taco Hoekwater.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/fonts/type1/hoekwater/mflogo-font
%{_texmfdistdir}/fonts/map/dvips/mflogo-font
%{_texmfdistdir}/fonts/afm/hoekwater/mflogo-font
%doc %{_texmfdistdir}/doc/fonts/mflogo-font

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
