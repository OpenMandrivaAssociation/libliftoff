%define major 0
%define libname %mklibname liftoff %{major}
%define devname %mklibname liftoff -d

# As gamescope require 0.2.0, let's pull it as git (it is still not relased).
%define git 20220131

Name:           libliftoff
Version:        0.2.0
Release:        0.%{git}.1
Summary:        Lightweight KMS plane library
Group:          System/Libraries
License:        MIT
URL:            https://gitlab.freedesktop.org/emersion/libliftoff/
Source0:        https://gitlab.freedesktop.org/emersion/libliftoff/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkgconfig(libdrm)

%description
libliftoff eases the use of KMS planes from userspace without
standing in your way. Users create "virtual planes" called
layers, set KMS properties on them, and libliftoff will
allocate planes for these layers if possible.

%package -n %{libname}
Summary:	Library for libliftoff
Group:		System/Libraries

%description -n %{libname}
libliftoff eases the use of KMS planes from userspace without
standing in your way. Users create "virtual planes" called
layers, set KMS properties on them, and libliftoff will
allocate planes for these layers if possible.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-v%{version} -p1

%build
%meson
%meson_build

%install
%meson_install

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%license LICENSE
%doc README.md
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
