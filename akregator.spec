#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE feed reader application
Name:		akregator
Version:	25.08.1
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/akregator/-/archive/%{gitbranch}/akregator-%{gitbranchd}.tar.bz2#/akregator-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/akregator-%{version}.tar.xz
%endif
Patch0:		akregator-17.04.0-OMA-blog-feed.patch
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6Test)
BuildRequires:	pkgconfig(Qt6WebEngineCore)
BuildRequires:	pkgconfig(Qt6WebEngineWidgets)
BuildRequires:	pkgconfig(Qt6PrintSupport)
BuildRequires:	cmake(KF6TextTemplate)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6NotifyConfig)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(KF6TextEditor)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(KF6TextUtils)
BuildRequires:	cmake(KF6StatusNotifierItem)
BuildRequires:	cmake(KPim6GrantleeTheme)
BuildRequires:	cmake(KPim6KontactInterface)
BuildRequires:	cmake(KPim6Libkdepim)
BuildRequires:	cmake(KPim6Libkleo)
BuildRequires:	cmake(KPim6MessageViewer)
BuildRequires:	cmake(KF6Syndication)
BuildRequires:	cmake(KPim6WebEngineViewer)
BuildRequires:	cmake(KPim6AkonadiMime)
BuildRequires:	cmake(KPim6PimCommonAkonadi)
BuildRequires:	cmake(QGpgme)
BuildRequires:	cmake(KF6UserFeedback)
BuildRequires:	cmake(KF6TextAddonsWidgets)
BuildRequires:	%mklibname -d KF6UserFeedbackWidgets
BuildRequires:	boost-devel
Requires:	kdepim-runtime >= 6.0
Suggests:	kdepim-addons >= 6.0

%rename plasma6-akregator

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
Akregator is a news feed reader for the KDE desktop. It enables you to
follow news sites, blogs and other RSS/Atom-enabled websites without
the need to manually check for updates using a web browser. Akregator
is designed to be both easy to use and to be powerful enough to read
hundreds of news sources conveniently. It comes with Konqueror
integration for adding news feeds and with an internal browser for
easy news reading.

%files -f %{name}.lang
%{_datadir}/applications/org.kde.akregator.desktop
%{_bindir}/akregator
%{_bindir}/akregatorstorageexporter
%{_datadir}/config.kcfg/akregator.kcfg
%{_iconsdir}/hicolor/*/apps/akregator.*
%{_iconsdir}/hicolor/*/apps/akregator_empty.*
%{_datadir}/knotifications6/akregator.notifyrc
%{_datadir}/qlogging-categories6/akregator.categories
%{_datadir}/qlogging-categories6/akregator.renamecategories
%{_datadir}/metainfo/org.kde.akregator.appdata.xml
%{_datadir}/dbus-1/interfaces/org.kde.akregator.part.xml
%{_qtdir}/plugins/pim6/kontact/kontact_akregatorplugin.so
%{_qtdir}/plugins/pim6/kcms/akregator
%{_qtdir}/plugins/akregatorpart.so

#----------------------------------------------------------------------------

%define akregatorinterfaces_major 6
%define libakregatorinterfaces %mklibname akregatorinterfaces %{akregatorinterfaces_major}

%package -n %{libakregatorinterfaces}
Summary:	KDE PIM shared library
Group:		System/Libraries

%description -n %{libakregatorinterfaces}
KDE PIM shared library.

%files -n %{libakregatorinterfaces}
%{_libdir}/libakregatorinterfaces.so.%{akregatorinterfaces_major}*

#----------------------------------------------------------------------------

%define akregatorprivate_major 6
%define libakregatorprivate %mklibname akregatorprivate %{akregatorprivate_major}

%package -n %{libakregatorprivate}
Summary:	KDE PIM shared library
Group:		System/Libraries

%description -n %{libakregatorprivate}
KDE PIM shared library.

%files -n %{libakregatorprivate}
%{_libdir}/libakregatorprivate.so.%{akregatorprivate_major}*
