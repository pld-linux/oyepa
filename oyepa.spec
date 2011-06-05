Summary:	A tagging file system emulator
Name:		oyepa
Version:	3.2
Release:	0.3
License:	GPL v2
Group:		X11/Applications
Source0:	http://pages.stern.nyu.edu/~marriaga/software/oyepa/%{name}-%{version}.tgz
# Source0-md5:	099777c8b0601bdaa6ff2e6ab4fcfe8c
URL:		http://pages.stern.nyu.edu/~marriaga/software/oyepa/
BuildRequires:	python-PyQt4-devel
BuildRequires:	python-pyinotify
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A tagging file system emulator

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/icons

install *.py $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
install icons/* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/icons
cd $RPM_BUILD_ROOT%{_bindir}
for file in oyepa{,-filemon} mp ds wnote; do
	ln -sf ../share/%{name}-%{version}/$file.py $file
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGE.LOG README TODO
%dir %{_datadir}/%{name}-%{version}
%attr(755,root,root) %{_datadir}/%{name}-%{version}/*.py
%{_datadir}/%{name}-%{version}/icons
%attr(755,root,root) %{_bindir}/*
