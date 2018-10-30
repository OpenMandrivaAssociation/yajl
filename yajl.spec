%define git fee1ebe
%define major 2
%define libname %mklibname %{name} %{major}
%define devname %mklibname -d %{name}

Name:		yajl
Version:	2.0.4
Release:	10
Summary:	Yet Another JSON Library
License:	ISC License
Group:		System/Libraries
Url:		http://lloyd.github.com/yajl/
Source0:	lloyd-%{name}-%{version}-0-g%{git}.tar.gz
BuildRequires:	doxygen
BuildRequires:	cmake
Requires:	%{libname} = %{EVRD}

%description
Yet Another JSON Library. YAJL is a small event-driven (SAX-style) JSON parser
written in ANSI C, and a small validating JSON generator. YAJL is released
under the ISC license.

%package -n %{libname}
Summary:	%{summary}
Provides:	lib%{name}

%description -n %{libname}
Yet Another JSON Library. YAJL is a small event-driven (SAX-style) JSON parser
written in ANSI C, and a small validating JSON generator. YAJL is released
under the ISC license.

%package -n %{devname}
Summary:	Development files for using %{name}
Group:		Development/C
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files for using %{name}

%prep
%setup -q -n lloyd-%{name}-%{git}

%build
%cmake
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std -C build

%__rm -f %{buildroot}%{_libdir}/*.a

%clean
%__rm -rf %{buildroot}

%files
%{_bindir}/json_reformat
%{_bindir}/json_verify

%files -n %{libname}
%{_libdir}/libyajl.so.*

%files -n %{devname}
%{_libdir}/libyajl.so
%{_includedir}/yajl
%{_datadir}/pkgconfig/yajl.pc



%changelog
* Mon Mar 26 2012 Andrey Bondrov <abondrov@mandriva.org> 2.0.4-1mdv2012.0
+ Revision: 786878
- New version 2.0.4, new library major 2

* Fri Sep 23 2011 Alexander Barakin <abarakin@mandriva.org> 1.0.11-4.1
+ Revision: 701106
- back compat to yajl-utils (fix #64225 #64302)

* Wed Sep 21 2011 Alexander Barakin <abarakin@mandriva.org> 1.0.11-4
+ Revision: 700747
- imported package yajl

* Sun Feb 27 2011 Funda Wang <fwang@mandriva.org> 1.0.11-3
+ Revision: 640470
- rebuild to obsolete old packages

* Fri Feb 18 2011 Joao Victor Duarte Martins <jvdm@mandriva.com.br> 1.0.11-2
+ Revision: 638321
- fix static lib package name
- fix provides/requires of devel package

* Tue Feb 15 2011 Joao Victor Duarte Martins <jvdm@mandriva.com.br> 1.0.11-1
+ Revision: 637854
- First initial release.
- create yajl

