cmake_minimum_required(VERSION 2.8.3)
project(turtlebot_app_manager_msgs)

find_package(catkin REQUIRED COMPONENTS message_generation )

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
generate_messages()

catkin_package(DEPENDS CATKIN DEPENDS message_runtime)


