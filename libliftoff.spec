Name:           libliftoff
Version:        0.1.0
Release:        1
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

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n -p1 %{name}-v%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_libdir}/*.so.0*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
