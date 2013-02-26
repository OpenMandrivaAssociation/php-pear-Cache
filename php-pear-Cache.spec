%define		_class		Cache
%define		upstream_name	%{_class}

Name:		php-pear-%{upstream_name}
Version:	1.5.6
Release:	%mkrel 4
Summary:	Framework for caching of arbitrary data
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Cache/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires:	php-pear
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear-HTTP_Request
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
With the PEAR Cache you can cache the result of certain function
calls, as well as the output of a whole script run or share data
between applications.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}.php
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{upstream_name}
%{_datadir}/pear/packages/%{upstream_name}.xml




%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.5.6-2mdv2011.0
+ Revision: 667484
- mass rebuild

* Sun Nov 07 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.5.6-1mdv2011.0
+ Revision: 594482
- update to new version 1.5.6

* Sun Dec 13 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.5.5-4mdv2010.1
+ Revision: 478287
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.5.5-3mdv2010.0
+ Revision: 426603
- rebuild

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 1.5.5-2mdv2009.1
+ Revision: 321797
- rebuild

* Sun Oct 12 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.5.5-1mdv2009.1
+ Revision: 292876
- update to new version 1.5.5

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.5.4-10mdv2009.0
+ Revision: 224686
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 1.5.4-9mdv2008.1
+ Revision: 178499
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.5.4-8mdv2007.0
+ Revision: 81403
- Import php-pear-Cache

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.5.4-8mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.5.4-7mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.5.4-6mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.5.4-5mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.5.4-4mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.5.4-3mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.5.4-2mdk
- fix spec file to conform with the others

* Thu Jan 20 2005 Pascal Terjan <pterjan@mandrake.org> 1.5.4-1mdk
- First mdk package

