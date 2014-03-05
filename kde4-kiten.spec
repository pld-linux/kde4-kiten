%define		_state		stable
%define		orgname		kiten

Summary:	K Desktop Environment - A Japanese reference tool
Summary(pl.UTF-8):	K Desktop Environment - Słownik angielsko-japoński
Name:		kde4-kiten
Version:	4.12.3
Release:	1
License:	GPL
Group:		X11/Applications/Science
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	8a8a2793e80c0f973cdd155bd18cb075
URL:		http://www.kde.org/
BuildRequires:	kde4-kdelibs-devel
Obsoletes:	kde4-kdeedu-kiten < 4.6.99
Obsoletes:	kiten <= 4.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kiten is an application with multiple functions. Firstly, it is a
convenient English to Japanese and Japanese to English dictionary;
secondly, it is a Kanji dictionary, with multiple ways to look up
specific characters; thirdly, it is a tool to help you learn Kanji.

%description -l pl.UTF-8
Kiten to aplikacja o wielu funkcjach. Po pierwsze, jest wygodnym
słownikiem angielsko-japońskim i japońsko-angielskim; po drugie, jest
słownikiem Kanji z wieloma sposobami wyszukiwania określonych znaków;
po trzecie, jest narzędziem pomagającym w nauce Kanji.

%package devel
Summary:	Header files for kiten libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek kiten
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	kiten-devel <= 4.8.0

%description devel
Header files for kiten libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek kiten.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{orgname} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kiten
%attr(755,root,root) %{_bindir}/kitengen
%attr(755,root,root) %{_bindir}/kitenkanjibrowser
%attr(755,root,root) %{_bindir}/kitenradselect
%attr(755,root,root) %ghost %{_libdir}/libkiten.so.4
%attr(755,root,root) %{_libdir}/libkiten.so.*.*.*
%{_datadir}/apps/kiten
%{_datadir}/apps/kitenradselect
%{_datadir}/apps/kitenkanjibrowser
%{_datadir}/config.kcfg/kiten.kcfg
%{_desktopdir}/kde4/kiten.desktop
%{_desktopdir}/kde4/kitenkanjibrowser.desktop
%{_desktopdir}/kde4/kitenradselect.desktop
%{_fontsdir}/kanjistrokeorders
%{_iconsdir}/hicolor/scalable/apps/kiten.svgz
%{_iconsdir}/hicolor/*x*/apps/kiten.png

%files devel
%defattr(644,root,root,755)
%{_includedir}/libkiten
%attr(755,root,root) %{_libdir}/libkiten.so
