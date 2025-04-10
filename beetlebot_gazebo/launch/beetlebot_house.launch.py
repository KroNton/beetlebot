import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.actions import Node
from launch.substitutions import Command
from ament_index_python.packages import (get_package_prefix, get_package_share_directory)

def generate_launch_description():
    # Configure ROS nodes for launch
    package_description = "beetlebot_description"
    package_gazebo = "beetlebot_gazebo"

    # Setup project paths
    pkg_project_gazebo = get_package_share_directory('beetlebot_gazebo')
    package_directory_description = get_package_share_directory(package_description)
    pkg_ros_gz_sim = get_package_share_directory('ros_gz_sim')

    # Set the Path to Robot Mesh Models for Loading in Gazebo Sim
    install_dir_path = get_package_prefix(package_description) + "/share"
    install_gazebo_dir_path = get_package_prefix(package_gazebo) + "/share"
    gazebo_resource_paths = [install_dir_path, install_gazebo_dir_path]

    # Update environment variables for Gazebo
    for env_var in ["GZ_SIM_RESOURCE_PATH", "GZ_SIM_MODEL_PATH", "SDF_PATH"]:
        if env_var in os.environ:
            for resource_path in gazebo_resource_paths:
                if resource_path not in os.environ[env_var]:
                    os.environ[env_var] += (':' + resource_path)
        else:
            os.environ[env_var] = (':'.join(gazebo_resource_paths))

    # Load the SDF file from "description" package
    urdf_file = 'beetlebot.xacro'
    robot_desc_path = os.path.join(package_directory_description, "urdf", urdf_file)

    # Check if the URDF file exists
    if not os.path.exists(robot_desc_path):
        raise FileNotFoundError(f"URDF file not found at: {robot_desc_path}")

    robot_description = ParameterValue(
        Command(['xacro ', robot_desc_path]),
        value_type=str
    )

    # Setup to launch the simulator and Gazebo world
    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py')),
        launch_arguments={'gz_args': PathJoinSubstitution([
            pkg_project_gazebo,
            'worlds',
            'house.sdf'
        ])}.items(),
    )

    # Spawn the Robot
    declare_spawn_x = DeclareLaunchArgument("x", default_value="0.0",
                                            description="Model Spawn X Axis Value")
    declare_spawn_y = DeclareLaunchArgument("y", default_value="0.0",
                                            description="Model Spawn Y Axis Value")
    declare_spawn_z = DeclareLaunchArgument("z", default_value="0.5",
                                            description="Model Spawn Z Axis Value")
    gz_spawn_entity = Node(
        package="ros_gz_sim",
        executable="create",
        name="my_robot_spawn",
        arguments=[
            "-name", "beetlebot",
            "-allow_renaming", "true",
            "-topic", "robot_description",
            "-x", LaunchConfiguration("x"),
            "-y", LaunchConfiguration("y"),
            "-z", LaunchConfiguration("z"),
        ],
        output="screen",
    )

    # Robot State Publisher
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='both',
        parameters=[
            {'use_sim_time': True},
            {'robot_description': robot_description},
        ]
    )

    # RViz
    rviz = Node(
       package='rviz2',
       executable='rviz2',
       arguments=['-d', os.path.join(pkg_project_gazebo, 'config', 'beetlebot.rviz')],
       condition=IfCondition(LaunchConfiguration('rviz'))
    )

    # ROS-Gazebo Bridge
    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        parameters=[{
            'config_file': os.path.join(pkg_project_gazebo, 'config', 'beetlebot_ros_bridge.yaml'),
            'qos_overrides./tf_static.publisher.durability': 'transient_local',
        }],
        output='screen'
    )

        # For publishing and controlling the robot pose, we need joint states of the robot
    joint_state_publisher = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        output=['screen']
    )

    return LaunchDescription([

        declare_spawn_x,
        declare_spawn_y,
        declare_spawn_z,
        gz_spawn_entity,
        gz_sim,
        joint_state_publisher,
        DeclareLaunchArgument('rviz', default_value='true', description='Open RViz.'),
        bridge,
        robot_state_publisher,
        rviz
    ])