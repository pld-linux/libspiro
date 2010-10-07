Summary:	Library to draw Raph Levien's spiro splines
Summary(pl.UTF-8):	Biblioteka do rysowania splajnów spiro Rapha Leviena
Name:		libspiro
Version:	20071029
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libspiro/%{name}_src-%{version}.tar.bz2
# Source0-md5:	ab6aaa50bbd8fa55e78f8b8b0112f6cd
URL:		http://libspiro.sourceforge.net/
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library to draw Raph Levien's spiro splines.

%description -l pl.UTF-8
Biblioteka do rysowania splajnów spiro Rapha Leviena.

%package devel
Summary:	Header files for libspiro library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libspiro
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libspiro library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libspiro.

%package static
Summary:	Static libspiro library
Summary(pl.UTF-8):	Statyczna biblioteka libspiro
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libspiro library.

%description static -l pl.UTF-8
Statyczna biblioteka libspiro.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.* .
%configure \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README README-RaphLevien
%attr(755,root,root) %{_libdir}/libspiro.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libspiro.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libspiro.so
%{_libdir}/libspiro.la
%{_includedir}/bezctx*.h
%{_includedir}/spiro*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libspiro.a
