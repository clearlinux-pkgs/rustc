PKG_NAME := rustc
URL = https://static.rust-lang.org/dist/rustc-1.66.1-src.tar.gz
ARCHIVES = https://github.com/llvm/llvm-project/releases/download/llvmorg-15.0.6/compiler-rt-15.0.6.src.tar.xz ./compiler-rt

include ../common/Makefile.common
