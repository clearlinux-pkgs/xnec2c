#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure_ac
# autospec version: v10
# autospec commit: 5905be9
#
Name     : xnec2c
Version  : 4.4.16
Release  : 8
URL      : https://www.xnec2c.org/releases/xnec2c-v4.4.16.tar.gz
Source0  : https://www.xnec2c.org/releases/xnec2c-v4.4.16.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: xnec2c-bin = %{version}-%{release}
Requires: xnec2c-data = %{version}-%{release}
Requires: xnec2c-license = %{version}-%{release}
Requires: xnec2c-man = %{version}-%{release}
BuildRequires : gettext
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gmodule-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(openblas)
BuildRequires : sed
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Please read the user manual in the doc/ directory

%package bin
Summary: bin components for the xnec2c package.
Group: Binaries
Requires: xnec2c-data = %{version}-%{release}
Requires: xnec2c-license = %{version}-%{release}

%description bin
bin components for the xnec2c package.


%package data
Summary: data components for the xnec2c package.
Group: Data

%description data
data components for the xnec2c package.


%package doc
Summary: doc components for the xnec2c package.
Group: Documentation
Requires: xnec2c-man = %{version}-%{release}

%description doc
doc components for the xnec2c package.


%package license
Summary: license components for the xnec2c package.
Group: Default

%description license
license components for the xnec2c package.


%package man
Summary: man components for the xnec2c package.
Group: Default

%description man
man components for the xnec2c package.


%prep
%setup -q -n xnec2c-v4.4.16
cd %{_builddir}/xnec2c-v4.4.16
pushd ..
cp -a xnec2c-v4.4.16 buildavx2
popd
pushd ..
cp -a xnec2c-v4.4.16 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1714067216
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%reconfigure --disable-static
make  %{?_smp_mflags}
unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%reconfigure --disable-static
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx512/
GOAMD64=v4
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -Wl,-z,x86-64-v4 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -Wl,-z,x86-64-v4 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -Wl,-z,x86-64-v4 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v4 -mprefer-vector-width=256 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v4 "
%reconfigure --disable-static
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :
cd ../buildavx512;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1714067216
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xnec2c
cp %{_builddir}/xnec2c-v%{version}/COPYING %{buildroot}/usr/share/package-licenses/xnec2c/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v4
pushd ../buildavx512/
%make_install_v4
popd
GOAMD64=v2
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/xnec2c
/V4/usr/bin/xnec2c
/usr/bin/xnec2c

