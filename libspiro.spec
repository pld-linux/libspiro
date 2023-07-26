#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	Library to draw Raph Levien's spiro splines
Summary(pl.UTF-8):	Biblioteka do rysowania splajnów spiro Rapha Leviena
Name:		libspiro
%define	pkgver	1.3.0
%define	pkgdate	20221101
Version:	%{pkgver}.%{pkgdate}
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Libraries
#Source0Download: https://github.com/fontforge/libspiro/releases
Source0:	https://github.com/fontforge/libspiro/releases/download/%{pkgdate}/%{name}-dist-%{pkgdate}.tar.gz
# Source0-md5:	e5b8cbce8e55b089de96c6ea4c2b5bf6
URL:		https://libspiro.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	__cxx

%description
Library to draw Raph Levien's spiro splines.

%description -l pl.UTF-8
Biblioteka do rysowania splajnów spiro Rapha Leviena.

%package devel
Summary:	Header files for libspiro library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libspiro
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for libspiro library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libspiro.

%package static
Summary:	Static libspiro library
Summary(pl.UTF-8):	Statyczna biblioteka libspiro
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static libspiro library.

%description static -l pl.UTF-8
Statyczna biblioteka libspiro.

%prep
%setup -q -n %{name}-%{pkgdate}

%build
%configure \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libspiro.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README README-RaphLevien
%attr(755,root,root) %{_libdir}/libspiro.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libspiro.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libspiro.so
%{_includedir}/bezctx*.h
%{_includedir}/spiro*.h
%{_pkgconfigdir}/libspiro.pc
%{_mandir}/man3/libspiro.3*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libspiro.a
%endif
