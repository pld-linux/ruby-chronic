Summary:	Natural language date parser for Ruby
Summary(pl):	Analizator dat w jêzyku naturalnym dla jêzyka Ruby
Name:		ruby-chronic
Version:	0.1.4
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/14040/chronic-0.1.4.gem
# Source0-md5:	54204d527c502b42daed33bf9b1ce3f8
URL:		http://chronic.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	setup.rb = 3.3.1
Requires:	ruby-builder
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Chronic is a pure Ruby natural language date parser. It can parse
dates/times in a wide variety of standard and natural formats from
simple things like "tomorrow" to comples things like "7 hours before
tomorrow at noon".

%description -l pl
Chronic to napisany w czystym Rubym analizator dat w jêzyku
naturalnym. Mo¿e analizowaæ daty i czasy w szerokim zakresie
standardów i formatów naturalnych od prostych takich jak "tomorrow"
(jutro) do bardziej z³o¿onych jak "7 hours before tomorrow at noon" (7
godzin przed jutrzejszym po³udniem).


%prep
%setup -q -c -T
tar xf %{SOURCE0} -O data.tar.gz | tar xzv-
cp %{_datadir}/setup.rb .

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc lib
rdoc --ri --op ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%{ruby_rubylibdir}/chronic*
%{ruby_ridir}/*
