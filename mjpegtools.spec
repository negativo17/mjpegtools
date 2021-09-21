Name:           mjpegtools
Version:        2.2.1
Release:        1%{?dist}
Summary:        Tools to manipulate MPEG data
License:        GPLv2
URL:            http://mjpeg.sourceforge.net/

Source0:        https://downloads.sourceforge.net/sourceforge/mjpeg/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  nasm
BuildRequires:  pkgconfig(libdv) >= 0.9
BuildRequires:  pkgconfig(sdl) >= 1.1.3
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.4.0
BuildRequires:  libtool

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       %{name}-lav%{?_isa} = %{version}-%{release}
# ffmpeg + which for anytovcd.sh
Requires:       ffmpeg
Requires:       which

Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info

%description
The mjpeg programs are a set of tools that can do recording of videos and
playback, simple cut-and-paste editing and the MPEG compression of audio and
video under Linux.

This package contains mjpegtools console utilities.

%package        gui
Summary:        GUI tools to manipulate MPEG data
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    gui
The mjpeg programs are a set of tools that can do recording of videos and
playback, simple cut-and-paste editing and the MPEG compression of audio and
video under Linux.

This package contains mjpegtools GUI utilities.

%package        libs
Summary:        MJPEGtools libraries

%description    libs
The mjpeg programs are a set of tools that can do recording of videos and
playback, simple cut-and-paste editing and the MPEG compression of audio and
video under Linux.

This package contains libraries which are used by %{name} and also by several
other projects.

%package        lav
Summary:        MJPEGtools lavpipe libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    lav
The mjpeg programs are a set of tools that can do recording of videos and
playback, simple cut-and-paste editing and the MPEG compression of audio and
video under Linux.

This package contains libraries used by %{name}.

%package        devel
Summary:        Development files for mjpegtools libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
The mjpeg programs are a set of tools that can do recording of videos and
playback, simple cut-and-paste editing and the MPEG compression of audio and
video under Linux.

This package contains development files for building applications that use
%{name} libraries.

%package        lav-devel
Summary:        Development files for mjpegtools lavpipe libraries
Requires:       %{name}-lav%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description    lav-devel
The mjpeg programs are a set of tools that can do recording of videos and
playback, simple cut-and-paste editing and the MPEG compression of audio and
video under Linux.

This package contains development files for building applications that use
%{name} lavpipe libraries.

%prep 
%autosetup -p1

sed -i -e 's/ARCHFLAGS=.*/ARCHFLAGS=/g' configure*
for f in docs/yuvfps.1 ; do
    iconv -f iso-8859-1 -t utf-8 $f > $f.utf8 ; mv $f.utf8 $f
done

%build
autoreconf -vif
%configure \
  --disable-static \
  --with-dga \
  --with-gtk \
  --with-libdv \
  --with-libpng \
  --with-libquicktime \
  --with-libsdl \
  --with-v4l \
  --without-sdlgfx

%make_build

%install
%make_install
find %{buildroot} -name "*.la" -delete
rm -f %{buildroot}%{_infodir}/dir

rm %{buildroot}%{_bindir}/mpegtranscode
rm %{buildroot}%{_bindir}/lav2avi.sh

%post
/sbin/install-info %{_infodir}/mjpeg-howto.info %{_infodir}/dir || :

%preun
[ $1 -eq 0 ] && \
/sbin/install-info --delete %{_infodir}/mjpeg-howto.info %{_infodir}/dir || :

%ldconfig_scriptlets libs
%ldconfig_scriptlets lav

