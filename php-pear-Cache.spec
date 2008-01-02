%define		_class		Cache
%define		_status		stable
%define		_pearname	%{_class}

Summary:	%{_pearname} - Framework for caching of arbitrary data
Name:		php-pear-%{_pearname}
Version:	1.5.4
Release:	%mkrel 8
License:	PHP License
Group:		Development/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tar.bz2
URL:		http://pear.php.net/package/Cache/
Requires:	php-pear
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear-HTTP_Request
BuildArch:	noarch
BuildRequires:	dos2unix
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
With the PEAR Cache you can cache the result of certain function
calls, as well as the output of a whole script run or share data
between applications.

In PEAR status of this package is: %{_status}.

%prep

%setup -q -c

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

# strip away annoying ^M
find -type f | grep -v ".gif" | grep -v ".png" | grep -v ".jpg" | xargs dos2unix -U

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/pear/%{_class}/Container

install %{_pearname}-%{version}/%{_class}.php %{buildroot}%{_datadir}/pear/
install %{_pearname}-%{version}/*.php %{buildroot}%{_datadir}/pear/%{_class}/
install %{_pearname}-%{version}/Container/* %{buildroot}%{_datadir}/pear/%{_class}/Container

rm %{buildroot}%{_datadir}/pear/%{_class}/%{_class}.php

install -d %{buildroot}%{_datadir}/pear/packages
install -m0644 package.xml %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

%post
if [ "$1" = "1" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi
if [ "$1" = "2" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi

%preun
if [ "$1" = 0 ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear uninstall --nodeps -r %{_pearname}
	fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%dir %{_datadir}/pear/%{_class}
%{_datadir}/pear/*.php
%{_datadir}/pear/%{_class}/*.php
%{_datadir}/pear/%{_class}/Container
%{_datadir}/pear/packages/%{_pearname}.xml


