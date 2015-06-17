Name:           ros-indigo-cob-script-server
Version:        0.6.2
Release:        0%{?dist}
Summary:        ROS cob_script_server package

Group:          Development/Libraries
License:        LGPL
URL:            http://ros.org/wiki/cob_script_server
Source0:        %{name}-%{version}.tar.gz

Requires:       graphviz-python
Requires:       python-ipython
Requires:       ros-indigo-actionlib
Requires:       ros-indigo-actionlib-msgs
Requires:       ros-indigo-cob-sound
Requires:       ros-indigo-control-msgs
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-move-base-msgs
Requires:       ros-indigo-rospy
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-std-srvs
Requires:       ros-indigo-tf
Requires:       ros-indigo-trajectory-msgs
BuildRequires:  python-ipython
BuildRequires:  ros-indigo-actionlib
BuildRequires:  ros-indigo-actionlib-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cob-sound
BuildRequires:  ros-indigo-control-msgs
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-move-base-msgs
BuildRequires:  ros-indigo-rospy
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-std-srvs
BuildRequires:  ros-indigo-tf
BuildRequires:  ros-indigo-trajectory-msgs

%description
The cob_script_server package provides a simple interface to operate Care-O-bot.
It can be used via the python API or the actionlib interface.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Jun 17 2015 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.2-0
- Autogenerated by Bloom

* Mon Dec 15 2014 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.1-2
- Autogenerated by Bloom

* Mon Dec 15 2014 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.1-1
- Autogenerated by Bloom

* Mon Dec 15 2014 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.1-0
- Autogenerated by Bloom

* Thu Sep 18 2014 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.0-0
- Autogenerated by Bloom

* Thu Aug 28 2014 Florian Weisshardt <fmw@ipa.fhg.de> - 0.5.2-0
- Autogenerated by Bloom

