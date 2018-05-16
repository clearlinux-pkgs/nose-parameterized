#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nose-parameterized
Version  : 0.6.0
Release  : 16
URL      : https://pypi.debian.net/nose-parameterized/nose-parameterized-0.6.0.tar.gz
Source0  : https://pypi.debian.net/nose-parameterized/nose-parameterized-0.6.0.tar.gz
Summary  : Parameterized testing with any Python test framework (DEPRECATED; See the 'parameterized' package)
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause
Requires: nose-parameterized-python3
Requires: nose-parameterized-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
====================================================
        
        DEPRECATION WARNING
        -------------------
        
        The ``nose-parameterized`` package is deprecated and has been renamed to ``parameterized``.

%package python
Summary: python components for the nose-parameterized package.
Group: Default
Requires: nose-parameterized-python3

%description python
python components for the nose-parameterized package.


%package python3
Summary: python3 components for the nose-parameterized package.
Group: Default
Requires: python3-core

%description python3
python3 components for the nose-parameterized package.


%prep
%setup -q -n nose-parameterized-0.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523292853
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
