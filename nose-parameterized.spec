#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nose-parameterized
Version  : 0.5.0
Release  : 3
URL      : http://pypi.debian.net/nose-parameterized/nose-parameterized-0.5.0.tar.gz
Source0  : http://pypi.debian.net/nose-parameterized/nose-parameterized-0.5.0.tar.gz
Summary  : Parameterized testing with any Python test framework
Group    : Development/Tools
License  : BSD-3-Clause
Requires: nose-parameterized-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Parameterized testing with any Python test framework
====================================================

%package python
Summary: python components for the nose-parameterized package.
Group: Default

%description python
python components for the nose-parameterized package.


%prep
%setup -q -n nose-parameterized-0.5.0

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*