%define upstream_name    Text-Greeking
%define upstream_version 0.12

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	A module for generating meaningless text
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch: noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc CHANGES META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.120.0-2mdv2011.0
+ Revision: 655233
- rebuild for updated spec-helper

* Thu May 06 2010 Michael Scherer <misc@mandriva.org> 0.120.0-1mdv2011.0
+ Revision: 542841
- import perl-Text-Greeking


* Thu May 06 2010 cpan2dist 0.12-1mdv
- initial mdv release, generated with cpan2dist
