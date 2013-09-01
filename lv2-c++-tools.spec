Summary:	A LV2 Development SDK
Summary(pl.UTF-8):	Narzędzia programistyczne LV2
Name:		lv2-c++-tools
Version:	1.0.5
Release:	1
License:	GPL v3+
Group:		Libraries
Source0:	http://download.savannah.nongnu.org/releases/ll-plugins/%{name}-%{version}.tar.bz2
# Source0-md5:	4707f2507f86d6c7bbaa809bb52eed9b
URL:		http://ll-plugins.nongnu.org/hacking.html
BuildRequires:	bash >= 3.0
BuildRequires:	boost-devel
BuildRequires:	gtkmm-devel >= 2.8.8
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This software package contains libraries and programs that should make
it easier to write LV2 plugins.

%description -l pl.UTF-8
Pakiet ten zawiera biblioteki i programy, które powinny przyczynić
się do łatwiejszego pisania wtyczek LV2.

%package devel
Summary:	Header files for LV2-C++-tools libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek LV2-C++-tools
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
# lv2-gui additionally gtkmm-devel >= 2.6.0

%description devel
Header files for LV2-C++-tools libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek LV2-C++-tools.

%package static
Summary:	Static LV2 libpaq library
Summary(pl.UTF-8):	Statyczna biblioteka LV2 libpaq
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static LV2 libpaq library.

%description static -l pl.UTF-8
Statyczna biblioteka LV2 libpaq.

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

%{__ldconfig} -n $RPM_BUILD_ROOT%{_libdir}

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
%attr(755,root,root) %{_libdir}/libpaq.so
%{_libdir}/liblv2-gui.a
%{_libdir}/liblv2-plugin.a
%{_includedir}/lv2-c++-tools
%{_pkgconfigdir}/lv2-plugin.pc
%{_pkgconfigdir}/lv2-gui.pc
%{_pkgconfigdir}/paq.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libpaq.a
