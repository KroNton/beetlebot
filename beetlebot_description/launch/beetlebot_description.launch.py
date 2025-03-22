import os
from ament_index_python.packages import (get_package_prefix, get_package_share_directory)
from launch.substitutions import Command
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.actions import Node


def generate_launch_description():

    # Setup project paths
    package_description ="beetlebot_description"

    pkg_project_description = get_package_share_directory('beetlebot_description')
    package_directory = get_package_share_directory(package_description)

    install_dir_path = (get_package_prefix(package_description) + "/share")
    gazebo_resource_paths = [install_dir_path]

    if "GZ_SIM_RESOURCE_PATH" in os.environ:
        for resource_path in gazebo_resource_paths:
            if resource_path not in os.environ["GZ_SIM_RESOURCE_PATH"]:
                os.environ["GZ_SIM_RESOURCE_PATH"] += (':' + resource_path)
        else:
            os.environ["GZ_SIM_RESOURCE_PATH"] = (':'.join(gazebo_resource_paths))

    if "GZ_SIM_MODEL_PATH" in os.environ:
        for resource_path in gazebo_resource_paths:
            if resource_path not in os.environ["GZ_SIM_MODEL_PATH"]:
                os.environ["GZ_SIM_MODEL_PATH"] += (':' + resource_path)
        else:
            os.environ["GZ_SIM_MODEL_PATH"] = (':'.join(gazebo_resource_paths))   
               
    urdf_file = 'beetlebot.xacro'      
    robot_desc_path = os.path.join(package_directory, "urdf", urdf_file)
    robot_description = ParameterValue(
        Command(['xacro ', robot_desc_path]),
        value_type=str
    )

    print("URDF Loaded !")

    # For publishing and controlling the robot pose, we need joint states of the robot
    joint_state_publisher = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        output=['screen']
    )

    # Takes the description and joint angles as inputs and publishes the 3D poses of the robot links
    # Robot State Publisher (RSP) #
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher_node',
        output="screen",
        emulate_tty=True,
        parameters=[{
            'use_sim_time': True, 
            'robot_description': robot_description  # Use the evaluated ParameterValue
        }]
    )

    # Visualize in RViz
    rviz = Node(
       package='rviz2',
       executable='rviz2',
       arguments=['-d', os.path.join(pkg_project_description, 'config', 'beetlebot.rviz')],
       condition=IfCondition(LaunchConfiguration('rviz'))
    )

    return LaunchDescription([
        DeclareLaunchArgument('rviz', default_value='true',
                              description='Open RViz.'),
        joint_state_publisher,
        robot_state_publisher_node,
        rviz
    ])
