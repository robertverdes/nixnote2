Summary: An Evernote client clone for Linux, Mac OS X and Windows
Name: nixnote
Version: __VERSION__
Release: 0
License: GNUv2
Group: Applications/Internet 
Vendor: Randy Baumgarte
URL: http://nevernote.sourceforge.net/
Packager: Randy Baumgarte <randy@fbn.cx>
Source: /home/randy/nn2/package_scripts/nixnote2___VERSION_____ARCH__.tar.gz
Requires: tidy

%description
NixNote:: Evernote client clone for Linux

    Copyright 2009-2014, Randy Baumgarte 
    Licensed under GNU General Public Lisence version 2

This is an incomplete clone of Evernote designed to run on Linux. 
While this is designed to work with Evernote, it is in no way
connected with or supported by Evernote.  Any problems you encounter will not be corrected by them
and, since this is GPL software, you are using this software at your own risk.  

See release.txt for details of what works and what doesn't work.

Documents:

release.txt:    Includes new features, known bugs and limitations.

changelog.txt:  ChangeLog and development history
install.txt:    Build and install instructions
credit.txt:     Credit of nixnote developers
gpl.txt:        License description of GPL v2.
license.txt:    Legal notices for licenses and trademarks

shortcut_howto.txt:  How-to document to setup shortcut keys.
shurtcut_sample.txt: Its configuration sample


%clean
rm -rf ${RPM_BUILD_ROOT}
rm -rf ${RPM_BUILD_DIR}/nixnote2

%prep
%setup -n nixnote2


%build

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}
mv -f usr ${RPM_BUILD_ROOT}

%post

%postun
if [ -d /usr/share/nixnote2 ]; then
    rm -rf /usr/share/nixnote2
fi
if [ -f /usr/share/applications/nixnote2.desktop ]; then
    rm -f /usr/share/applications/nixnote2.desktop
fi
if [ -f /usr/bin/nixnote2 ]; then
	rm -f /usr/bin/nixnote2
fi

%files
%attr(644,root,root) /usr/share/nixnote2
%attr(755,root,root) /usr/bin/nixnote2  
%attr(644,root,root) /usr/lib/nixnote2  
%attr(644,root,root) /usr/share/doc/nixnote2
%attr(644,root,root) /usr/share/applications/nixnote2.desktop
%attr(644,root,root) /usr/share/man/man1/nixnote2.1.gz

%changelog
* Sat Mar 15 2014 Randy Baumgarte <randy@fbn.cx> - 2.0-alpha5
- Spec file created for Fedora rpm builds
- See changelog.txt for all changes

