PKG_NAME := rustc
URL = https://static.rust-lang.org/dist/rustc-1.60.0-src.tar.gz
ARCHIVES = https://github.com/llvm/llvm-project/releases/download/llvmorg-14.0.3/compiler-rt-14.0.3.src.tar.xz ./compiler-rt

include ../common/Makefile.common
