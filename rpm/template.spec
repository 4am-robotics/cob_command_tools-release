%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/melodic/.*$
%global __requires_exclude_from ^/opt/ros/melodic/.*$

Name:           ros-melodic-cob-script-server
Version:        0.6.15
Release:        1%{?dist}
Summary:        ROS cob_script_server package

License:        Apache 2.0
URL:            http://ros.org/wiki/cob_script_server
Source0:        %{name}-%{version}.tar.gz

Requires:       graphviz-python
Requires:       python-ipython
Requires:       ros-melodic-actionlib
Requires:       ros-melodic-actionlib-msgs
Requires:       ros-melodic-cob-actions
Requires:       ros-melodic-cob-light
Requires:       ros-melodic-cob-mimic
Requires:       ros-melodic-cob-sound
Requires:       ros-melodic-control-msgs
Requires:       ros-melodic-geometry-msgs
Requires:       ros-melodic-message-runtime
Requires:       ros-melodic-move-base-msgs
Requires:       ros-melodic-rospy
Requires:       ros-melodic-rostest
Requires:       ros-melodic-std-msgs
Requires:       ros-melodic-std-srvs
Requires:       ros-melodic-tf
Requires:       ros-melodic-trajectory-msgs
Requires:       ros-melodic-urdfdom-py
BuildRequires:  ros-melodic-actionlib
BuildRequires:  ros-melodic-actionlib-msgs
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-message-generation
BuildRequires:  ros-melodic-rostest
BuildRequires:  ros-melodic-trajectory-msgs

%description
The cob_script_server package provides a simple interface to operate Care-O-bot.
It can be used via the python API or the actionlib interface.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/melodic

%changelog
* Thu Nov 07 2019 Felix Messmer <felixmessmer@gmail.com> - 0.6.15-1
- Autogenerated by Bloom

* Wed Aug 07 2019 Felix Messmer <felixmessmer@gmail.com> - 0.6.14-1
- Autogenerated by Bloom

