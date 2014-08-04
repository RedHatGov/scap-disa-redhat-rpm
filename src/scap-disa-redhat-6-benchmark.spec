%global		elver		6
%global		disamaj		1
%global		disamin		4
%global		disaver		v%{disamaj}r%{disamin}

Name:		scap-disa-redhat-6-benchmark-%{disaver}
Version:	%{disamaj}.0
Release:	%{disamin}%{?dist}
Summary:	DISA security guidance and baselines in SCAP formats (Version %{disaver})
Group:		Applications/System
License:	Public Domain
URL:		http://iase.disa.mil/stigs/os/unix/red_hat.html
Source0:	http://iase.disa.mil/stigs/os/unix/u_redhat_%{elver}_v%{disamaj}r%{disamin}_benchmark.zip
BuildArch:	noarch
Requires:	xml-common, openscap-utils >= 0.9.1

%description
Official DISA released SCAP content.

%prep
%setup -q -T -c %{name} -a0

%build

%install
# Create required directory structure
mkdir -p %{buildroot}%{_datadir}/xml/scap/disa/rhel6/%{disaver}
cp -a  *xml %{buildroot}%{_datadir}/xml/scap/disa/rhel6/%{disaver}

%files
%{_datadir}/xml/scap/disa/rhel6/*


%changelog
* Mon Aug 04 2014 Michael J. Ayers <ayersmj@redhat.com> - %{disamaj}.%{disamin}
- Initial build
