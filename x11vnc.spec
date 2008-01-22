Summary:	A VNC server for the current X11 session
Summary(pl.UTF-8):	Program serwujący aktualną sesję X11 poprzez VNC
Name:		x11vnc
Version:	0.9.3
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://www.karlrunge.com/x11vnc/%{name}-%{version}.tar.gz
# Source0-md5:	868d2be5c8d4f116e89b8573db435889
Source1:	%{name}-x11vncd
Source2:	%{name}-x11vncd.init
Source3:	%{name}-x11vncd.sysconfig
Source4:	%{name}-x11vncd_passwd
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

%description -l pl.UTF-8
x11vnc jest dla X Window System tym, czym jest WinVNC dla Windows,
czyli programem udostępniającym aktualny ekran X Window System poprzez
protokół RFB (VNC) dla użytkownika.

Bazuje na pomyśle x0rfbserver i LibVNCServer, został stworzony jako
wszechstronny i wydajny, ale także łatwy w użyciu.

%package init
Summary:	Init scripts for VNC server.
Summary(pl.UTF-8):	Skrytpy startowe dla servera VNC.
Group:		X11/Applications/Networking
Requires:	x11vnc

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

cp %{SOURCE1} $RPM_BUILD_ROOT%{_sbindir}/x11vncd
cp %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/x11vncd
cp %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/x11vncd
cp %{SOURCE4} $RPM_BUILD_ROOT/etc/x11vncd_passwd

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
%doc README NEWS TODO ChangeLog AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*

%files init
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/x11vncd
%attr(755,root,root) /etc/rc.d/init.d/x11vncd
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/x11vncd
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/x11vncd_passwd
