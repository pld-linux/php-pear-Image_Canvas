%include	/usr/lib/rpm/macros.php
%define		_status		alpha
%define		_pearname	Image_Canvas
Summary:	%{_pearname} - common interface to image drawing
Summary(pl.UTF-8):	%{_pearname} - wspólny interfejs do rysowania obrazków
Name:		php-pear-%{_pearname}
Version:	0.3.3
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	5998eb6954c4584a71b933df1c9c387a
URL:		http://pear.php.net/package/Image_Canvas/
BuildRequires:	php-pear-PEAR
BuildRequires:	php-pear-PEAR >= 1:1.8.1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-gd
Requires:	php-pear
Requires:	php-pear-Image_Color >= 1.0.0
Obsoletes:	php-pear-Image_Canvas-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A package providing a common interface to image drawing, making source
code independent on the library used.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet dostarczający wspólnego interfejsu do rysowania obrazków,
sprawiając, iż kod jest niezależny od użytej biblioteki.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

# tests should not be packaged
%{__rm} -r $RPM_BUILD_ROOT%{php_pear_dir}/tests/%{_pearname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Image/*.php
%{php_pear_dir}/Image/Canvas

%{php_pear_dir}/data/%{_pearname}
