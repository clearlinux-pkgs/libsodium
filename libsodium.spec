#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v12
# autospec commit: fbcebd0
#
# Source0 file verified with key 0x62F25B592B6F76DA (github@pureftpd.org)
#
Name     : libsodium
Version  : 1.0.20
Release  : 20
URL      : https://github.com/jedisct1/libsodium/releases/download/1.0.20-RELEASE/libsodium-1.0.20.tar.gz
Source0  : https://github.com/jedisct1/libsodium/releases/download/1.0.20-RELEASE/libsodium-1.0.20.tar.gz
Source1  : https://github.com/jedisct1/libsodium/releases/download/1.0.20-RELEASE/libsodium-1.0.20.tar.gz.sig
Source2  : 62F25B592B6F76DA.pkey
Summary  : A modern and easy-to-use crypto library
Group    : Development/Tools
License  : ISC
Requires: libsodium-lib = %{version}-%{release}
Requires: libsodium-license = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : file
BuildRequires : gnupg
BuildRequires : llvm
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
[![GitHub CI](https://github.com/jedisct1/libsodium/workflows/CI/badge.svg)](https://github.com/jedisct1/libsodium/actions)
[![Windows build status](https://ci.appveyor.com/api/projects/status/fu8s2elx25il98hj?svg=true)](https://ci.appveyor.com/project/jedisct1/libsodium)
[![Coverity Scan Build Status](https://scan.coverity.com/projects/2397/badge.svg)](https://scan.coverity.com/projects/2397)
[![Azure build status](https://jedisct1.visualstudio.com/Libsodium/_apis/build/status/jedisct1.libsodium?branchName=stable)](https://jedisct1.visualstudio.com/Libsodium/_build/latest?definitionId=3&branchName=stable)
[![CodeQL scan](https://github.com/jedisct1/libsodium/workflows/CodeQL%20scan/badge.svg)](https://github.com/jedisct1/libsodium/actions)

%package dev
Summary: dev components for the libsodium package.
Group: Development
Requires: libsodium-lib = %{version}-%{release}
Provides: libsodium-devel = %{version}-%{release}
Requires: libsodium = %{version}-%{release}

%description dev
dev components for the libsodium package.


%package lib
Summary: lib components for the libsodium package.
Group: Libraries
Requires: libsodium-license = %{version}-%{release}

%description lib
lib components for the libsodium package.


%package license
Summary: license components for the libsodium package.
Group: Default

%description license
license components for the libsodium package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 62F25B592B6F76DA' gpg.status
%setup -q -n libsodium-1.0.20
cd %{_builddir}/libsodium-1.0.20
pushd ..
cp -a libsodium-1.0.20 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1717427876
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static
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

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1717427876
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libsodium
cp %{_builddir}/libsodium-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/libsodium/5f4c899787127f3591fc51faf0f5621e758910ae || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/sodium.h
/usr/include/sodium/core.h
/usr/include/sodium/crypto_aead_aegis128l.h
/usr/include/sodium/crypto_aead_aegis256.h
/usr/include/sodium/crypto_aead_aes256gcm.h
/usr/include/sodium/crypto_aead_chacha20poly1305.h
/usr/include/sodium/crypto_aead_xchacha20poly1305.h
/usr/include/sodium/crypto_auth.h
/usr/include/sodium/crypto_auth_hmacsha256.h
/usr/include/sodium/crypto_auth_hmacsha512.h
/usr/include/sodium/crypto_auth_hmacsha512256.h
/usr/include/sodium/crypto_box.h
/usr/include/sodium/crypto_box_curve25519xchacha20poly1305.h
/usr/include/sodium/crypto_box_curve25519xsalsa20poly1305.h
/usr/include/sodium/crypto_core_ed25519.h
/usr/include/sodium/crypto_core_hchacha20.h
/usr/include/sodium/crypto_core_hsalsa20.h
/usr/include/sodium/crypto_core_ristretto255.h
/usr/include/sodium/crypto_core_salsa20.h
/usr/include/sodium/crypto_core_salsa2012.h
/usr/include/sodium/crypto_core_salsa208.h
/usr/include/sodium/crypto_generichash.h
/usr/include/sodium/crypto_generichash_blake2b.h
/usr/include/sodium/crypto_hash.h
/usr/include/sodium/crypto_hash_sha256.h
/usr/include/sodium/crypto_hash_sha512.h
/usr/include/sodium/crypto_kdf.h
/usr/include/sodium/crypto_kdf_blake2b.h
/usr/include/sodium/crypto_kdf_hkdf_sha256.h
/usr/include/sodium/crypto_kdf_hkdf_sha512.h
/usr/include/sodium/crypto_kx.h
/usr/include/sodium/crypto_onetimeauth.h
/usr/include/sodium/crypto_onetimeauth_poly1305.h
/usr/include/sodium/crypto_pwhash.h
/usr/include/sodium/crypto_pwhash_argon2i.h
/usr/include/sodium/crypto_pwhash_argon2id.h
/usr/include/sodium/crypto_pwhash_scryptsalsa208sha256.h
/usr/include/sodium/crypto_scalarmult.h
/usr/include/sodium/crypto_scalarmult_curve25519.h
/usr/include/sodium/crypto_scalarmult_ed25519.h
/usr/include/sodium/crypto_scalarmult_ristretto255.h
/usr/include/sodium/crypto_secretbox.h
/usr/include/sodium/crypto_secretbox_xchacha20poly1305.h
/usr/include/sodium/crypto_secretbox_xsalsa20poly1305.h
/usr/include/sodium/crypto_secretstream_xchacha20poly1305.h
/usr/include/sodium/crypto_shorthash.h
/usr/include/sodium/crypto_shorthash_siphash24.h
/usr/include/sodium/crypto_sign.h
/usr/include/sodium/crypto_sign_ed25519.h
/usr/include/sodium/crypto_sign_edwards25519sha512batch.h
/usr/include/sodium/crypto_stream.h
/usr/include/sodium/crypto_stream_chacha20.h
/usr/include/sodium/crypto_stream_salsa20.h
/usr/include/sodium/crypto_stream_salsa2012.h
/usr/include/sodium/crypto_stream_salsa208.h
/usr/include/sodium/crypto_stream_xchacha20.h
/usr/include/sodium/crypto_stream_xsalsa20.h
/usr/include/sodium/crypto_verify_16.h
/usr/include/sodium/crypto_verify_32.h
/usr/include/sodium/crypto_verify_64.h
/usr/include/sodium/export.h
/usr/include/sodium/randombytes.h
/usr/include/sodium/randombytes_internal_random.h
/usr/include/sodium/randombytes_sysrandom.h
/usr/include/sodium/runtime.h
/usr/include/sodium/utils.h
/usr/include/sodium/version.h
/usr/lib64/libsodium.so
/usr/lib64/pkgconfig/libsodium.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libsodium.so.26.2.0
/usr/lib64/libsodium.so.26
/usr/lib64/libsodium.so.26.2.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libsodium/5f4c899787127f3591fc51faf0f5621e758910ae