%files
%doc CHANGES ChangeLog AUTHORS BUGS README.lavpipe NEWS TODO
%{_bindir}/anytovcd.sh
%{_bindir}/jpeg2yuv
%{_bindir}/lav2mpeg
%{_bindir}/lav2wav
%{_bindir}/lav2yuv
%{_bindir}/lavaddwav
%{_bindir}/lavinfo
%{_bindir}/lavpipe
%{_bindir}/lavtc.sh
%{_bindir}/lavtrans
%{_bindir}/matteblend.flt
%{_bindir}/mjpeg_simd_helper
%{_bindir}/mp2enc
%{_bindir}/mpeg2enc
%{_bindir}/mplex
%{_bindir}/multiblend.flt
%{_bindir}/pgmtoy4m
%{_bindir}/png2yuv
%{_bindir}/pnmtoy4m
%{_bindir}/ppmtoy4m
%{_bindir}/transist.flt
%{_bindir}/y4mblack
%{_bindir}/y4mcolorbars
%{_bindir}/y4mdenoise
%{_bindir}/y4minterlace
%{_bindir}/y4mivtc
%{_bindir}/y4mscaler
%{_bindir}/y4mshift
%{_bindir}/y4mspatialfilter
%{_bindir}/y4mstabilizer
%{_bindir}/y4mtopnm
%{_bindir}/y4mtoppm
%{_bindir}/y4mtoyuv
%{_bindir}/y4munsharp
%{_bindir}/ypipe
%{_bindir}/yuv2lav
%{_bindir}/yuv4mpeg
%{_bindir}/yuvcorrect
%{_bindir}/yuvcorrect_tune
%{_bindir}/yuvdeinterlace
%{_bindir}/yuvdenoise
%{_bindir}/yuvfps
%{_bindir}/yuvinactive
%{_bindir}/yuvkineco
%{_bindir}/yuvmedianfilter
%{_bindir}/yuvscaler
%{_bindir}/yuvycsnoise
%{_bindir}/yuyvtoy4m
%{_infodir}/mjpeg-howto.info*
%{_mandir}/man1/*.1*
%{_mandir}/man1/jpeg2yuv.1.gz
%{_mandir}/man1/lav2mpeg.1.gz
%{_mandir}/man1/lav2wav.1.gz
%{_mandir}/man1/lav2yuv.1.gz
%{_mandir}/man1/lavpipe.1.gz
%{_mandir}/man1/lavrec.1.gz
%{_mandir}/man1/lavtrans.1.gz
%{_mandir}/man1/mjpegtools.1.gz
%{_mandir}/man1/mp2enc.1.gz
%{_mandir}/man1/mpeg2enc.1.gz
%{_mandir}/man1/mplex.1.gz
%{_mandir}/man1/pgmtoy4m.1.gz
%{_mandir}/man1/png2yuv.1.gz
%{_mandir}/man1/pnmtoy4m.1.gz
%{_mandir}/man1/ppmtoy4m.1.gz
%{_mandir}/man1/y4mcolorbars.1.gz
%{_mandir}/man1/y4mdenoise.1.gz
%{_mandir}/man1/y4mscaler.1.gz
%{_mandir}/man1/y4mtopnm.1.gz
%{_mandir}/man1/y4mtoppm.1.gz
%{_mandir}/man1/y4munsharp.1.gz
%{_mandir}/man1/yuv2lav.1.gz
%{_mandir}/man1/yuvdenoise.1.gz
%{_mandir}/man1/yuvfps.1.gz
%{_mandir}/man1/yuvinactive.1.gz
%{_mandir}/man1/yuvkineco.1.gz
%{_mandir}/man1/yuvmedianfilter.1.gz
%{_mandir}/man1/yuvscaler.1.gz
%{_mandir}/man1/yuvycsnoise.1.gz
%{_mandir}/man5/yuv4mpeg.5.gz

%files gui
%doc README.glav
%{_bindir}/glav
# lavplay and yuvplay won't save console util users from X11 and SDL
# dependencies as long as liblavplay is in -lav, but they're inherently
# GUI tools -> include them here
%{_bindir}/lavplay
%{_bindir}/y4mhist
%{_bindir}/yuvplay
%{_mandir}/man1/lavplay.1*
%{_mandir}/man1/yuvplay.1*

%files libs
%license COPYING
%{_libdir}/libm*.so.*

%files lav
%license COPYING
%{_libdir}/liblav*.so.*

%files devel
%{_includedir}/%{name}
%exclude %{_includedir}/%{name}/*lav*.h
%{_libdir}/libm*.so
%{_libdir}/pkgconfig/%{name}.pc

%files lav-devel
%{_includedir}/%{name}/*lav*.h
%{_libdir}/liblav*.so

%changelog
* Fri Sep 17 2021 Simone Caronni <negativo17@gmail.com> - 2.2.1-1
- Update to 2.2.1.

* Fri Apr 03 2020 Simone Caronni <negativo17@gmail.com> - 2.1.0-10
- Disable libquicktime support in tools.

* Sun Jan 19 2020 Simone Caronni <negativo17@gmail.com> - 2.1.0-9
- Disable SDL_gfx and use ldconfig macros.

* Thu Sep 27 2018 Simone Caronni <negativo17@gmail.com> - 2.1.0-8
- Add GCC as build requirement.

* Sun Jan 08 2017 Simone Caronni <negativo17@gmail.com> - 2.1.0-7
- Remove lav2avi.sh script and mencoder dependency.

* Sun Jun 05 2016 Simone Caronni <negativo17@gmail.com> - 2.1.0-6
- Clean up SPEC file.
- Explicitly declare binaries in the SPEC file.

* Sun Oct 19 2014 Sérgio Basto <sergio@serjux.com> - 2.1.0-5
- Rebuilt for FFmpeg 2.4.3
