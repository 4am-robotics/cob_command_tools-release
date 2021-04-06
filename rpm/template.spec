%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-cob-interactive-teleop
Version:        0.6.21
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS cob_interactive_teleop package

License:        Apache 2.0
URL:            http://ros.org/wiki/cob_interactive_teleop
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-geometry-msgs
Requires:       ros-noetic-interactive-markers
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-rviz
Requires:       ros-noetic-std-msgs
Requires:       ros-noetic-tf
Requires:       ros-noetic-visualization-msgs
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-geometry-msgs
BuildRequires:  ros-noetic-interactive-markers
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-std-msgs
BuildRequires:  ros-noetic-tf
BuildRequires:  ros-noetic-visualization-msgs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
COB teleop interactive marker for RViz provided by dcgm-robotics@FIT group.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Tue Apr 06 2021 Richard Bormann <richard.bormann@ipa.fraunhofer.de> - 0.6.21-1
- Autogenerated by Bloom

* Mon Jan 25 2021 Richard Bormann <richard.bormann@ipa.fraunhofer.de> - 0.6.20-1
- Autogenerated by Bloom

* Wed Dec 02 2020 Richard Bormann <richard.bormann@ipa.fraunhofer.de> - 0.6.19-1
- Autogenerated by Bloom

* Wed Oct 21 2020 Richard Bormann <richard.bormann@ipa.fraunhofer.de> - 0.6.18-1
- Autogenerated by Bloom

* Sat Oct 17 2020 Richard Bormann <richard.bormann@ipa.fraunhofer.de> - 0.6.17-1
- Autogenerated by Bloom

