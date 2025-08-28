from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    joint_state_broadcaster_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "joint_state_broadcaster",
            "--controller-manager",
            "/controller_manager"
        ]
    )
    
    joint_velocity_controller = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "joint_velocity_controller",  
            "--controller-manager",
            "/controller_manager"
        ]
    )
    wheel_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["beetlebot_diff_drive_controller", 
                   "--controller-manager", 
                   "/controller_manager"]         
                   )
    

    return LaunchDescription([
        joint_state_broadcaster_spawner,
        # joint_velocity_controller,
        wheel_controller_spawner
    ])