%files data
%defattr(-,root,root,-)
/usr/share/applications/xnec2c.desktop
/usr/share/icons/hicolor/256x256/apps/xnec2c.png
/usr/share/mime-packages/x-nec2.xml
/usr/share/pixmaps/xnec2c.svg
/usr/share/xnec2c/examples/10-20m-moxon.nec
/usr/share/xnec2c/examples/10-30m-box.nec
/usr/share/xnec2c/examples/10-30m_MultiBand_Vertical.nec
/usr/share/xnec2c/examples/10-30m_bipyramid.nec
/usr/share/xnec2c/examples/10-30m_inv_cone.nec
/usr/share/xnec2c/examples/10-30m_sphere.nec
/usr/share/xnec2c/examples/10-40m_windom.nec
/usr/share/xnec2c/examples/10-80m_Classic_Windom-optimized.nec
/usr/share/xnec2c/examples/10-80m_G5RV.nec
/usr/share/xnec2c/examples/10-80m_Inverted-L.nec
/usr/share/xnec2c/examples/10-80m_windom.nec
/usr/share/xnec2c/examples/137MHz_broadside_Yagi.nec
/usr/share/xnec2c/examples/137MHz_turnstile.nec
/usr/share/xnec2c/examples/137MHz_turnstile_sloped.nec
/usr/share/xnec2c/examples/137Mhz-QFHA1.nec
/usr/share/xnec2c/examples/137Mhz-QFHA2.nec
/usr/share/xnec2c/examples/137Mhz-QFHA3.nec
/usr/share/xnec2c/examples/137Mhz_xpol_omni.nec
/usr/share/xnec2c/examples/13cm_Yagi.nec
/usr/share/xnec2c/examples/13cm_corner_reflector.nec
/usr/share/xnec2c/examples/13cm_helix+screen.nec
/usr/share/xnec2c/examples/15m_delta-loop.nec
/usr/share/xnec2c/examples/1MHz_3x_helicone.nec
/usr/share/xnec2c/examples/1MHz_3x_helisphere.nec
/usr/share/xnec2c/examples/1MHz_4x_helisphere.nec
/usr/share/xnec2c/examples/1MHz_helivert.nec
/usr/share/xnec2c/examples/1MHz_tower.nec
/usr/share/xnec2c/examples/20-40m_ground_plane.nec
/usr/share/xnec2c/examples/20-40m_vert_circ_cliff.nec
/usr/share/xnec2c/examples/20-40m_vert_linear_cliff.nec
/usr/share/xnec2c/examples/20-40m_vert_sommerfeld_cliff.nec
/usr/share/xnec2c/examples/20m_car_ant.nec
/usr/share/xnec2c/examples/20m_quad.nec
/usr/share/xnec2c/examples/23cm_helix+radials.nec
/usr/share/xnec2c/examples/23cm_helix+screen.nec
/usr/share/xnec2c/examples/2m_1to4l-gp_on_pole.nec
/usr/share/xnec2c/examples/2m_1to4l-horiz_gp_on_pole.nec
/usr/share/xnec2c/examples/2m_5to8l-gp_on_pole.nec
/usr/share/xnec2c/examples/2m_EME_ant.nec
/usr/share/xnec2c/examples/2m_Lindenblad.nec
/usr/share/xnec2c/examples/2m_bigwheel.nec
/usr/share/xnec2c/examples/2m_extended_Xpol_yagi-2-optimized.nec
/usr/share/xnec2c/examples/2m_extended_Xpol_yagi-2.nec
/usr/share/xnec2c/examples/2m_extended_Xpol_yagi.nec
/usr/share/xnec2c/examples/2m_extended_yagi-optimized.nec
/usr/share/xnec2c/examples/2m_extended_yagi.nec
/usr/share/xnec2c/examples/2m_halo_stack.nec
/usr/share/xnec2c/examples/2m_sqr_halo.nec
/usr/share/xnec2c/examples/2m_sqr_halo_stack.nec
/usr/share/xnec2c/examples/2m_xpol_omni.nec
/usr/share/xnec2c/examples/2m_xpol_omni_stack.nec
/usr/share/xnec2c/examples/2m_yagi.nec
/usr/share/xnec2c/examples/2m_yagi_stack.nec
/usr/share/xnec2c/examples/30-80m_inv_L.nec
/usr/share/xnec2c/examples/35-55MHz_logper.nec
/usr/share/xnec2c/examples/40-80m_Inv_L.nec
/usr/share/xnec2c/examples/40m-moxon.nec
/usr/share/xnec2c/examples/6-17m_bipyramid.nec
/usr/share/xnec2c/examples/6-20m_fan.nec
/usr/share/xnec2c/examples/6-20m_inv_cone.nec
/usr/share/xnec2c/examples/6-40m_5B4AZ-optimized.nec
/usr/share/xnec2c/examples/6-40m_Classic_Windom-optimized.nec
/usr/share/xnec2c/examples/6m_big-square_stack.nec
/usr/share/xnec2c/examples/6m_bigwheel-stack.nec
/usr/share/xnec2c/examples/6m_horizomni.nec
/usr/share/xnec2c/examples/70cm_collinear.nec
/usr/share/xnec2c/examples/80m_zepp.nec
/usr/share/xnec2c/examples/T12m-H24m.nec
/usr/share/xnec2c/examples/T20m-H18m.nec
/usr/share/xnec2c/examples/airplane.nec
/usr/share/xnec2c/examples/buoy.nec
/usr/share/xnec2c/examples/conductivity.txt
/usr/share/xnec2c/examples/data/10-20m-moxon.csv
/usr/share/xnec2c/examples/data/10-30m-box.csv
/usr/share/xnec2c/examples/data/10-30m_MultiBand_Vertical.csv
/usr/share/xnec2c/examples/data/10-30m_bipyramid.csv
/usr/share/xnec2c/examples/data/10-30m_inv_cone.csv
/usr/share/xnec2c/examples/data/10-30m_sphere.csv
/usr/share/xnec2c/examples/data/10-40m_windom.csv
/usr/share/xnec2c/examples/data/10-80m_Classic_Windom-optimized.csv
/usr/share/xnec2c/examples/data/10-80m_G5RV.csv
/usr/share/xnec2c/examples/data/10-80m_Inverted-L.csv
/usr/share/xnec2c/examples/data/10-80m_windom.csv
/usr/share/xnec2c/examples/data/137MHz_broadside_Yagi.csv
/usr/share/xnec2c/examples/data/137MHz_turnstile.csv
/usr/share/xnec2c/examples/data/137MHz_turnstile_sloped.csv
/usr/share/xnec2c/examples/data/137Mhz-QFHA1.csv
/usr/share/xnec2c/examples/data/137Mhz-QFHA2.csv
/usr/share/xnec2c/examples/data/137Mhz-QFHA3.csv
/usr/share/xnec2c/examples/data/137Mhz_xpol_omni.csv
/usr/share/xnec2c/examples/data/13cm_Yagi.csv
/usr/share/xnec2c/examples/data/13cm_corner_reflector.csv
/usr/share/xnec2c/examples/data/13cm_helix+screen.csv
/usr/share/xnec2c/examples/data/15m_delta-loop.csv
/usr/share/xnec2c/examples/data/1MHz_3x_helicone.csv
/usr/share/xnec2c/examples/data/1MHz_3x_helisphere.csv
/usr/share/xnec2c/examples/data/1MHz_4x_helisphere.csv
/usr/share/xnec2c/examples/data/1MHz_helivert.csv
/usr/share/xnec2c/examples/data/1MHz_tower.csv
/usr/share/xnec2c/examples/data/20-40m_ground_plane.csv
/usr/share/xnec2c/examples/data/20-40m_vert_circ_cliff.csv
/usr/share/xnec2c/examples/data/20-40m_vert_linear_cliff.csv
/usr/share/xnec2c/examples/data/20-40m_vert_sommerfeld_cliff.csv
/usr/share/xnec2c/examples/data/20m_car_ant.csv
/usr/share/xnec2c/examples/data/20m_quad.csv
/usr/share/xnec2c/examples/data/23cm_helix+radials.csv
/usr/share/xnec2c/examples/data/23cm_helix+screen.csv
/usr/share/xnec2c/examples/data/2m_1to4l-gp_on_pole.csv
/usr/share/xnec2c/examples/data/2m_1to4l-horiz_gp_on_pole.csv
/usr/share/xnec2c/examples/data/2m_5to8l-gp_on_pole.csv
/usr/share/xnec2c/examples/data/2m_EME_ant.csv
/usr/share/xnec2c/examples/data/2m_Lindenblad.csv
/usr/share/xnec2c/examples/data/2m_bigwheel.csv
/usr/share/xnec2c/examples/data/2m_extended_Xpol_yagi-2-optimized.csv
/usr/share/xnec2c/examples/data/2m_extended_Xpol_yagi-2.csv
/usr/share/xnec2c/examples/data/2m_extended_Xpol_yagi.csv
/usr/share/xnec2c/examples/data/2m_extended_yagi-optimized.csv
/usr/share/xnec2c/examples/data/2m_extended_yagi.csv
/usr/share/xnec2c/examples/data/2m_halo_stack.csv
/usr/share/xnec2c/examples/data/2m_sqr_halo.csv
/usr/share/xnec2c/examples/data/2m_sqr_halo_stack.csv
/usr/share/xnec2c/examples/data/2m_xpol_omni.csv
/usr/share/xnec2c/examples/data/2m_xpol_omni_stack.csv
/usr/share/xnec2c/examples/data/2m_yagi.csv
/usr/share/xnec2c/examples/data/2m_yagi_stack.csv
/usr/share/xnec2c/examples/data/30-80m_inv_L.csv
/usr/share/xnec2c/examples/data/35-55MHz_logper.csv
/usr/share/xnec2c/examples/data/40-80m_Inv_L.csv
/usr/share/xnec2c/examples/data/40m-moxon.csv
/usr/share/xnec2c/examples/data/6-17m_bipyramid.csv
/usr/share/xnec2c/examples/data/6-20m_fan.csv
/usr/share/xnec2c/examples/data/6-20m_inv_cone.csv
/usr/share/xnec2c/examples/data/6-40m_5B4AZ-optimized.csv
/usr/share/xnec2c/examples/data/6-40m_Classic_Windom-optimized.csv
/usr/share/xnec2c/examples/data/6m_big-square_stack.csv
/usr/share/xnec2c/examples/data/6m_bigwheel-stack.csv
/usr/share/xnec2c/examples/data/6m_horizomni.csv
/usr/share/xnec2c/examples/data/70cm_collinear.csv
/usr/share/xnec2c/examples/data/80m_zepp.csv
/usr/share/xnec2c/examples/data/README
/usr/share/xnec2c/examples/data/T12m-H24m.csv
/usr/share/xnec2c/examples/data/T20m-H18m.csv
/usr/share/xnec2c/examples/data/airplane.csv
/usr/share/xnec2c/examples/data/buoy.csv
/usr/share/xnec2c/examples/data/gray_hoverman.csv
/usr/share/xnec2c/examples/data/k9ay_5b4az.csv
/usr/share/xnec2c/examples/data/k9ay_orig.csv
/usr/share/xnec2c/examples/data/satellite.csv
/usr/share/xnec2c/examples/gray_hoverman.nec
/usr/share/xnec2c/examples/ground.txt
/usr/share/xnec2c/examples/k9ay_5b4az.nec
/usr/share/xnec2c/examples/k9ay_orig.nec
/usr/share/xnec2c/examples/satellite.nec

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/xnec2c/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xnec2c/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/xnec2c.1
