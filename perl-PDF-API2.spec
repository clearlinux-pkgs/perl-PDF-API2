#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v10
# autospec commit: 5905be9
#
Name     : perl-PDF-API2
Version  : 2.047
Release  : 31
URL      : https://cpan.metacpan.org/authors/id/S/SS/SSIMMS/PDF-API2-2.047.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SS/SSIMMS/PDF-API2-2.047.tar.gz
Summary  : 'Create, modify, and examine PDF files'
Group    : Development/Tools
License  : LGPL-2.1
Requires: perl-PDF-API2-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Font::TTF)
BuildRequires : perl(Font::TTF::Font)
BuildRequires : perl(Sub::Uplevel)
BuildRequires : perl(Test::Exception)
BuildRequires : perl(Test::Memory::Cycle)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This archive contains the distribution PDF-API2,
version 2.047:
Create, modify, and examine PDF files

%package dev
Summary: dev components for the perl-PDF-API2 package.
Group: Development
Provides: perl-PDF-API2-devel = %{version}-%{release}
Requires: perl-PDF-API2 = %{version}-%{release}

%description dev
dev components for the perl-PDF-API2 package.


%package perl
Summary: perl components for the perl-PDF-API2 package.
Group: Default
Requires: perl-PDF-API2 = %{version}-%{release}

%description perl
perl components for the perl-PDF-API2 package.


%prep
%setup -q -n PDF-API2-2.047
cd %{_builddir}/PDF-API2-2.047

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/PDF::API2.3
/usr/share/man/man3/PDF::API2::Annotation.3
/usr/share/man/man3/PDF::API2::Basic::PDF::Array.3
/usr/share/man/man3/PDF::API2::Basic::PDF::Bool.3
/usr/share/man/man3/PDF::API2::Basic::PDF::Dict.3
/usr/share/man/man3/PDF::API2::Basic::PDF::File.3
/usr/share/man/man3/PDF::API2::Basic::PDF::Filter.3
/usr/share/man/man3/PDF::API2::Basic::PDF::Name.3
/usr/share/man/man3/PDF::API2::Basic::PDF::Null.3
/usr/share/man/man3/PDF::API2::Basic::PDF::Number.3
/usr/share/man/man3/PDF::API2::Basic::PDF::Objind.3
/usr/share/man/man3/PDF::API2::Basic::PDF::Page.3
/usr/share/man/man3/PDF::API2::Basic::PDF::Pages.3
/usr/share/man/man3/PDF::API2::Basic::PDF::String.3
/usr/share/man/man3/PDF::API2::Basic::PDF::Utils.3
/usr/share/man/man3/PDF::API2::Content.3
/usr/share/man/man3/PDF::API2::Lite.3
/usr/share/man/man3/PDF::API2::NamedDestination.3
/usr/share/man/man3/PDF::API2::Outline.3
/usr/share/man/man3/PDF::API2::Page.3
/usr/share/man/man3/PDF::API2::Resource.3
/usr/share/man/man3/PDF::API2::Resource::BaseFont.3
/usr/share/man/man3/PDF::API2::Resource::CIDFont.3
/usr/share/man/man3/PDF::API2::Resource::CIDFont::CJKFont.3
/usr/share/man/man3/PDF::API2::Resource::CIDFont::TrueType.3
/usr/share/man/man3/PDF::API2::Resource::ColorSpace.3
/usr/share/man/man3/PDF::API2::Resource::ColorSpace::Indexed::ACTFile.3
/usr/share/man/man3/PDF::API2::Resource::ColorSpace::Separation.3
/usr/share/man/man3/PDF::API2::Resource::ExtGState.3
/usr/share/man/man3/PDF::API2::Resource::Font::BdFont.3
/usr/share/man/man3/PDF::API2::Resource::Font::CoreFont.3
/usr/share/man/man3/PDF::API2::Resource::Font::SynFont.3
/usr/share/man/man3/PDF::API2::Resource::XObject.3
/usr/share/man/man3/PDF::API2::Resource::XObject::Form.3
/usr/share/man/man3/PDF::API2::Resource::XObject::Form::BarCode.3
/usr/share/man/man3/PDF::API2::Resource::XObject::Form::BarCode::code128.3
/usr/share/man/man3/PDF::API2::Resource::XObject::Form::BarCode::qrcode.3
/usr/share/man/man3/PDF::API2::Resource::XObject::Image.3
/usr/share/man/man3/PDF::API2::Resource::XObject::Image::TIFF.3
/usr/share/man/man3/PDF::API2::ViewerPreferences.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
