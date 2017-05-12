cmake_minimum_required(VERSION 2.8.3)
project(turtlebot_app_manager)

find_package(catkin REQUIRED COMPONENTS
 rospy roslaunch std_msgs roscpp
)

catkin_python_setup()


catkin_package(DEPENDS CATKIN DEPENDS rospy roslaunch std_msgs roscpp
)

install(PROGRAMS
  scripts/app_manager
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

