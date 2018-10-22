%include	/usr/lib/rpm/macros.php
%define		_class		DB
%define		_subclass	odbtp
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - DB interface for ODBTP
Summary(pl.UTF-8):	%{_pearname} - interfejs DB do ODBTP
Name:		php-pear-%{_pearname}
Version:	1.0.4
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	89f6fb35d5b697fef6bdb864ddf04c2e
URL:		http://pear.php.net/package/DB_odbtp/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(odbtp)
Requires:	php-pear
Requires:	php-pear-DB
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DB_odbtp is a PEAR DB driver that uses the ODBTP extension to connect
to a database. It can be used to remotely access any Win32-ODBC
accessible database from any platform.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
DB_odbtp to sterownik DB używający rozszerzenia ODBTP do połączenia z
bazą danych. Umożliwia pracę z bazą danych udostępnioną za pomocą
Win32-ODBC.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/{docs/*,examples}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
