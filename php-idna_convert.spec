%include	/usr/lib/rpm/macros.php
%define		php_min_version 5.0.0
%define		pkgname	idna_convert
%define		ver		%(echo %{version} | tr -d .)
Summary:	PHP class to encode/decode IDN
Name:		php-%{pkgname}
Version:	0.9.0
Release:	1
License:	LGPL v2.1
Group:		Development/Languages/PHP
Source0:	https://phlymail.com/download/Goodies/idna_convert_%{ver}.zip
# Source0-md5:	2657de643b847be40dab1e447e549cf0
URL:		https://phlymail.com/en/downloads/idna-convert.html
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.461
BuildRequires:	unzip
Requires:	php(core) >= %{php_min_version}
Requires:	php(mbstring)
Requires:	php(pcre)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The class idna_convert allows to convert internationalized domain
names (see RFC 3490, 3491, 3492 and 3454 for detials) as they can be
used with various registries worldwide to be translated between their
original (localized) form and their encoded form as it will be used in
the DNS (Domain Name System).

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}
cp -a idna_convert.class.php $RPM_BUILD_ROOT%{php_data_dir}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a example.php $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ReadMe.txt
%{php_data_dir}/idna_convert.class.php
%{_examplesdir}/%{name}-%{version}
