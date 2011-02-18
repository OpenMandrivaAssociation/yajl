%define major 1
%define libname %mklibname yajl %{major}
%define develname %mklibname yajl -d
%define staticdevelname %mklibname yajl -d -s

# NB, upstream does not provide pre-built tar.gz downloads. Instead
# they make you use the 'on the fly' generated tar.gz from GITHub's
# web interface
#
# The Source0 for any version is obtained by a URL
#
#   http://github.com/lloyd/yajl/tarball/1.0.7
#
# Which causes a download of a archive named after
# the GIT hash corresponding to the version tag
#
#   eg lloyd-yajl-45a1bdb.tar.gz
#
# NB even though the tar.gz is generated on the fly by GITHub it
# will always have identical md5sum
#
# So for new versions, update 'githash' to match the hash of the
# GIT tag associated with updated 'Version:' field just above
%global githash f4baae0

Name:		yajl
Version:	1.0.11
Release:	%mkrel 2
Summary:	Yet Another JSON Library (YAJL)
License:	BSD
Group:		System/Libraries
URL:		http://lloyd.github.com/yajl/

Source0: 	lloyd-%{name}-%{version}-0-g%{githash}.tar.gz

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	cmake

%description
YAJL is a Portable JSON parsing and serialization library in ANSI C.
It's event-driven (SAX-style) and also a small validating JSON
generator.


%package -n	%{libname}
Summary:	Yet Another JSON Library (YAJL)
Group:		System/Libraries

%description -n	%{libname}
YAJL is a Portable JSON parsing and serialization library in ANSI
C. It's event-driven (SAX-style) and also a small validating JSON
generator.

This package contains YAJL libraries files.


%package -n	%{develname}
Summary:	YAJL development files
Group:		Development/C
Provides:	libyajl-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n	%{develname}
YAJL is a Portable JSON parsing and serialization library in ANSI
C. It's event-driven (SAX-style) and also a small validating JSON
generator.

This package provides the libraries and includes for developing
against the YAJL library.


%package -n	%{staticdevelname}
Summary:	YAJL development files
Group:		Development/C
Requires:	%{name} = %{version}-%{release}

%description -n	%{staticdevelname}
YAJL is a Portable JSON parsing and serialization library in ANSI
C. It's event-driven (SAX-style) and also a small validating JSON
generator.

This package provides the static libraries and includes for developing
against the YAJL library.


%package 	utils
Summary:	YAJL binary utils for json files
Group:		Development/C
Requires:	%{name} = %{version}-%{release}

%description	utils
YAJL is a Portable JSON parsing and serialization library in ANSI
C. It's event-driven (SAX-style) and also a small validating JSON
generator.

This package provides utilities that accompany the YAJL library for
handling JSON files.

%prep
%setup -q -n lloyd-%{name}-%{githash}

%build
# Following 'by hand' instructions in BUILDING instead of 
# './configure && make install'.
%cmake ..
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
cd build
make install DESTDIR=%{buildroot}
# jvdm: don't know why cmake generated this; renaming came from fedora
# package.
mv %{buildroot}%{_includedir}/yajl/yajl_version.h.cmake \
  %{buildroot}%{_includedir}/yajl/yajl_version.h


%check
cd test
./run_tests.sh

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n	%{libname}
%defattr(-,root,root,-)
%{_libdir}/libyajl.so.%{major}*

%files -n	%{develname}
%defattr(-,root,root,-)
%doc COPYING ChangeLog README TODO
%dir %{_includedir}/yajl
%{_includedir}/yajl/*.h
%{_libdir}/libyajl.so

%files -n	%{staticdevelname}
%defattr(-,root,root)
%{_libdir}/libyajl_s.a

%files		utils
%defattr(-,root,root)
%{_bindir}/json_reformat
%{_bindir}/json_verify
