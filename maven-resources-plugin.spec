Name:           maven-resources-plugin
Version:        2.6
Release:        5%{?dist}
Summary:        Maven Resources Plugin

Group:          Development/Libraries
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-resources-plugin
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildArch: noarch

BuildRequires: java-devel >= 1:1.6.0
BuildRequires: maven-local
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-plugin-testing-harness
BuildRequires: maven-shared-reporting-impl
BuildRequires: plexus-interpolation
BuildRequires: plexus-digest
BuildRequires: maven-project
BuildRequires: maven-monitor
BuildRequires: maven-filtering

Provides:       maven2-plugin-resources = %{version}-%{release}
Obsoletes:      maven2-plugin-resources <= 0:2.0.8

%description
The Resources Plugin handles the copying of project resources
to the output directory.

%package javadoc
Group:          Documentation
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.


%prep
%setup -q -n %{name}-%{version}

%build
%mvn_build -f

%install
%mvn_install


%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Mon Aug 26 2013 Michal Srb <msrb@redhat.com> - 2.6-5
- Migrate away from mvn-rpmbuild (Resolves: #997513)

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-4
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.6-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Oct 23 2012 Alexander Kurtakov <akurtako@redhat.com> 2.6-1
- Update to latest upstream.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 06 2011 Tomas Radej <tradej@redhat.com> - 2.5-4
- Fixed dependency on plexus-container-default

* Tue Aug 30 2011 Tomas Radej <tradej@redhat.com> - 2.5-3
- Added changelog

* Mon Aug 29 2011 Tomas Radej <tradej@redhat.com> - 2.5-1
- Update to 2.5
- Guideline fixes
- Added maven-filtering dep

* Thu Jun 23 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.4.3-4
- Add several packages to BR/R as stated in pom.xml

* Tue Jun 21 2011 Alexander Kurtakov <akurtako@redhat.com> 2.4.3-3
- Build with maven 3.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

*Thu Sep 09 2010 Pierre-Yves Chibon <pingou@pingoured.fr> - 2.4.3-1
- Update to 2.4.3

* Fri May 21 2010 Hui Wang <huwang@redhat.com> - 2.2-6
- delete duplicate maven2-plugin-jar
- delete source1

* Tue May 20 2010 Hui Wang <huwang@redhat.com> - 2.2-5
- Add maven-resources-plugin-demap.xml
- Set maven test ignore

* Wed May 19 2010 Hui Wang <huwang@redhat.com> - 2.2-4
- Add missing obsoletes/provides

* Wed May 19 2010 Hui Wang <huwang@redhat.com> - 2.2-3
- Add missing BR:maven-shared-reporting-impl

* Mon May 17 2010 Hui Wang <huwang@redhat.com> - 2.2-2
- Fixed install -pm 644 pom.xml

* Thu May 13 2010 Hui Wang <huwang@redhat.com> - 2.2-1
- Initial version of the package
