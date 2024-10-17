Summary:	HTTP based time synchronization tool
Name:		htpdate
Version:	1.1.0
Release:	2
License:	GPL
Group:		System/Servers
URL:		https://www.clevervest.com/htp/
Source0:	http://www.clevervest.com/htp/archive/c/%{name}-%{version}.tar.xz
Source1:	htpdate.service
Source2:	htpdate.sysconfig
Source3:	%{name}.tmpfiles

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

cp %{SOURCE1} %{name}.service
cp %{SOURCE2} %{name}.sysconfig

%build

%make CFLAGS="%{optflags}"

%install

# don't fiddle with the initscript!
export DONT_GPRINTIFY=1

install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_mandir}
install -d %{buildroot}%{_unitdir}
install -d %{buildroot}%{_sysconfdir}/sysconfig

install -m0755 %{name} %{buildroot}%{_sbindir}/%{name}
install -m0644 %{name}.8 %{buildroot}%{_mandir}/%{name}.8
install -m0644 %{name}.service %{buildroot}%{_unitdir}/%{name}.service
install -m0644 %{name}.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/%{name}
sed "s:sysconfig:%{_sysconfdir}/sysconfig:" -i %{buildroot}%{_unitdir}/%{name}.service
install -D -m 644 %{SOURCE3} %{buildroot}%{_prefix}/lib/tmpfiles.d/htpdate.conf

%post
%tmpfiles_create htpdate
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%clean

%files
%doc README Changelog
%attr(0644,root,root) %{_unitdir}/%{name}.service
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%attr(0755,root,root) %{_sbindir}/%{name}
%attr(0644,root,root) %{_mandir}/%{name}.8*
%{_prefix}/lib/tmpfiles.d/*.conf


