#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libsodium
Version  : 1.0.6
Release  : 7
URL      : https://download.libsodium.org/libsodium/releases/libsodium-1.0.6.tar.gz
Source0  : https://download.libsodium.org/libsodium/releases/libsodium-1.0.6.tar.gz
Summary  : A portable, cross-compilable, installable, packageable fork of NaCl, with a compatible API.
Group    : Development/Tools
License  : HPND
Requires: libsodium-lib

%description


%package dev
Summary: dev components for the libsodium package.
Group: Development
Requires: libsodium-lib
Provides: libsodium-devel

%description dev
dev components for the libsodium package.


%package lib
Summary: lib components for the libsodium package.
Group: Libraries

%description lib
lib components for the libsodium package.


%prep
%setup -q -n libsodium-1.0.6

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/include/sodium/core.h
/usr/include/sodium/crypto_aead_aes256gcm.h
/usr/include/sodium/crypto_aead_chacha20poly1305.h
/usr/include/sodium/crypto_auth.h
/usr/include/sodium/crypto_auth_hmacsha256.h
/usr/include/sodium/crypto_auth_hmacsha512.h
/usr/include/sodium/crypto_auth_hmacsha512256.h
/usr/include/sodium/crypto_box.h
/usr/include/sodium/crypto_box_curve25519xsalsa20poly1305.h
/usr/include/sodium/crypto_core_hsalsa20.h
/usr/include/sodium/crypto_core_salsa20.h
/usr/include/sodium/crypto_core_salsa2012.h
/usr/include/sodium/crypto_core_salsa208.h
/usr/include/sodium/crypto_generichash.h
/usr/include/sodium/crypto_generichash_blake2b.h
/usr/include/sodium/crypto_hash.h
/usr/include/sodium/crypto_hash_sha256.h
/usr/include/sodium/crypto_hash_sha512.h
/usr/include/sodium/crypto_int32.h
/usr/include/sodium/crypto_int64.h
/usr/include/sodium/crypto_onetimeauth.h
/usr/include/sodium/crypto_onetimeauth_poly1305.h
/usr/include/sodium/crypto_pwhash_scryptsalsa208sha256.h
/usr/include/sodium/crypto_scalarmult.h
/usr/include/sodium/crypto_scalarmult_curve25519.h
/usr/include/sodium/crypto_secretbox.h
/usr/include/sodium/crypto_secretbox_xsalsa20poly1305.h
/usr/include/sodium/crypto_shorthash.h
/usr/include/sodium/crypto_shorthash_siphash24.h
/usr/include/sodium/crypto_sign.h
/usr/include/sodium/crypto_sign_ed25519.h
/usr/include/sodium/crypto_sign_edwards25519sha512batch.h
/usr/include/sodium/crypto_stream.h
/usr/include/sodium/crypto_stream_aes128ctr.h
/usr/include/sodium/crypto_stream_chacha20.h
/usr/include/sodium/crypto_stream_salsa20.h
/usr/include/sodium/crypto_stream_salsa2012.h
/usr/include/sodium/crypto_stream_salsa208.h
/usr/include/sodium/crypto_stream_xsalsa20.h
/usr/include/sodium/crypto_uint16.h
/usr/include/sodium/crypto_uint32.h
/usr/include/sodium/crypto_uint64.h
/usr/include/sodium/crypto_uint8.h
/usr/include/sodium/crypto_verify_16.h
/usr/include/sodium/crypto_verify_32.h
/usr/include/sodium/crypto_verify_64.h
/usr/include/sodium/export.h
/usr/include/sodium/randombytes.h
/usr/include/sodium/randombytes_salsa20_random.h
/usr/include/sodium/randombytes_sysrandom.h
/usr/include/sodium/runtime.h
/usr/include/sodium/utils.h
/usr/include/sodium/version.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
