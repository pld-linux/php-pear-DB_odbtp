%include	/usr/lib/rpm/macros.php
%define		_class		DB
%define		_subclass	odbtp
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - DB interface for ODBTP
Summary(pl):	%{_pearname} - interfejs DB do ODBTP
Name:		php-pear-%{_pearname}
Version:	1.0.1
%define	_ver	RC1
Release:	0.%{_ver}
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{_ver}.tgz
# Source0-md5:	3dd8e18e4a5de92279d06ea4d83aaa95
URL:		http://pear.php.net/package/DB_odbtp/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DB_odbtp is a PEAR DB driver that uses the ODBTP extension to connect
to a database. It can be used to remotely access any Win32-ODBC
accessible database from any platform.

In PEAR status of this package is: %{_status}.

%description -l pl
DB_odbtp to sterownik DB u¿ywaj±cy rozszerzenia ODBTP do po³±czenia z
baz± danych. Umo¿liwia pracê z baz± danych udostêpnion± za pomoc±
Win32-ODBC.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c -n %{name}-%{version}%{_ver}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}%{_ver}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}%{_ver}/{docs,examples}
%{php_pear_dir}/%{_class}/*.php
