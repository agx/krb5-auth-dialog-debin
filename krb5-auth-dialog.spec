Summary: Kerberos 5 authentication dialog
Name: krb5-auth-dialog
Version: 3.15.4
Release: 1
License: GPL
Group: User Interface/X
URL: http://www.redhat.com/
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: krb5-devel
BuildRequires: libgnomeui-devel

%description
This package contains a dialog that warns the user when their Kerberos
tickets are about to expire and lets them renew them.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT


%files -f %name.lang
%defattr(-,root,root,-)
%doc
%{_bindir}/krb5-auth-dialog
%{_mandir}/man?/krb5-auth-dialog.1*
%{_datadir}/krb5-auth-dialog/
%{_sysconfdir}/xdg/autostart/krb5-auth-dialog.dekstop


%changelog
* Mon Aug 16 2004 GNOME <jrb@redhat.com> - auth-dialog
- Initial build.

