Summary:	Elegant image viewer
Name:		viewnior
Version:	1.5
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	https://github.com/xsisqox/Viewnior/archive/%{name}-%{version}.tar.gz
Source1:	viewnior.appdata.xml
URL:		http://siyanpanayotov.com/project/viewnior/
BuildRequires:	desktop-file-utils
BuildRequires:	exiv2-devel >= 0.21
BuildRequires:	gdk-pixbuf2-devel >= 2.4.0
BuildRequires:	gettext
BuildRequires:	glib2-devel >= 2.32
BuildRequires:	gnome-common
BuildRequires:	gtk+2-devel >= 2.20
BuildRequires:	intltool
BuildRequires:	shared-mime-info >= 0.20
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

%prep
%setup -qn Viewnior-%{name}-%{version}

%build
./autogen.sh
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

install -d $RPM_BUILD_ROOT%{_datadir}/appdata
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

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
%doc AUTHORS ChangeLog-20090517 COPYING NEWS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man*/%{name}*
%{_datadir}/appdata/%{name}.appdata.xml
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_datadir}/%{name}
