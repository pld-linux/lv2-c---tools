Summary:	A LV2 Development SDK
Summary(pl.UTF-8):	Narzędzia programistyczne LV2
Name:		lv2-c++-tools
Version:	1.0.3
Release:	1
License:	GPL v3+
Group:		Libraries
Source0:	http://download.savannah.nongnu.org/releases/ll-plugins/%{name}-%{version}.tar.bz2
# Source0-md5:	03547cc1c36b3ccb607ea9f1005365a1
URL:		http://freshmeat.net/projects/lv2-c-tools
BuildRequires:	boost-devel
BuildRequires:	gtkmm-devel >= 2.8.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This software package contains libraries and programs that should make
it easier to write LV2 plugins.

%description -l pl.UTF-8
Pakiet ten zawiera biblioteki i programy, które powinny przyczynić
się do łatwiejszego pisania wtyczek LV2.

%package devel
Summary:	Header files for lv2-c++-tools library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki lv2-c++-tools
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for lv2-c++-tools library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki lv2-c++-tools.

%package static
Summary:	Static lv2-c++-tools library
Summary(pl.UTF-8):	Statyczna biblioteka lv2-c++-tools
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static lv2-c++-tools library.

%description static -l pl.UTF-8
Statyczna biblioteka lv2-c++-tools.

%package utils
Summary:	Utils for lv2-c++-tools
Summary(pl.UTF-8):	Narzędzia dla lv2-c++-tools
Group:		Development/Tools

%description utils
Utils for lv2-c++-tools.

%description utils -l pl.UTF-8
Narzędzia dla lv2-c++-tools.

%prep
%setup -q
%__sed -i -e 's|/sbin/ldconfig -n |/bin/true |g' Makefile.template

%build
./configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--CFLAGS="%rpmcflags" \
	--LDFLAGS="%rpmldflags"

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
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libpaq.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/lv2-c++-tools
%{_libdir}/libpaq.so
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lv2peg
%attr(755,root,root) %{_bindir}/lv2soname