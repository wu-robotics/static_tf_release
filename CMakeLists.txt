cmake_minimum_required(VERSION 2.8.3)
project(static_tf)

find_package(catkin REQUIRED COMPONENTS
  rospy
  tf2_ros
  geometry_msgs
  tf 
)

catkin_package(
  CATKIN_DEPENDS geometry_msgs rospy tf tf2_ros
)
