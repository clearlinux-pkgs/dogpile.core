#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x330239C1C4DAFEE1 (classic@zzzcomputing.com)
#
Name     : dogpile.core
Version  : 0.4.1
Release  : 23
URL      : https://files.pythonhosted.org/packages/0e/77/e72abc04c22aedf874301861e5c1e761231c288b5de369c18be8f4b5c9bb/dogpile.core-0.4.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/0e/77/e72abc04c22aedf874301861e5c1e761231c288b5de369c18be8f4b5c9bb/dogpile.core-0.4.1.tar.gz
Source99 : https://files.pythonhosted.org/packages/0e/77/e72abc04c22aedf874301861e5c1e761231c288b5de369c18be8f4b5c9bb/dogpile.core-0.4.1.tar.gz.asc
Summary  : A 'dogpile' lock, typically used as a component of a larger caching solution
Group    : Development/Tools
License  : BSD-3-Clause
Requires: dogpile.core-python3
Requires: dogpile.core-license
Requires: dogpile.core-python
BuildRequires : buildreq-distutils3
BuildRequires : nose
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

%description
============
        
        A "dogpile" lock, one which allows a single thread to generate
        an expensive resource while other threads use the "old" value, until the
        "new" value is ready.
        
        Dogpile is basically the locking code extracted from the
        Beaker package, for simple and generic usage.
        
        Usage
        -----

%package license
Summary: license components for the dogpile.core package.
Group: Default

%description license
license components for the dogpile.core package.


%package python
Summary: python components for the dogpile.core package.
Group: Default
Requires: dogpile.core-python3

%description python
python components for the dogpile.core package.


%package python3
Summary: python3 components for the dogpile.core package.
Group: Default
Requires: python3-core

%description python3
python3 components for the dogpile.core package.


%prep
%setup -q -n dogpile.core-0.4.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532378514
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test || :
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/dogpile.core
cp LICENSE %{buildroot}/usr/share/doc/dogpile.core/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/dogpile.core/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
