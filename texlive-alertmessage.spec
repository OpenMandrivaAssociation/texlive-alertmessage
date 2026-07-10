%global tl_name alertmessage
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Alert messages for LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/alertmessage
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/alertmessage.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/alertmessage.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/alertmessage.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Some macros to display alert messages (informational, error, warning and
success messages).

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/alertmessage
%dir %{_datadir}/texmf-dist/source/latex/alertmessage
%dir %{_datadir}/texmf-dist/tex/latex/alertmessage
%dir %{_datadir}/texmf-dist/tex/latex/alertmessage/img
%doc %{_datadir}/texmf-dist/doc/latex/alertmessage/README.md
%doc %{_datadir}/texmf-dist/doc/latex/alertmessage/alertmessage.pdf
%doc %{_datadir}/texmf-dist/source/latex/alertmessage/alertmessage.dtx
%doc %{_datadir}/texmf-dist/source/latex/alertmessage/alertmessage.ins
%{_datadir}/texmf-dist/tex/latex/alertmessage/alertmessage.sty
%{_datadir}/texmf-dist/tex/latex/alertmessage/img/alertmessage-error.png
%{_datadir}/texmf-dist/tex/latex/alertmessage/img/alertmessage-info.png
%{_datadir}/texmf-dist/tex/latex/alertmessage/img/alertmessage-success.png
%{_datadir}/texmf-dist/tex/latex/alertmessage/img/alertmessage-warning.png
