%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}
%global npm_name latest-version

Summary:       Get the latest version of a npm package
Name:          %{?scl_prefix}nodejs-%{npm_name}
Version:       2.0.0
Release:       4%{?dist}
License:       MIT
URL:           https://github.com/sindresorhus/latest-version
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: %{?scl_prefix}nodejs-devel
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
BuildArch:     noarch
Provides:      %{?scl_prefix}nodejs-%{npm_name} = %{version}

%description
Get the latest version of a npm package

Fetches the version directly from the registry instead of 
depending on the massive npm module like the latest module does.

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%files
%doc readme.md
%doc license
%{nodejs_sitelib}/%{npm_name}

%changelog
* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.0-4
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.0-3
- Rebuilt with updated metapackage

* Wed Jan 06 2016 Tomas Hrcka <thrcka@redhat.com> - 2.0.0-2
- Enable scl macros

* Wed Dec 16 2015 Troy Dawson <tdawson@redhat.com> - 2.0.0-1
- Initial package