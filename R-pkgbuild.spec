%global packname  pkgbuild
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Find Tools Needed to Build R Packages

License:          GPLv3
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-callr >= 2.0.0, R-crayon, R-desc, R-R6, R-rprojroot, R-withr >= 2.1.2
# Suggests:  R-Rcpp, R-testthat, R-covr
# LinkingTo:
# Enhances:

BuildArch:        noarch
Requires:         R-core
Requires:         R-callr >= 2.0.0
Requires:         R-crayon
Requires:         R-desc
Requires:         R-R6
Requires:         R-rprojroot
Requires:         R-withr >= 2.1.2
Suggests:         R-Rcpp
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-callr >= 2.0.0
BuildRequires:    R-crayon
BuildRequires:    R-desc
BuildRequires:    R-R6
BuildRequires:    R-rprojroot
BuildRequires:    R-withr >= 2.1.2
BuildRequires:    R-Rcpp
BuildRequires:    R-testthat

%description
Provides functions used to build R packages. Locates compilers needed to
build R packages on various platforms and ensures the PATH is configured
appropriately so R can use them.


%prep
%setup -q -c -n %{packname}

# Don't need coverage; it's not packaged either.
sed -i 's/, covr//g' %{packname}/DESCRIPTION


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%{_bindir}/R CMD check %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help


%changelog
* Sat Sep 22 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.1-1
- Update to latest version

* Tue Jul 31 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.0-1
- initial package for Fedora
