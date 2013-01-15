Name:		mednafen
Version:	0.9.28
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

