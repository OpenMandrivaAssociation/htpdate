Summary:	HTTP based time synchronization tool
Name:		htpdate
Version:	1.0.0
Release:	%mkrel 3
License:	GPL
Group:		System/Servers
URL:		http://www.clevervest.com/htp/
Source0:	http://www.clevervest.com/htp/archive/c/%{name}-%{version}.tar.gz
Source1:	htpdate.init
Source2:	htpdate.sysconfig
Requires(post): rpm-helper
Requires(preun): rpm-helper
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

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
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changelog
%attr(0755,root,root) %{_initrddir}/htpdate
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/htpdate
%attr(0755,root,root) %{_sbindir}/htpdate
%attr(0644,root,root) %{_mandir}/htpdate.8*


