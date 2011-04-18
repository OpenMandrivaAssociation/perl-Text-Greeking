%define upstream_name    Text-Greeking
%define upstream_version 0.12

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    A module for generating meaningless text
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz


BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Greeking is the use of random letters or marks to show the overall
appearance of a printed page without showing the actual text. Greeking is
used to make it easy to judge the overall appearance of a document without
being distracted by the meaning of the text.

This is a module is for quickly generating varying meaningless text from
any source to create this illusion of the content in systems.

This module was created to quickly give developers simulated content to
fill systems with simulated content. Instead of static Lorem Ipsum text, by
using randomly generated text and optionally varying word sources,
repetitive and monotonous patterns that do not represent real system usage
is avoided.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc CHANGES META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


