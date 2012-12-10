Summary:	HTTP based time synchronization tool
Name:		htpdate
Version:	1.0.4
Release:	%mkrel 4
License:	GPL
Group:		System/Servers
URL:		http://www.clevervest.com/htp/
Source0:	http://www.clevervest.com/htp/archive/c/%{name}-%{version}.tar.gz
Source1:	htpdate.init
Source2:	htpdate.sysconfig
Requires(post): rpm-helper
Requires(preun): rpm-helper
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The HTTP Time Protocol (HTP) is used to synchronize a computer's time
with web servers as reference time source. Htpdate will synchronize your
computer's time by extracting timestamps from HTTP headers found
in web servers responses. Htpdate can be used as a daemon, to keep your
computer synchronized.
Accuracy of htpdate is usually better than 0.5 seconds (even better with
multiple servers). If this is not good enough for you, try the ntpd package.

Install the htp package if you need tools for keeping your system's
time synchronized via the HTP protocol. Htpdate works also through
proxy servers.

%prep

%setup -q -n %{name}-%{version}

gunzip htpdate.8*

cp %{SOURCE1} htpdate.init
cp %{SOURCE2} htpdate.sysconfig

%build

%make CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}

# don't fiddle with the initscript!
export DONT_GPRINTIFY=1

install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_mandir}
install -d %{buildroot}%{_initrddir}
install -d %{buildroot}%{_sysconfdir}/sysconfig

install -m0755 htpdate %{buildroot}%{_sbindir}/htpdate
install -m0644 htpdate.8 %{buildroot}%{_mandir}/htpdate.8
install -m0755 htpdate.init %{buildroot}%{_initrddir}/htpdate
install -m0644 htpdate.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/htpdate

%post
%_post_service htpdate

%preun
%_preun_service htpdate

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changelog
%attr(0755,root,root) %{_initrddir}/htpdate
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/htpdate
%attr(0755,root,root) %{_sbindir}/htpdate
%attr(0644,root,root) %{_mandir}/htpdate.8*


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-4mdv2011.0
+ Revision: 619487
- the mass rebuild of 2010.0 packages

* Sun Oct 04 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-3mdv2010.0
+ Revision: 453481
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Oct 16 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-1mdv2009.1
+ Revision: 294284
- 1.0.4

* Sun Sep 07 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-1mdv2009.0
+ Revision: 282155
- 1.0.3

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-3mdv2009.0
+ Revision: 247042
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.0.0-1mdv2008.1
+ Revision: 140755
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Mar 03 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-1mdv2007.0
+ Revision: 131794
- 1.0.0
- bunzip sources

* Fri Mar 02 2007 Oden Eriksson <oeriksson@mandriva.com> 0.9.0-1mdv2007.1
+ Revision: 131183
- Import htpdate

* Fri Feb 03 2006 Oden Eriksson <oeriksson@mandriva.com> 0.9.0-1mdk
- initial Mandriva package

