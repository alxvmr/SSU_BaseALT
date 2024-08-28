Name: calc
Version: 0.1.0
Release: alt1

Summary: Simply calc
License: GPLv3+
Group: Other
BuildArch: noarch

BuildRequires: rpm-build-python3
BuildRequires: python3-module-wheel, python3-module-poetry
Requires: python3-module-emoji

Source0: %name-%version.tar

%description
Demo application

%prep
%setup -q

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%{name}
%python3_sitelibdir/%{name}-%version.dist-info

%changelog
* Wed Aug 28 2024 Maria Alexeeva <alxvmr@altlinux.org> 0.1.0-alt1
- First build

