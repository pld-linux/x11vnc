Summary:	A VNC server for the current X11 session
Summary(pl):	Program serwuj�cy aktualn� sesj� X11 poprzez VNC
Name:		x11vnc
Version:	0.8.4
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://www.karlrunge.com/x11vnc/%{name}-%{version}.tar.gz
# Source0-md5:	ba5273a480f3c3ee2e676710f9d230b2
URL:		http://www.karlrunge.com/x11vnc/
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	openssl-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXTrap-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
x11vnc is to X Window System what WinVNC is to Windows, i.e. a server
which serves the current X Window System desktop via RFB (VNC)
protocol to the user.

Based on the ideas of x0rfbserver and on LibVNCServer, it has evolved
into a versatile and performant while still easy to use program.

%description -l pl
x11vnc jest dla X Window System tym, czym jest WinVNC dla Windows,
czyli programem udost�pniaj�cym aktualny ekran X Window System poprzez
protok� RFB (VNC) dla u�ytkownika.

Bazuje na pomy�le x0rfbserver i LibVNCServer, zosta� stworzony jako
wszechstronny i wydajny, ale tak�e �atwy w u�yciu.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-x

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS TODO ChangeLog AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*
