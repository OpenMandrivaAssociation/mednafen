Name:			mednafen
Version:		0.9.18
Release:		%mkrel 2

Summary:	Multi-consoles Emulator
License:	GPLv2+
URL:		http://mednafen.sourceforge.net/
Group:		Emulators
Source0:	%{name}-%{version}-wip.tar.bz2
Patch0:		mednafen-9.17.1-formatfix.patch
BuildRequires:	libcdio-devel
BuildRequires:	libvorbis-devel
BuildRequires:	SDL_net-devel
BuildRequires:	libsndfile-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	zlib-devel
BuildRequires:	bison
BuildRequires:	SDL-devel
BuildRequires:	mesagl-devel
BuildRequires:	mesaglu-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
%patch0 -p1
find ./src -type f -exec chmod 644 '{}' +
find ./src -type d -exec chmod 755 '{}' +

%build
autoreconf -i
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall
%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root)
%doc ABOUT-NLS AUTHORS COPYING ChangeLog INSTALL TODO Documentation/*
%{_bindir}/%{name}
%{_datadir}/%{name}/c68k_op0.inc

%clean
rm -rf %{buildroot}

