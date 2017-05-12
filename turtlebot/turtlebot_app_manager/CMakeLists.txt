cmake_minimum_required(VERSION 2.8.3)
project(app_manager)

find_package(catkin REQUIRED COMPONENTS
 rospy roslaunch message_generation std_msgs roscpp
)

catkin_python_setup()

 add_message_files(DIRECTORY msg
   FILES
   App.msg
   AppInstallationState.msg
   AppList.msg
   AppStatus.msg
   ClientApp.msg
   ExchangeApp.msg
   Icon.msg
   KeyValue.msg
   StatusCodes.msg
 )


## Generate services in the 'srv' folder
 add_service_files(DIRECTORY srv
   FILES
   GetAppDetails.srv
   GetInstallationState.srv
   InstallApp.srv
   ListApps.srv
   StartApp.srv
   StopApp.srv
   UninstallApp.srv
 )
generate_messages(DEPENDENCIES std_msgs)

catkin_package(DEPENDS CATKIN DEPENDS rospy roslaunch message_runtime std_msgs roscpp
)

install(PROGRAMS
  scripts/app_manager
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

