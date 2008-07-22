#
# TODO:
# - why cmake doesn't see our OSIP2 - owfiles/FindOSIP2.cmake not executed
# - doesn't build on ppc:
#   Linking CXX executable qtwengophone
#   /home/users/builder/rpm/BUILD/wengophone-2.1.2-source/build/libs/3rdparty/coredumper/libcoredumper.so: undefined reference to `GetAllProcessThreads'
#   collect2: ld returned 1 exit status
#   make[2]: *** [wengophone/src/presentation/qt/qtwengophone] Error 1
# - add pl summary and desc
# - doesn't build with boost-1.35.0 (libs/owutil/thread/RecursiveMutex.h):
#	boost::detail::thread::lock_ops has been removed.
#	Code that relies on the lock_ops implementation detail
#	will no longer work, as this has been removed, as it is no longer
#	necessary now that mutex types now have public lock()
#	and unlock()  member functions. (http://www.boost.org/users/news/version_1_35_0)
#
Summary:	Free software SIP compliant VoIP client developed by the OpenWengo community
Summary(pl.UTF-8):	Wolnodostępny klient VoIP zgodny z SIP tworzony przez społeczność OpenWengo
Name:		wengophone
Version:	2.1.2
Release:	1.1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://download.wengo.com/nightlybuilds/universal/sources/openwengo/%{version}/%{name}-%{version}-source.zip
# Source0-md5:	5c079f8e0b0bcf7e951c1350c0739520
Patch0:		%{name}-avcodec.patch
Patch1:		%{name}-desktop.patch
URL:		http://www.openwengo.com/
BuildRequires:	QtGui-devel >= 4.1.4
BuildRequires:	QtSvg-devel >= 4.1.4
BuildRequires:	QtUiTools-devel >= 4.1.4
BuildRequires:	alsa-lib-devel >= 1.0.11
BuildRequires:	boost-devel >= 1.35.0
BuildRequires:	boost-python-devel
BuildRequires:	cmake >= 2.4.4
BuildRequires:	curl-devel >= 7.16.1
BuildRequires:	ffmpeg-devel
BuildRequires:	glib2-devel >= 2.10.3
BuildRequires:	gnutls-devel >= 1.2.9
BuildRequires:	libosip2-devel >= 3.0.1
BuildRequires:	libsamplerate-devel >= 0.1.2
BuildRequires:	libsndfile-devel >= 1.0.12
BuildRequires:	libuuid-devel
BuildRequires:	libxml2-devel >= 2.6.24
BuildRequires:	openssl-devel >= 0.9.8a
BuildRequires:	pkgconfig
BuildRequires:	portaudio-devel >= 19
BuildRequires:	qt4-build >= 4.3.3-3
BuildRequires:	qt4-linguist >= 4.3.3-3
BuildRequires:	qt4-qmake >= 4.3.3-3
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRequires:	speex-devel >= 1.1.12
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WengoPhone is a free software SIP compliant VoIP client developed by
the OpenWengo community. It allows users to speak to other users of
SIP compliant VoIP software at no cost. It also allows users to call
landlines, cellphones, send SMS and make video calls. None of these
functionalities are tied to a particular SIP provider and can be used
with any provider available on the market, unlike proprietary software
such as Skype and others.

%description -l pl.UTF-8
WengoPhone to wolnodostępny, programowy klient VoIP zgodny z SIP
rozwijany przez społeczność OpenWengo. Pozwala użytkownikom bezpłatnie
rozmawiać z innymi użytkownikami oprogramowania VoIP zgodnego z SIP, a
także dzwonić na linie naziemne i telefony komórkowe, wysyłać SMS-y i
nawiązywać połączenia wideo. Żadna z tych funkcji nie jest przywiązana
do określonego dostawcy SIP; wszystkie mogą być wykorzystywane u
dowolnego dostawcy na rynku, w przeciwieństwie do programów
własnościowych, takich jak Skype czy inne.

%prep
%setup -q -n %{name}-%{version}-source
%patch0 -p1
%patch1 -p1

%build
cd build
%cmake \
	-DCMAKE_BUILD_TYPE="Release" \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DQT_LRELEASE_EXECUTABLE=%{_bindir}/lrelease-qt4 \
	-DQT_MOC_EXECUTABLE=%{_bindir}/moc-qt4 \
	-DQT_UIC_EXECUTABLE=%{_bindir}/uic-qt4 \
	-DQT_QMAKE_EXECUTABLE=%{_bindir}/qmake-qt4 \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_desktopdir},%{_pixmapsdir},%{_datadir}/%{name},%{_datadir}/services}

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

install wengophone/res/*.protocol $RPM_BUILD_ROOT%{_datadir}/services

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_datadir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/*/*/*/*.png
%{_datadir}/services/*.protocol
