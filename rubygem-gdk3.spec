# Generated from pkg-config-1.1.4.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	gdk3

Summary:	Ruby binding of gdk3
Name:		rubygem-%{rbname}

Version:	2.2.4
Release:	3
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		https://ruby-gnome2.sourceforge.jp/
BuildArch:	noarch
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildRequires:  rubygem(glib2)
BuildRequires:  rubygem-glib2-devel
BuildRequires:	rubygem(gobject-introspection)
BuildRequires:	rubygem-gobject-introspection-devel
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:  ruby-devel
BuildRequires:  pkgconfig(glib-2.0)

%description
Ruby binding of gdk3.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build

%install
%gem_install

%files
%{gem_dir}/gems/%{rbname}-%{version}/lib/*.rb
%{gem_dir}/gems/%{rbname}-%{version}/lib/%{rbname}/*.rb
%{gem_dir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{gem_dir}/doc/%{rbname}-%{version}


%changelog

