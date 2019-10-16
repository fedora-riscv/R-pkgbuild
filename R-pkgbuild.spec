%global packname  pkgbuild
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.0.6
Release:          1%{?dist}
Summary:          Find Tools Needed to Build R Packages

License:          GPLv3
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-callr >= 3.2.0, R-cli, R-crayon, R-desc, R-prettyunits, R-R6, R-rprojroot, R-withr >= 2.1.2
# Suggests:  R-Rcpp, R-testthat, R-covr
# LinkingTo:
# Enhances:

BuildArch:        noarch
Requires:         R-core
Requires:         R-callr >= 3.2.0
Requires:         R-cli
Requires:         R-crayon
Requires:         R-desc
Requires:         R-prettyunits
Requires:         R-R6
Requires:         R-rprojroot
Requires:         R-withr >= 2.1.2
Suggests:         R-Rcpp
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-callr >= 3.2.0
BuildRequires:    R-cli
BuildRequires:    R-crayon
BuildRequires:    R-desc
BuildRequires:    R-prettyunits
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
NOT_CRAN=true %{_bindir}/R CMD check %{packname}


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
* Tue Oct 15 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.6-1
- Update to latest version

* Mon Aug 26 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.5-1
- Update to latest version

* Sat Aug 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.4-1
- Update to latest version

* Wed Mar 20 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.3-1
- Update to latest version

* Wed Mar 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.2-2
- Enable more tests

* Sun Feb 10 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.2-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Sep 22 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.1-1
- Update to latest version

* Tue Jul 31 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.0-1
- initial package for Fedora
