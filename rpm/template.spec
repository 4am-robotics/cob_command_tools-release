%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-cob-monitoring
Version:        0.6.17
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS cob_monitoring package

License:        Apache 2.0
URL:            http://ros.org/wiki/cob_monitoring
Source0:        %{name}-%{version}.tar.gz

Requires:       ifstat
Requires:       ipmitool
Requires:       ntpdate
Requires:       python-mechanize
Requires:       python-psutil
Requires:       python-requests
Requires:       python3-paramiko
Requires:       ros-noetic-actionlib
Requires:       ros-noetic-cob-light
Requires:       ros-noetic-cob-msgs
Requires:       ros-noetic-cob-script-server
Requires:       ros-noetic-diagnostic-msgs
Requires:       ros-noetic-diagnostic-updater
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-rospy
Requires:       ros-noetic-rostopic
Requires:       ros-noetic-sensor-msgs
Requires:       ros-noetic-std-msgs
Requires:       ros-noetic-topic-tools
Requires:       sysstat
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-diagnostic-updater
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-topic-tools
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
cob_monitoring

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
    -DCMAKE_INSTALL_LIBDIR="lib" \
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
* Sat Oct 17 2020 Felix Messmer <felixmessmer@gmail.com> - 0.6.17-1
- Autogenerated by Bloom

