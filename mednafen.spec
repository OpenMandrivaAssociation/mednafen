Summary:	Multi-consoles Emulator
Name:		mednafen
Version:	0.9.36.4
Release:	2
License:	GPLv2+
Group:		Emulators
Url:		https://mednafen.sourceforge.net/
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	bison
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libcdio)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	SDL_net-devel
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(zlib)

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

%files -f %{name}.lang
%doc ABOUT-NLS AUTHORS COPYING ChangeLog TODO Documentation/*
%{_bindir}/%{name}
%{_datadir}/%{name}/c68k_op0.inc

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}
find ./src -type f -exec chmod 644 '{}' +
find ./src -type d -exec chmod 755 '{}' +

%build
autoreconf -i
CFLAGS="-O2 -mtune=atom" CXXFLAGS="-O2 -mtune=atom" %configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name}

