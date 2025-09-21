from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    
    twist_relay_node = Node(
        package="beetlebot_controller",
        executable="twist_relay.py",
        name="twist_relay",
        parameters=[{"use_sim_time": True}]
    )

    return LaunchDescription([
        twist_relay_node
    ])