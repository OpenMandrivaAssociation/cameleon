%define name	cameleon
%define version	1.3
%define up_version	1_3
%define release	%mkrel 2

%if %mdkversion > 200900
%define ocaml_libdir %{_libdir}/ocaml
%else
%define ocaml_libdir %{ocaml_sitelib}
%endif

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    OCaml IDE
Group:      Development/Other
License:    MIT
URL:        http://pauillac.inria.fr/~guesdon/Tools/cameleon/cameleon.html
Source0:    http://pauillac.inria.fr/~guesdon/Tools/Tars/cameleon_%{up_version}.tar.gz
Patch0:     cameleon-1.3-use-camlp5.patch
Patch1:     cameleon-1.3-no-zoggy.patch
Patch2:     cameleon-1.3-fix-report-output.patch
BuildRequires:  ocaml
BuildRequires:  ocaml-ioxml
BuildRequires:  ocaml-lablgtk-devel
BuildRequires:  camlp5
BuildRequires:  ncurses-devel
Requires:   %{name}-libs = %{version}-%{release}
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Cameleon aims to become an integrated development environment for
Objective-Caml, and eventually other languages. Its main features are:

* graphical user interface,
* configuration management based on CVS,
* easy access to and browsing of documentation,
* various editors, according to customizable file types,
* use of plug-ins to define new features,
* highly customizable interface (menus, toolbar, keyboard shortcuts).

%package utils
Summary:	Utils for %{name}
Group:		Development/Other

%description utils
This package contains utils for %{name}.

%package libs
Summary:	Libraries for %{name}
Group:		Development/Other

%description libs
This package contains libraries for %{name}.

%prep
%setup -q
%patch0 -p 1
%patch1 -p 1
%patch2 -p 1
autoreconf

%build
./configure
make upto_toolhtml upto_toolhtml.opt LABLGTKDIR=%{ocaml_libdir}/lablgtk

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{ocaml_libdir}/cameleon
install -m 644 options/*.o %{buildroot}%{ocaml_libdir}/cameleon
install -m 644 options/*.cm{i,o,x} %{buildroot}%{ocaml_libdir}/cameleon
install -m 644 okey/*.o %{buildroot}%{ocaml_libdir}/cameleon
install -m 644 okey/*.cm{i,o,x} %{buildroot}%{ocaml_libdir}/cameleon
install -m 644 configwin/*.a %{buildroot}%{ocaml_libdir}/cameleon
install -m 644 configwin/*.cm{a,i,xa} %{buildroot}%{ocaml_libdir}/cameleon
install -m 644 report/*.a %{buildroot}%{ocaml_libdir}/cameleon
install -m 644 report/*.cm{a,i,xa} %{buildroot}%{ocaml_libdir}/cameleon
install -m 644 toolhtml/*.a %{buildroot}%{ocaml_libdir}/cameleon
install -m 644 toolhtml/*.cm{a,i,xa} %{buildroot}%{ocaml_libdir}/cameleon

install -d -m 755 %{buildroot}%{_bindir}
install -m 755 report/report.opt %{buildroot}%{_bindir}/report
install -m 755 report/report.gui.opt %{buildroot}%{_bindir}/report.gui
install -m 755 report/translate.opt %{buildroot}%{_bindir}/translate

%clean
rm -rf %{buildroot}

%files utils
%{_bindir}/report
%{_bindir}/report.gui
%{_bindir}/translate

%files libs
%doc README TODO INSTALL LICENSE
%defattr(-,root,root)
%{ocaml_libdir}/cameleon
