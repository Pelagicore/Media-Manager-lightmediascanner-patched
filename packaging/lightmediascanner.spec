Name:       lightmediascanner
Summary:    Light media scanner is a media indexer for embedded devices
Version:    0.4.5
Release:    1
Group:      Multimedia/Libraries
License:    LGPL-2.1
Source:	    %{name}-%{version}.tar.gz
Url:	    http://lms.garage.maemo.org/
BuildRequires: sqlite-devel
BuildRequires: gettext-tools
BuildRequires: pkgconfig(flac)
BuildRequires: pkgconfig(vorbis)

%description
Description: %{summary}

%package devel
Summary: LMS headers, static libraries, documentation and test programs
Requires: %{name} = %{version}

%description devel
Headers, static libraries, test programs and documentation for LMS

%prep
%setup -q -n %{name}-%{version}

%build

%autogen

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-, root, root)
%doc AUTHORS README
%license COPYING
%{_libdir}/*.so.*
%{_libdir}/lightmediascanner/plugins/*

%files devel
%defattr(-, root, root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
