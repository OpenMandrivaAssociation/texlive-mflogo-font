%global tl_name mflogo-font
%global tl_revision 54512

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.002
Release:	%{tl_revision}.1
Summary:	Metafont logo font
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/mflogo
License:	knuth
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mflogo-font.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mflogo-font.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
These fonts were created in Metafont by Knuth, for his own publications.
At some stage, the letters 'P' and 'S' were added, so that the MetaPost
logo could also be expressed. The fonts were originally issued (of
course) as Metafont source; they have since been autotraced and reissued
in Adobe Type 1 format by Taco Hoekwater.

