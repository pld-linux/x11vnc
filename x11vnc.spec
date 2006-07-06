Summary:	A VNC server for the current X11 session
Summary(pl):	Program serwuj±cy aktualn± sesjê X11 poprzez VNC
Name:		x11vnc
Version:	0.8.2
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://www.karlrunge.com/x11vnc/%{name}-%{version}.tar.gz
# Source0-md5:	086e029f3fbe806a31ece558732c8db7
URL:		http://www.karlrunge.com/x11vnc/
BuildRequires:	XFree86-devel
BuildRequires:	libjpeg-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
x11vnc is to X Window System what WinVNC is to Windows, i.e. a server
which serves the current X Window System desktop via RFB (VNC)
protocol to the user.

Based on the ideas of x0rfbserver and on LibVNCServer, it has evolved
into a versatile and performant while still easy to use program.

%description -l pl
x11vnc jest dla X Window System tym, czym czym jest WinVNC dla
Windows, czyli programem udostêpniaj±cym aktualny ekran X Window
System poprzez protokó³ RFB (VNC) dla u¿ytkownika.

Bazuje na pomy¶le x0rfbserver i LibVNCServer, zosta³ stworzony jako
wszechstronny i wydajny, ale tak¿e ³atwy w u¿yciu.

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
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*
