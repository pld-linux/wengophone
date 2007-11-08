#
# TODO:
# - why cmake doesn't see our OSIP2 - owfiles/FindOSIP2.cmake not executed
# - update desc.
Summary:	WengoPhone
Summary(pl.UTF-8):	WengoPhone
Name:		wengophone
Version:	2.1.2
Release:	0.5
License:	GPL
Group:		X11/Applications
Source0:	http://download.wengo.com/nightlybuilds/universal/sources/openwengo/%{version}/%{name}-%{version}-source.zip
# Source0-md5:	5c079f8e0b0bcf7e951c1350c0739520
Patch0:		%{name}-qt4tools.patch
Patch1:		%{name}-lrelease.patch
Patch2:		%{name}-avcodec.patch
Patch3:		%{name}-desktop.patch
URL:		http://www.openwengo.com/
BuildRequires:	QtCore-devel >= 4.1.4
BuildRequires:	QtGui-devel >= 4.1.4
BuildRequires:	QtSvg-devel >= 4.1.4
BuildRequires:	QtXml-devel >= 4.1.4
BuildRequires:	cmake >= 2.4.4
BuildRequires:	qt4-build >= 4.1.4
BuildRequires:	qt4-qmake >= 4.1.4
BuildRequires:	libosip2-devel >= 3.0.1
BuildRequires:	curl-libs >= 7.16.1
BuildRequires:	libsamplerate-devel >= 0.1.2
BuildRequires:	libsndfile-devel >= 1.0.12
BuildRequires:	alsa-lib-devel >= 1.0.11
BuildRequires:	ffmpeg-devel
BuildRequires:	libxml2-devel >= 2.6.24
BuildRequires:	openssl-devel >= 0.9.8a
BuildRequires:	glib2-devel >= 2.10.3
BuildRequires:	gnutls-devel >= 1.2.9
BuildRequires:	speex-devel >= 1.1.12
BuildRequires:	portaudio-devel >= 19
BuildRequires:	boost >= 1.33
BuildRequires:	boost-thread-devel >= 1.33
BuildRequires:	boost-signals-devel >= 1.33
BuildRequires:	boost-program_options-devel >= 1.33
BuildRequires:	boost-regex-devel >= 1.33
BuildRequires:	boost-test-devel >= 1.33
BuildRequires:	boost-python-devel >= 1.33
BuildRequires:	libuuid-devel
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WengoPhone.

#% description -l pl.UTF-8

%prep
%setup -q -n %{name}-%{version}-source
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
cd build
%cmake \
	-DCMAKE_BUILD_TYPE="Release" \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_desktopdir},%{_pixmapsdir},%{_datadir}/%{name},%{_datadir}/services}

cd build
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install ../wengophone/res/*.protocol $RPM_BUILD_ROOT%{_datadir}/services

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL.txt wengophone/COPYING
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_datadir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/*/*/*/*.png
%{_datadir}/services/*.protocol
