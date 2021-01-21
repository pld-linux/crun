%ifarch %{x8664} %{arm} aarch64 ppc64
%define		with_criu	1
%endif

%ifarch %{ix86} %{x8664} %{arm} aarch64 mips64 mips64le ppc64 ppc64le s390x
%define		with_man	1
%endif

Summary:	OCI runtime written in C
Name:		crun
Version:	0.17
Release:	1
License:	GPL v3+
Group:		Applications/System
Source0:	https://github.com/containers/crun/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	3cded6f821a9e09bc634d08a7799e213
URL:		https://github.com/containers/crun
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.11.2
%{?with_criu:BuildRequires:	criu-devel >= 3.15}
%{?with_man:BuildRequires:	go-md2man}
BuildRequires:	libcap-devel
BuildRequires:	libseccomp-devel
BuildRequires:	libselinux-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python3
BuildRequires:	python3-devel
BuildRequires:	systemd-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yajl-devel >= 2.0.0
Requires:	criu-libs >= 3.15
Requires:	yajl >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
crun is a runtime for running OCI containers.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libcrun.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/crun
%{?with_man:%{_mandir}/man1/crun.1*}
