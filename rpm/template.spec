Name:           ros-indigo-static-tf
Version:        0.0.2
Release:        2%{?dist}
Summary:        ROS static_tf package

Group:          Development/Libraries
License:        TODO
Source0:        %{name}-%{version}.tar.gz

Requires:       python
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-rospy
Requires:       ros-indigo-tf
Requires:       ros-indigo-tf2-ros
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-rospy
BuildRequires:  ros-indigo-tf
BuildRequires:  ros-indigo-tf2-ros

%description
The static_tf package

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
        -DCMAKE_INSTALL_LIBDIR="lib" \
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
* Tue Aug 28 2018 David V. Lu!! <davidvlu@gmail.com> - 0.0.2-2
- Autogenerated by Bloom

* Tue Aug 28 2018 David V. Lu!! <davidvlu@gmail.com> - 0.0.2-1
- Autogenerated by Bloom

* Tue Aug 28 2018 David V. Lu!! <davidvlu@gmail.com> - 0.0.2-0
- Autogenerated by Bloom

* Sat Apr 01 2017 David V. Lu!! <davidvlu@gmail.com> - 0.0.1-1
- Autogenerated by Bloom

* Sat Apr 01 2017 David V. Lu!! <davidvlu@gmail.com> - 0.0.1-0
- Autogenerated by Bloom

