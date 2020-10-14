Name:           rustc
Version:        1.47.0
Release:        69
Summary:        The Rust Programming Language
License:        Apache-2.0 BSD-2-Clause BSD-3-Clause ISC MIT
URL:            https://www.rust-lang.org
Source0:        https://static.rust-lang.org/dist/rust-1.47.0-x86_64-unknown-linux-gnu.tar.gz

Requires:       binutils
Requires:       gcc
Requires:       gcc-dev
Requires:       libc6-dev
Provides:       libLLVM-11-rust-%{version}-stable.so()(64bit)
Provides:       libLLVM-11-rust-%{version}-stable.so(LLVM_11)(64bit)
Provides:       librustc_driver-ff4ec557f69b94a7.so()(64bit)
Provides:       librustc_derive-8c5c69f492ead449.so()(64bit)
Provides:       librustc_macros-1e9f2ea5bcbf04e7.so()(64bit)
Provides:       libstd-f14aca24435a5414.so()(64bit)
Provides:       libtest-1a99bd050f5bcac9.so()(64bit)
Provides:       libtracing_attributes-72c431a73c36fa6b.so()(64bit)
Provides:       cargo


%description
Rust is a systems programming language that runs blazingly fast, prevents
segfaults, and guarantees thread safety.

%prep

%setup -q -n rust-%{version}-x86_64-unknown-linux-gnu

%install
install -d %{buildroot}/usr/bin
install -d %{buildroot}/usr/share/bash-completion/completions
install -d %{buildroot}/usr/share/package-licenses
install -d %{buildroot}/usr/share/man/man1
install -d %{buildroot}/usr/lib/rustlib
install -d %{buildroot}/usr/lib64/rustlib/x86_64-unknown-linux-gnu/lib
install cargo/bin/cargo %{buildroot}/usr/bin
install cargo/etc/bash_completion.d/cargo %{buildroot}/usr/share/bash-completion/completions
install rustc/bin/rust-gdb %{buildroot}/usr/bin
install rustc/bin/rust-lldb %{buildroot}/usr/bin
install rustc/bin/rustc %{buildroot}/usr/bin
install rustc/bin/rustdoc %{buildroot}/usr/bin
install rustc/share/man/man1/rustc.1 %{buildroot}/usr/share/man/man1
install rustc/share/man/man1/rustdoc.1 %{buildroot}/usr/share/man/man1
cp -a cargo/share/man/man1/* %{buildroot}/usr/share/man/man1
cp -a cargo/share/doc/cargo %{buildroot}/usr/share/package-licenses/cargo
cp -a cargo/share/zsh %{buildroot}/usr/share
# Location is for rust-gdb to set path of python scripts
cp -a rustc/lib/rustlib/etc %{buildroot}/usr/lib/rustlib
cp -a rustc/lib/rustlib/x86_64-unknown-linux-gnu %{buildroot}/usr/lib64/rustlib
cp -a rustc/lib/*.so %{buildroot}/usr/lib64
cp -a rustc/share/doc/rust %{buildroot}/usr/share/package-licenses/rustc
cp -a rust-std-x86_64-unknown-linux-gnu/lib/rustlib/x86_64-unknown-linux-gnu/lib/* %{buildroot}/usr/lib64/rustlib/x86_64-unknown-linux-gnu/lib

chmod a-x %{buildroot}/usr/share/man/man1/*
chmod a-x %{buildroot}/usr/share/package-licenses/*/*

%files
/usr/bin/cargo
/usr/bin/rust-gdb
/usr/bin/rust-lldb
/usr/bin/rustc
/usr/bin/rustdoc
/usr/lib64/*.so
/usr/lib/rustlib/etc/*
/usr/lib64/rustlib/x86_64-unknown-linux-gnu/bin/rust-lld
/usr/lib64/rustlib/x86_64-unknown-linux-gnu/lib/*.a
/usr/lib64/rustlib/x86_64-unknown-linux-gnu/lib/*.rlib
/usr/lib64/rustlib/x86_64-unknown-linux-gnu/lib/*.so
/usr/share/bash-completion/completions/cargo
/usr/share/package-licenses/cargo/*
/usr/share/package-licenses/rustc/*
/usr/share/man/man1/*.1
/usr/share/zsh/site-functions/_cargo
