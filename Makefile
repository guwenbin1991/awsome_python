###############################################################################
## File       : Makefile
## Created    : 2021-7-2
## 
## Description:
## 
## This is the top Makefile for the my python project
## 
## It supports to make below targets:
## 
##   - all
## 
##     Same as "build". It is the default target if no target specified.
## 
##   - build
## 
##     Build and generate the executable binary file of PGW simulation program.
## 
##   - clean
## 
##     Remove all the generated objects and files during building.
## 
##   - install
## 
##     Copy the generated executable binary file of PGW simulation program to
##     the package directory.
###############################################################################

## Environment definition
SHELL := /bin/bash

## Sub folders definition
SUBDIRS = src
SUBDIRS_STRING = src/string

## Targets definition
.PHONY: all build_t test install

all:: clean

# install:: $(PKG_SBIN_DIR) $(PKG_SHARE_DIR) $(PKG_ETC_DIR)
# 	@ cp    -f $(TAR_BIN_FDR)/${TARGET_PLATFORM}/gtpgw $(PKG_SBIN_DIR)/gtpgw
# 	@ mkdir -p $(PKG_SHARE_DIR)/templates
# 	@ cp    -f etc/gtpgw/*.template         $(PKG_SHARE_DIR)/templates/
# 	@ cp    -f etc/gtpgwsim                 $(PKG_ETC_DIR)/gtpgwsim

# ## Include package.mk
# include ${MK}/utils/package.mk

## Include subdirs.mk
# include ${MK}/utils/subdirs.mk
clean:
	rm -f $(SUBDIRS)/*.pyc >/dev/null 2>&1
	rm -f $(SUBDIRS_STRING)/*.pyc >/dev/null 2>&1

## Set the default goal
.DEFAULT_GOAL := all
