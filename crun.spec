%ifarch %{x8664} %{armv7} %{armv8} aarch64 ppc64
%define		with_criu	1
%endif

%ifarch %{ix86} %{x8664} %{arm} aarch64 mips64 mips64le ppc64 ppc64le s390x
%define		with_man	1
%endif

Summary:	OCI runtime written in C
Name:		crun
Version:	1.18.1
Release:	1
License:	GPL v3+
Group:		Applications/System
Source0:	https://github.com/containers/crun/releases/download/%{version}/%{name}-%{version}.tar.zst
# Source0-md5:	77a1be98037ed9cf066833fd2a5227f2
URL:		https://github.com/containers/crun
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.11.2
%{?with_criu:BuildRequires:	criu-devel >= 3.16.1}
%{?with_man:BuildRequires:	go-md2man}
BuildRequires:	libcap-devel
BuildRequires:	libseccomp-devel
BuildRequires:	libselinux-devel
BuildRequires:	libtool
BuildRequires:	linux-libc-headers >= 7:3.18
BuildRequires:	pkgconfig
BuildRequires:	python3
BuildRequires:	python3-modules
BuildRequires:	rpmbuild(macros) >= 2.007
BuildRequires:	systemd-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	yajl-devel >= 2.0.0
BuildRequires:	zstd
Requires:	yajl >= 2.0.0
%{?with_criu:Suggests:	criu-libs >= 3.16.1}
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
