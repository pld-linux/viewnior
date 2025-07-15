Summary:	Elegant image viewer
Summary(pl.UTF-8):	Elegancka przeglądarka obrazków
Name:		viewnior
Version:	1.8
Release:	2
License:	GPL v3+
Group:		X11/Applications
#Source0Download: https://github.com/hellosiyan/Viewnior/tags
Source0:	https://github.com/hellosiyan/Viewnior/archive/%{name}-%{version}.tar.gz
# Source0-md5:	29d773910df2d120c193ff2e2bc971f3
Patch0:		%{name}-exiv2.patch
URL:		https://siyanpanayotov.com/project/viewnior/
BuildRequires:	desktop-file-utils
BuildRequires:	exiv2-devel >= 0.21
BuildRequires:	gdk-pixbuf2-devel >= 2.4.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.32
BuildRequires:	gtk+2-devel >= 2:2.20
BuildRequires:	libstdc++-devel
BuildRequires:	meson >= 0.43.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
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
%patch -P0 -p1

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

desktop-file-validate $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

%{__mv} $RPM_BUILD_ROOT%{_localedir}/{nb_NO,nb}

%find_lang %{name}

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
%doc AUTHORS NEWS README.md TODO
%attr(755,root,root) %{_bindir}/viewnior
%{_datadir}/%{name}
%{_datadir}/metainfo/viewnior.metainfo.xml
%{_desktopdir}/viewnior.desktop
%{_iconsdir}/hicolor/*x*/apps/viewnior.png
%{_iconsdir}/hicolor/scalable/apps/viewnior.svg
%{_mandir}/man1/viewnior.1*
