#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nose-parameterized
Version  : 0.6.0
Release  : 29
URL      : https://pypi.debian.net/nose-parameterized/nose-parameterized-0.6.0.tar.gz
Source0  : https://pypi.debian.net/nose-parameterized/nose-parameterized-0.6.0.tar.gz
Summary  : Parameterized testing with any Python test framework (DEPRECATED; See the 'parameterized' package)
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause
Requires: nose-parameterized-license = %{version}-%{release}
Requires: nose-parameterized-python = %{version}-%{release}
Requires: nose-parameterized-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
Parameterized testing with any Python test framework
====================================================

DEPRECATION WARNING
-------------------

The ``nose-parameterized`` package is deprecated and has been renamed to ``parameterized``.

See:

- https://pypi.python.org/pypi/parameterized
- https://github.com/wolever/parameterized


Migrating from ``nose-parameterized`` to ``parameterized``
----------------------------------------------------------

To migrate a codebase from ``nose-parameterized`` to ``parameterized``:

1. Update the requirements file, replacing ``nose-parameterized`` with
   ``parameterized``.

2. Replace all references to ``nose_parameterized`` with ``parameterized``::

    $ perl -pi -e 's/nose_parameterized/parameterized/g' your-codebase/

3. You're done!

%package license
Summary: license components for the nose-parameterized package.
Group: Default

%description license
license components for the nose-parameterized package.


%package python
Summary: python components for the nose-parameterized package.
Group: Default
Requires: nose-parameterized-python3 = %{version}-%{release}

%description python
python components for the nose-parameterized package.


%package python3
Summary: python3 components for the nose-parameterized package.
Group: Default
Requires: python3-core
Provides: pypi(nose-parameterized)

%description python3
python3 components for the nose-parameterized package.


%prep
%setup -q -n nose-parameterized-0.6.0
cd %{_builddir}/nose-parameterized-0.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583187253
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/nose-parameterized
cp %{_builddir}/nose-parameterized-0.6.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/nose-parameterized/416f8ee7afc3d6896efff6c8bdce9c327c77931a
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/nose-parameterized/416f8ee7afc3d6896efff6c8bdce9c327c77931a

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
