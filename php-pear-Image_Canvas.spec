%include	/usr/lib/rpm/macros.php
%define		_class		Image
%define		_subclass	Canvas
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - common interface to image drawing
Summary(pl.UTF-8):	%{_pearname} - wspólny interfejs do rysowania obrazków
Name:		php-pear-%{_pearname}
Version:	0.3.2
Release:	1
Epoch:		0
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	0ffb421ade2f9c8234861cc73550e503
URL:		http://pear.php.net/package/Image_Canvas/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(gd)
Requires:	php-pear
Requires:	php-pear-Image_Color >= 1.0.0
Requires:	php-pear-PEAR-core >= 1:1.8.1
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

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoProv:	no
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
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
