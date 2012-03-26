%define git fee1ebe
%define major 2
%define libname %mklibname %{name} %{major}
%define devname %mklibname -d %{name}

Name:		yajl
Version:	2.0.4
Release:	%mkrel 1
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

