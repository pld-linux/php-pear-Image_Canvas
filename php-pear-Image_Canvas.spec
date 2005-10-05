%include	/usr/lib/rpm/macros.php
%define		_class		Image
%define		_subclass	Canvas
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - common interface to image drawing
Summary(pl):	%{_pearname} - wspólny interfejs do rysowania obrazków
Name:		php-pear-%{_pearname}
Version:	0.2.1
Release:	2
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	f480e05d0cd9d3c7efd664e07d4a3e34
URL:		http://pear.php.net/package/Image_Canvas/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-gd
Requires:	php-pear
Requires:	php-pear-Image_Color >= 1.0.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A package providing a common interface to image drawing, making source
code independent on the library used.

In PEAR status of this package is: %{_status}.

%description -l pl
Pakiet dostarczaj±cy wspólnego interfejsu do rysowania obrazków,
sprawiaj±c, i¿ kod jest niezale¿ny od u¿ytej biblioteki.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

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
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}

%{php_pear_dir}/data/%{_pearname}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
