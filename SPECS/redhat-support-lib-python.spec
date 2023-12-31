%global         package_version 0.13.0-0
%global         package_name redhat-support-lib-python
%global         python_sitelib /usr/lib/python3.6/site-packages

Name:           %{package_name}
Version:        0.13.0
Release:        0%{?release_suffix}%{?dist}
Summary:        Red Hat Support Software Development Library
Vendor:         Red Hat, Inc.
Group:          Development/Libraries
License:        ASL 2.0
URL:            https://api.access.redhat.com
Source0:        http://people.redhat.com/kroberts/projects/redhat-support-lib/%{package_name}-%{package_version}.tar.gz

BuildRequires: python3-setuptools
BuildRequires: python3-devel
BuildArch: noarch
%{!?dist:BuildRequires: buildsys-macros}

Requires: python3
Requires: python3-lxml
Requires: python3-rpm
Requires: python3-dateutil
Requires: python3-requests
Requires: python3-pexpect
Requires: nmap-ncat
Requires: ca-certificates

%description
This package contains the Red Hat Support Software Development Library.
Red Hat customers can use the library to easily integrate their help desk
solutions, IT infrastructure, etc. with the services provided by the
Red Hat Customer Portal.

The library provided by this package is an abstraction layer that simplifies
interactions with the Red Hat Customer Portal. Simply create an instance of
the API by providing the necessary authorization credentials, then use the
API object to interact with the Red Hat Customer Portal.

Some of the interactions supported by this API include, but are not limited to,
automatic diagnostic services on log files, knowledge base searching,
support case creation, attach files to support cases, view the status of
support cases, entitlement viewing, etc.

%prep
%setup -q -n %{package_name}-%{package_version}

%build
%configure \
        --docdir="%{_docdir}/%{package_name}-%{version}" \
        --disable-python-syntax-check

make %{?_smp_mflags}

%install
rm -rf "%{buildroot}"
make %{?_smp_mflags} install DESTDIR="%{buildroot}"

%files
%doc AUTHORS README
%{python_sitelib}/redhat_support_lib/

%changelog
* Mon Dec 06 2021 Pranita Ghole<pghole@redhat.com> - 0.13.0-0
- Resolves: rhbz#2028550 - RHST should use new Red Hat Secure FTP instead of dropbox for attachments
- Resolves: rhbz#2028546 - Add support for handling JSON response from API's
- Resolves: rhbz#2028543 - Add support to upload to and download from S3

* Tue Nov 10 2020 Pranita Ghole<pghole@redhat.com> - 0.11.3-1
- Resolves: rhbz#1881343 - sosreports upload using redhat-support-tool fail with strong passwords

* Tue Feb 18 2020 Pranita Ghole<pghole@redhat.com> - 0.11.2-1
- Resolves: rhbz#1677257 - redhat-support-lib-python: AttributeError from utils/reporthelper.py no buf

* Fri Feb 08 2019 Pranita Ghole<pghole@redhat.com> - 0.10.1-1
- Resolves: rhbz#1670001 - redhat-support-tool -o option does not work (soscleaner)
- Resolves: rhbz#1670369 - redhat-support-lib-python: Traceback on make_report from utils.reporthelper
- Resolves: rhbz#1670044 - redhat-support-tool proxy does not work on rhel-8 

* Mon Jan 14 2019 Vikas Rathee <vrathee@redhat.com> - 0.10.1-0
- Resolves: rhbz#1628616 - Fixing python 3 issues

* Wed Nov 21 2018 Vikas Rathee <vrathee@redhat.com> - 0.10.0-0
- Resolves: rhbz#1628616 - Changes for rhel-8

* Thu May 25 2017 Vikas Rathee <vrathee@redhat.com> - 0.9.8-1
- Correcting changelog

* Tue Jul 5 2016 Mark Huth <mhuth@redhat.com> - 0.9.7-6
- Resolves: rhbz#1314606 - show progress with addattachment
- Resolves: rhbz#1314607 - problem with addattachment -s switch

* Wed Jan 7 2015 Mark Huth <mhuth@redhat.com> - 0.9.7-3
- Resolves: rhbz#1176473 - FTP upload via proxy
- Small changes to download progress

* Mon Oct 20 2014 Keith Robertson <kroberts@redhat.com> - 0.9.7-0
- Proxy fix for file uploads
- Get a specific case group

* Fri Sep 5 2014 Keith Robertson <kroberts@redhat.com> - 0.9.6-3
- Fix proxy upload attachment

* Thu Jun 19 2014 Keith Robertson <kroberts@redhat.com> - 0.9.6-1
- Display download progess for attachments

* Wed Feb 26 2014 Keith Robertson <kroberts@redhat.com> - 0.9.6-0
- Various fixes

* Sun Aug 11 2013 Keith Robertson <kroberts@redhat.com> - 0.9.5-8
- Resolves: rhbz#987168

* Tue Jul 23 2013 Keith Robertson <kroberts@redhat.com> - 0.9.5-6
- various security fixes

* Mon Jul 22 2013 Keith Robertson <kroberts@redhat.com> - 0.9.5-4
- Resolves: rhbz#967498

* Tue Jun 11 2013 Keith Robertson <kroberts@redhat.com> - 0.9.5-3
- Resolves: bz869406

* Tue Jun 11 2013 Keith Robertson <kroberts@redhat.com> - 0.9.5-2
- Various updates including;
  - CA certificate fix for EL5
  - Support for case filters
  
* Thu May 23 2013 Nigel Jones <nigjones@redhat.com> - 0.9.4-1
- Downloads:
  - Fixes to download handling to avoid excessive memory use
- Localization/Internationalization:
  - Changes to support non-ASCII character input from character sets used in
    Red Hat GSS supported languages.

* Fri Apr 26 2013 Nigel Jones <nigjones@redhat.com> - 0.9.2-1
- API update to bring in line with current version of Strata.
  Changes include:
   - Update to Recommendations API
   - Pagination of Cases
- Additional fixes for proxy handling, and traceability of exceptions

* Tue Feb 19 2013 Nigel Jones <nigjones@redhat.com> - 0.9.0-2
- Import into Red Hat packaging system

* Fri Aug 17 2012 Keith Robertson <kroberts@redhat.com> - 0.9.0-1
- Initial release
