%define upstream_name    IO-Prompt-Tiny
%define upstream_version 0.002

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:    Prompt for user input with a default option
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/IO/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(IO::Handle)
BuildRequires: perl(POSIX)
BuildRequires: perl(Term::ReadKey)
BuildRequires: perl(Test::More)
BuildRequires: perl(Capture::Tiny)
BuildRequires: perl-devel

BuildArch: noarch

%description
This is an extremely simple prompting module, based on the extremely
simple prompt offered by ExtUtils::MakeMaker.In many cases, that's all
you need and this module gives it to you without all the overhead of
ExtUtils::MakeMaker just to prompt for input.

It doesn't do any validation, coloring, menus, timeouts, or any of the
wild, crazy, cool stuff that other prompting modules do. It just prompts
with a default. That's it!

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/IO
