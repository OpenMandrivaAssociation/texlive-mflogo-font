%global tl_name mflogo-font
%global tl_revision 54512
%global tl_version 1.002

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Metafont logo font
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/mflogo
License:	knuth
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mflogo-font.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mflogo-font.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
These fonts were created in Metafont by Knuth, for his own publications.
At some stage, the letters 'P' and 'S' were added, so that the MetaPost
logo could also be expressed. The fonts were originally issued (of
course) as Metafont source; they have since been autotraced and reissued
in Adobe Type 1 format by Taco Hoekwater.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from mflogo-font:
MixedMap mflogo.map
TL_DROPIN_EOF
