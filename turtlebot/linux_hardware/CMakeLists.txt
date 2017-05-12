cmake_minimum_required(VERSION 2.8.3)
project(linux_hardware)

find_package(catkin REQUIRED COMPONENTS
 rospy roslaunch message_generation std_msgs
)

catkin_python_setup()

 add_message_files(DIRECTORY msg
   FILES
   LaptopChargeStatus.msg
 )

generate_messages(DEPENDENCIES std_msgs)
catkin_package(
  CATKIN_DEPENDS  rospy roslaunch message_runtime std_msgs
)
include_directories(
  ${catkin_INCLUDE_DIRS}
)

