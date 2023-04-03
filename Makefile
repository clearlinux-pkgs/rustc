PKG_NAME := rustc
URL = https://static.rust-lang.org/dist/rustc-1.68.2-src.tar.gz
ARCHIVES = https://github.com/llvm/llvm-project/releases/download/llvmorg-15.0.7/compiler-rt-15.0.7.src.tar.xz ./compiler-rt

include ../common/Makefile.common
