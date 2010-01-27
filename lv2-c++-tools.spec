Summary:	A LV2 Development SDK
Summary(pl.UTF-8):	Narzędzia programistyczne LV2
Name:		lv2-c++-tools
Version:	1.0.3
Release:	1
License:	GPL v3+
Group:		Libraries
Source0:	http://download.savannah.nongnu.org/releases/ll-plugins/%{name}-%{version}.tar.bz2
# Source0-md5:	8db2c4124af6ef932002bba9d99ba09f
URL:		http://freshmeat.net/projects/lv2-c-tools
BuildRequires:	boost-devel
BuildRequires:	gtkmm-devel >= 2.8.8
BuildRequires:	pkgconfig
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

%prep
%setup -q
%{__sed} -i -e '/sbin\/ldconfig -n /d' Makefile.template

%build
./configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--CXX="%{__cxx}" \
	--CFLAGS="%{rpmcppflags} %{rpmcxxflags}" \
	--LDFLAGS="%{rpmcxxflags} %{rpmldflags}"

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
%attr(755,root,root) %{_bindir}/lv2peg
%attr(755,root,root) %{_bindir}/lv2soname
%attr(755,root,root) %{_libdir}/libpaq.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libpaq.so.0

%files devel
%defattr(644,root,root,755)
%{_includedir}/lv2-c++-tools
%{_libdir}/libpaq.so
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libpaq.a
%{_libdir}/liblv2-gui.a
%{_libdir}/liblv2-plugin.a
