Name:		texlive-alertmessage
Version:	38055
Release:	2
Summary:	Alert messages for LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/alertmessage
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/alertmessage.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/alertmessage.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/alertmessage.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Some macros to display alert messages (informations, errors,
warnings and success messages).

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/alertmessage
%{_texmfdistdir}/tex/latex/alertmessage
%doc %{_texmfdistdir}/doc/latex/alertmessage

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
