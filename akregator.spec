%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE feed reader application
Name:		akregator
Version:	22.08.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Patch0:		akregator-17.04.0-OMA-blog-feed.patch
Requires:	grantlee
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5WebEngine)
BuildRequires:	pkgconfig(Qt5WebEngineWidgets)
BuildRequires:	pkgconfig(Qt5PrintSupport)
BuildRequires:	cmake(Grantlee5)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5TextEditor)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5GrantleeTheme)
BuildRequires:	cmake(KF5KontactInterface)
BuildRequires:	cmake(KF5Libkdepim)
BuildRequires:	cmake(KF5Libkleo)
BuildRequires:	cmake(KF5MessageViewer)
BuildRequires:	cmake(KF5PimTextEdit)
BuildRequires:	cmake(KF5Syndication)
BuildRequires:	cmake(KF5WebEngineViewer)
BuildRequires:	cmake(KF5AkonadiMime)
BuildRequires:	cmake(KF5PimCommonAkonadi)
BuildRequires:	cmake(QGpgme)
BuildRequires:	cmake(KUserFeedback)
BuildRequires:	boost-devel
Requires:	kdepim-runtime
Suggests:	kdepim-addons
Conflicts:	kontact < 3:17.04.0

%description
Akregator is a news feed reader for the KDE desktop. It enables you to
follow news sites, blogs and other RSS/Atom-enabled websites without
the need to manually check for updates using a web browser. Akregator
is designed to be both easy to use and to be powerful enough to read
hundreds of news sources conveniently. It comes with Konqueror
integration for adding news feeds and with an internal browser for
easy news reading.

%files -f %{name}.lang
%{_kde5_applicationsdir}/org.kde.akregator.desktop
%{_bindir}/akregator
%{_bindir}/akregatorstorageexporter
%{_datadir}/config.kcfg/akregator.kcfg
%dir %{_datadir}/akregator/
%{_datadir}/akregator/*
%{_docdir}/*/*/akregator
%{_iconsdir}/hicolor/*/apps/akregator.*
%{_iconsdir}/hicolor/*/apps/akregator_empty.*
%{_datadir}/knotifications5/akregator.notifyrc
%{_datadir}/qlogging-categories5/akregator.categories
%{_datadir}/qlogging-categories5/akregator.renamecategories
%{_datadir}/metainfo/org.kde.akregator.appdata.xml
%{_datadir}/dbus-1/interfaces/org.kde.akregator.part.xml
%{_qt5_plugindir}/akregatorpart.so
%{_qt5_plugindir}/pim5/kontact/kontact_akregatorplugin.so
%{_qt5_plugindir}/pim5/kcms/akregator/akregator_config_advanced.so
%{_qt5_plugindir}/pim5/kcms/akregator/akregator_config_appearance.so
%{_qt5_plugindir}/pim5/kcms/akregator/akregator_config_archive.so
%{_qt5_plugindir}/pim5/kcms/akregator/akregator_config_browser.so
%{_qt5_plugindir}/pim5/kcms/akregator/akregator_config_general.so
%{_qt5_plugindir}/pim5/kcms/akregator/akregator_config_plugins.so
%{_qt5_plugindir}/pim5/kcms/akregator/akregator_config_security.so
%{_qt5_plugindir}/pim5/kcms/akregator/akregator_config_userfeedback.so

#----------------------------------------------------------------------------

%define akregatorinterfaces_major 5
%define libakregatorinterfaces %mklibname akregatorinterfaces %{akregatorinterfaces_major}

%package -n %{libakregatorinterfaces}
Summary:	KDE PIM shared library
Group:		System/Libraries

%description -n %{libakregatorinterfaces}
KDE PIM shared library.

%files -n %{libakregatorinterfaces}
%{_libdir}/libakregatorinterfaces.so.%{akregatorinterfaces_major}*

#----------------------------------------------------------------------------

%define akregatorprivate_major 5
%define libakregatorprivate %mklibname akregatorprivate %{akregatorprivate_major}

%package -n %{libakregatorprivate}
Summary:	KDE PIM shared library
Group:		System/Libraries

%description -n %{libakregatorprivate}
KDE PIM shared library.

%files -n %{libakregatorprivate}
%{_libdir}/libakregatorprivate.so.%{akregatorprivate_major}*

#----------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1
%cmake_kde5 -G "Unix Makefiles"

%build
%make -C build

%install
%makeinstall_std -C build

rm -rf %{buildroot}%{_kde5_libdir}/libakregatorinterfaces.so

%find_lang %{name}
