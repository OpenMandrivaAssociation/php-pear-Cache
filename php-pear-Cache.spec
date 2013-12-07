%define		_class		Cache
%define		upstream_name	%{_class}

Summary:	Framework for caching of arbitrary data
Name:		php-pear-%{upstream_name}
Version:	1.5.6
Release:	6
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/Cache/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	php-pear
Requires:	php-pear
Requires(post,preun): php-pear
Requires:	php-pear-HTTP_Request

%description
With the PEAR Cache you can cache the result of certain function
calls, as well as the output of a whole script run or share data
between applications.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%files
%{_datadir}/pear/%{_class}.php
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{upstream_name}
%{_datadir}/pear/packages/%{upstream_name}.xml

