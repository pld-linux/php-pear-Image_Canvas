%include	/usr/lib/rpm/macros.php
%define		_class		Image
%define		_subclass	Canvas
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - common interface to image drawing
Summary(pl):	%{_pearname} - wspólny interfejs do rysowania obrazków
Name:		php-pear-%{_pearname}
Version:	0.2.1
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	f480e05d0cd9d3c7efd664e07d4a3e34
URL:		http://pear.php.net/package/Image_Canvas/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-gd
Requires:	php-pear
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

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/{Fonts,GD}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/%{_subclass}/Fonts/fontmap.txt $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Fonts
install %{_pearname}-%{version}/%{_subclass}/GD/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/GD

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{docs,tests}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
