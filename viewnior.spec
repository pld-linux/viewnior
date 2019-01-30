Summary:	Elegant image viewer
Summary(pl.UTF-8):	Elegancka przeglądarka obrazków
Name:		viewnior
Version:	1.6
Release:	3
License:	GPL v3+
Group:		X11/Applications
#Source0Download: https://github.com/xsisqox/Viewnior/releases
Source0:	https://github.com/xsisqox/Viewnior/archive/%{name}-%{version}.tar.gz
# Source0-md5:	f7d497360c48ce4bce09328d934cc4a4
Patch0:		%{name}-appdata.patch
URL:		http://siyanpanayotov.com/project/viewnior/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake >= 1:1.11
BuildRequires:	desktop-file-utils
BuildRequires:	exiv2-devel >= 0.21
BuildRequires:	gdk-pixbuf2-devel >= 2.4.0
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.32
BuildRequires:	gtk+2-devel >= 2:2.20
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	shared-mime-info >= 0.20
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	exiv2-libs >= 0.21
Requires:	gdk-pixbuf2 >= 2.4.0
Requires:	glib2 >= 1:2.32
Requires:	gtk+2 >= 2:2.20
Requires:	hicolor-icon-theme
Requires:	shared-mime-info >= 0.20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Viewnior is an image viewer program. Created to be simple, fast and
elegant. It's minimalistic interface provides more screen space for
your images.

Among its features are:
- Fullscreen & Slideshow
- Rotate, flip, save, delete images
- Animation support
- Browse only selected images
- Navigation window
- Simple interface
- Configurable mouse actions

%description -l pl.UTF-8
Viewnior to przeglądarka obrazków. Stworzona z myślą o prostocie,
szybkości i elegancji. Minimalistyczny interfejs pozostawia więcej
miejsca na ekranie dla obrazów.

Możliwości obejmują między innymi:
- tryb pełnoekranowy i przeglądu slajdów
- obracanie, odwracanie, zapis i usuwanie obrazów
- obsługę animacji
- przeglądanie tylko wybranych obrazów
- okno nawigacji
- prosty interfejs
- konfigurowalne akcje myszy

%prep
%setup -qn Viewnior-%{name}-%{version}
%patch0 -p1

%build
install -d m4
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-wallpaper

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL='install -p' \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

desktop-file-validate $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

# check when manual install becomes obsolete and can be dropped
test ! -f $RPM_BUILD_ROOT%{_datadir}/appdata/viewnior.appdata.xml || exit 1
install -d $RPM_BUILD_ROOT%{_datadir}/appdata
cp -p data/%{name}.appdata.xml $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database
%update_icon_cache hicolor

%postun
%update_desktop_database
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog-20090517 NEWS README TODO
%attr(755,root,root) %{_bindir}/viewnior
%{_datadir}/%{name}
%{_datadir}/appdata/viewnior.appdata.xml
%{_desktopdir}/viewnior.desktop
%{_iconsdir}/hicolor/*x*/apps/viewnior.png
%{_iconsdir}/hicolor/scalable/apps/viewnior.svg
%{_mandir}/man1/viewnior.1*
