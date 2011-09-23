Name:		yajl
Version:	1.0.11
%define	subrel	1
Release:	%mkrel 4
Summary:	Yet Another JSON Library (YAJL)

Group:		System/Libraries
License:	BSD
URL:		http://lloyd.github.com/yajl/

%define		githash	f4baae0
Source0:	lloyd-%{name}-%{version}-0-g%{githash}.tar.gz

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	cmake

%package devel
Summary:	Libraries, includes, etc to develop with YAJL
Requires:	%{name} = %{version}-%{release}

%package        utils
Summary:	YAJL binary utils for json files
Requires:	%{name} = %{version}
Group:		Development/C
Requires:	%{name} = %{version}-%{release}


%description
Yet Another JSON Library. YAJL is a small event-driven
(SAX-style) JSON parser written in ANSI C, and a small
validating JSON generator.

%description devel
Yet Another JSON Library. YAJL is a small event-driven
(SAX-style) JSON parser written in ANSI C, and a small
validating JSON generator.

%description    utils
YAJL is a Portable JSON parsing and serialization library in ANSI
C. It's event-driven (SAX-style) and also a small validating JSON
generator.

This sub-package provides the libraries and includes
necessary for developing against the YAJL library



%prep
%setup -q -n lloyd-%{name}-%{githash}

%build
# NB, we are not using upstream's 'configure'/'make'
# wrapper, instead we use cmake directly to better
# align with Fedora standards

#mkdir build
#cd build
%cmake ..
make VERBOSE=1 %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
cd build
make install DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT%{_includedir}/yajl/yajl_version.h.cmake \
  $RPM_BUILD_ROOT%{_includedir}/yajl/yajl_version.h


# No static libraries
rm -f $RPM_BUILD_ROOT%{_libdir}/libyajl_s.a


%check
cd test
./run_tests.sh

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING ChangeLog README TODO
%{_bindir}/json_reformat
%{_bindir}/json_verify
%{_libdir}/libyajl.so.1
%{_libdir}/libyajl.so.1.*


%files -n %{name}-utils
%defattr(-,root,root)


%files devel
%defattr(-,root,root,-)
%doc COPYING
%dir %{_includedir}/yajl
%{_includedir}/yajl/yajl_common.h
%{_includedir}/yajl/yajl_gen.h
%{_includedir}/yajl/yajl_parse.h
%{_includedir}/yajl/yajl_version.h
%{_libdir}/libyajl.so
