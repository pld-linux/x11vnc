Summary:	A VNC server for the current X11 session
Summary(pl.UTF-8):	Program serwujący aktualną sesję X11 poprzez VNC
Name:		x11vnc
Version:	0.9.16
Release:	1
License:	GPL v2+
Group:		X11/Applications/Networking
#Source0Download: https://github.com/LibVNC/x11vnc/releases
Source0:	https://github.com/LibVNC/x11vnc/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	64172e8f896389ec963fff93415f0d93
Source1:	%{name}-x11vncd
Source2:	%{name}-x11vncd.init
Source3:	%{name}-x11vncd.sysconfig
Source4:	%{name}-x11vncd_passwd
URL:		https://github.com/LibVNC/x11vnc/
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	avahi-devel >= 0.6.4
BuildRequires:	cairo-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libvncserver-devel >= 0.9.8
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXi-devel >= 1.3
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xorg-proto-inputproto-devel >= 2
BuildRequires:	zlib-devel
Requires:	avahi-libs >= 0.6.4
Requires:	libvncserver >= 0.9.8
Requires:	xorg-lib-libXi >= 1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
x11vnc is to X Window System what WinVNC is to Windows, i.e. a server
which serves the current X Window System desktop via RFB (VNC)
protocol to the user.

Based on the ideas of x0rfbserver and on LibVNCServer, it has evolved
into a versatile and performant while still easy to use program.

%description -l pl.UTF-8
x11vnc jest dla X Window System tym, czym jest WinVNC dla Windows,
czyli programem udostępniającym aktualny ekran X Window System poprzez
protokół RFB (VNC) dla użytkownika.

Bazuje na pomyśle x0rfbserver i LibVNCServer, został stworzony jako
wszechstronny i wydajny, ale także łatwy w użyciu.

%package init
Summary:	Init scripts for VNC server
Summary(pl.UTF-8):	Skrytpy startowe dla servera VNC.
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}

%description init
Init scripts for VNC server.

%description init -l pl.UTF-8
Skrytpy startowe dla servera VNC.

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

install -d $RPM_BUILD_ROOT%{_sbindir} \
	$RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig}

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_sbindir}/x11vncd
cp -p %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/x11vncd
cp -p %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/x11vncd
cp -p %{SOURCE4} $RPM_BUILD_ROOT/etc/x11vncd_passwd

%clean
rm -rf $RPM_BUILD_ROOT

%post init
/sbin/chkconfig --add x11vncd
%service x11vncd restart "VNC Server"

%preun init
if [ "$1" = "0" ]; then
	%service x11vncd stop
	/sbin/chkconfig --del x11vncd
fi

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/Xdummy
%attr(755,root,root) %{_bindir}/x11vnc
%{_desktopdir}/x11vnc.desktop
%{_mandir}/man1/x11vnc.1*

%files init
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/x11vncd
%attr(754,root,root) /etc/rc.d/init.d/x11vncd
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/x11vncd
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/x11vncd_passwd
