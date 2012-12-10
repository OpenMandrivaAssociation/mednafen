Name:		mednafen
Version:	0.9.25
Release:	1

Summary:	Multi-consoles Emulator
License:	GPLv2+
URL:		http://mednafen.sourceforge.net/
Group:		Emulators
Source0:	%{name}-%{version}-wip.tar.bz2
BuildRequires:	bison
BuildRequires:	pkgconfig(libcdio)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(SDL_net)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)

%description
Mednafen emulates several consoles:
-Atari Lynx
-GameBoy (Color)
-GameBoy Advance
-Neo Geo Pocket (Color)
-NES
-SNES
-PC Engine (TurboGrafx 16)
-PC-FX
-Sega Master System & Game Gear
-SuperGrafx
-Virtual Boy
-WonderSwan (Color)

Warning: No GUI.

%prep
%setup -q -n %{name}
find ./src -type f -exec chmod 644 '{}' +
find ./src -type d -exec chmod 755 '{}' +

%build
autoreconf -i
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc ABOUT-NLS AUTHORS COPYING ChangeLog INSTALL TODO Documentation/*
%{_bindir}/%{name}
%{_datadir}/%{name}/c68k_op0.inc

%changelog
* Thu Oct 27 2011 Götz Waschk <waschk@mandriva.org> 0.9.18-2mdv2012.0
+ Revision: 707549
- rebuild for new libcdio

  + Alexander Barakin <abarakin@mandriva.org>
    - imported package mednafen

* Sat Jul 30 2011 Andrey Bondrov <abondrov@mandriva.org> 0.9.17.1-1
+ Revision: 692335
- imported package mednafen


* Thu Jul 21 2011 Andrey Bondrov <bondrov@math.dvgu.ru> 0.9.17.1-1mdv2011.0
- 9.17.1

* Fri Jun 04 2010 Guillaume Bedot <littletux@zarb.org> 0.8.13-1plf2010.1
- 0.8.D

* Sun Apr 19 2009 Guillaume Bedot <littletux@zarb.org> 0.8.11-1plf2009.1
- 0.8.B

* Fri Oct 31 2008 Guillaume Bedot <littletux@zarb.org> 0.8.10-1plf2009.0
- 0.8.A

* Thu Jun 26 2008 Guillaume Bedot <littletux@zarb.org> 0.8.9-1plf2009.0
- 0.8.9

* Thu Apr 17 2008 Guillaume Bedot <littletux@zarb.org> 0.8.8-1plf2009.0
- 0.8.8

* Mon Jan 28 2008 Guillaume Bedot <littletux@zarb.org> 0.8.7-1plf2008.1
- 0.8.7

* Tue Nov 27 2007 Guillaume Bedot <littletux@zarb.org> 0.8.5-1plf2008.1
- 0.8.5

* Tue Aug 14 2007 Guillaume Bedot <littletux@zarb.org> 0.8.4-0.rc1plf2008.0
- 0.8.4-rc1

* Wed May  2 2007 Guillaume Bedot <littletux@zarb.org> 0.8.1-1plf2008.0
- 0.8.1

* Tue Mar 27 2007 Guillaume Bedot <littletux@zarb.org> 0.7.2-1plf2007.1
- 0.7.2

* Sun Sep 09 2006 Guillaume Bedot <littletux@zarb.org> 0.6.5-1plf2007.0
- 0.6.5

* Wed Aug 30 2006 Anssi Hannula <anssi@zarb.org> 0.6.4-2plf2007.0
- fix buildrequires

* Tue Aug 22 2006 Guillaume Bedot <littletux@zarb.org> 0.6.4-1plf2007.0
- 0.6.4
- fix rights on source files

* Fri Aug 11 2006 Guillaume Bedot <littletux@zarb.org> 0.6.3-1plf2007.0
- 0.6.3

* Wed Jul 19 2006 Guillaume Bedot <littletux@zarb.org> 0.6.2-2plf2007.0
- fixed permissions on source, space intead of tabs, clean install

* Mon Jun 26 2006 Guillaume Bedot <littletux@zarb.org> 0.6.2-1plf2007.0
- Release 0.6.2

* Sun May 28 2006 Guillaume Bedot <littletux@zarb.org> 0.6.1-1plf
- Release 0.6.1
- Buildrequires libGL and libGLU devel packages

* Sun Apr 02 2006 Guillaume Bedot <littletux@zarb.org> 0.5.2-2plf
- Rebuild for libcdio7

* Sun Mar 12 2006 Guillaume Bedot <littletux@zarb.org> 0.5.2-1plf
- New version

* Wed Feb 22 2006 Guillaume Bedot <littletux@zarb.org> 0.4.9-1plf
- First package
