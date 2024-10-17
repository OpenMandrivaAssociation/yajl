%define git fee1ebe
%define major 2
%define libname %mklibname %{name} %{major}
%define devname %mklibname -d %{name}

Name:		yajl
Version:	2.1.0
Release:	3
Summary:	Yet Another JSON Library
License:	ISC License
Group:		System/Libraries
Url:		https://lloyd.github.com/yajl/
Source0:	http://github.com/lloyd/yajl/tarball/%{name}-%{version}.tar.gz
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
%autosetup -p1

%build
%cmake
%make_build

%install
%make_install -C build

rm -f %{buildroot}%{_libdir}/*.a

%files
%{_bindir}/json_reformat
%{_bindir}/json_verify

%files -n %{libname}
%{_libdir}/libyajl.so.*

%files -n %{devname}
%{_libdir}/libyajl.so
%{_includedir}/yajl
%{_datadir}/pkgconfig/yajl.pc
