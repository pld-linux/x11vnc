Name:		x11vnc
Summary:	a VNC server for the current X11 session
Summary(pl):	Program serwuj�cy aktualn� sesj� X11 poprzez VNC
Version:	0.6.1
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/libvncserver/%{name}-%{version}.tar.gz
BuildRequires:	XFree86-devel
BuildRequires:	libjpeg-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
x11vnc is to Xwindows what WinVNC is to Windows, i.e. a server which
serves the current Xwindows desktop via RFB (VNC) protocol to the
user.
Based on the ideas of x0rfbserver and on LibVNCServer, it has evolved
into a versatile and performant while still easy to use program.

%description -l pl
x11vnc jest tym czym czym jest WinVNC dla windows, czyli programem
udost�pniaj�cym aktualny ekran Xwindow poprzez protok� RFB (VNC) dla
u�ytkownika.
Bazuje na pomysle x0rfbserver i LibVNCServer, zosta� stworzony jako
wszechstronny i wydajny, ale tak�e �atwy w u�yciu.

%prep
%setup -q

%build
%configure

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
