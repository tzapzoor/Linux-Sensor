#
# Copyright (C) 2011 Battelle Memorial Institute <http://www.battelle.org>
#
# Author: Brandon Carpenter
#
# This package is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This package is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#

%define package hone

Name: hone-dkms
Summary: DKMS support for Hone packet-process correlation kernel module
Version: 11.12.29+766
Release: 1
License: GPL2
Group: Utilities/Internet
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: dkms >= 2.1.0.0, bash, gcc
Packager: Brandon Carpenter
Source0: %{package}-%{version}.tar.gz

%description
Linux loadable kernel modules for peforming packet-to-process correlation.

%prep
%setup -q -n %{package}-%{version}

%install
if [ "%{buildroot}" != "/" ]; then
	rm -rf %{buildroot}
fi
mkdir -p %{buildroot}/usr/src/%{package}-%{version}
rm -rf debian hone.spec hone.spec.in dkms.conf.in
cp -rf * %{buildroot}/usr/src/%{package}-%{version}

%clean
if [ "%{buildroot}" != "/" ]; then
	rm -rf %{buildroot}
fi

%files
%attr(-,root,root) /usr/src/%{package}-%{version}/

%post
dkms add -m %{package} -v %{version} --rpm_safe_upgrade &&
dkms build -m %{package} -v %{version} &&
dkms install -m %{package} -v %{version}

%preun
dkms remove -m %{package} -v %{version} --all
