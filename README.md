Here is the updated documentation with the camera angle control part moved before the "Using Beetlebot in Custom Worlds" section:

# Beetlebot Documentation

## Overview

This repository contains the **Beetlebot** robot description and its configurations, designed for seamless integration into any custom Gazebo world with custom GUI configurations.

!Beetlebot

## Features

- **Separate SDF Robot Module**: Each robot component is defined as a standalone SDF module for maximum flexibility and reusability.
- **Custom World GUI Configuration Plugins**: Includes a configurable GUI plugin to tailor the simulation interface to your needs.
- **360° LIDAR Plugin**: Provides a simulated LIDAR sensor capable of full 360° scanning for obstacle detection and mapping.
- **Differential Drive Plugin**: Implements a differential drive controller for robot mobility, ensuring smooth and accurate navigation.
- **RGB Camera**: Equipped with an RGB camera for visual feedback.
- **Position Joint Control**: Allows changing the camera angle using position joint control.

## Getting Started

### Prerequisites

Ensure you have the following:

- **ROS 2 Jazzy** installed on your system.
- **Gazebo Harmonic** for robot simulation.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/KroNton/beetlebot.git
   ```
2. Build the ROS 2 package:
   ```bash
   colcon build
   ```
3. Source the setup file:
   ```bash
   source install/setup.bash
   ```

### Running the Robot

#### To run the robot in the empty world:
```bash
ros2 launch beetlebot_gazebo beetlebot_empty_world.launch.py
```

#### To run the robot in the warehouse world:
```bash
ros2 launch beetlebot_gazebo beetlebot_warehouse.launch.py
```

#### To run the robot in the track world:
```bash
ros2 launch beetlebot_gazebo beetlebot_track_world.launch.py
```

### Controlling the Robot

- Use the keyboard arrow keys to move the robot.
- Press `k` to stop the robot.

### Controlling the Camera Angle

You can control the camera angle by publishing to the `/camera_angle` topic.

#### Using the Terminal

1. Open a new terminal.
2. Publish a message to the `/camera_angle` topic to change the camera angle. For example, to set the camera angle to 0.5 radians:
   ```bash
   ros2 topic pub /camera_angle std_msgs/msg/Float64 "{data: 0.5}"
   ```

![Robot in Warehouse](imgs/robot_warehouse.gif)

### Using Beetlebot in Custom Worlds

1. Add the `beetlebot_description` model to your world by referencing the 

model.sdf

 file.
2. Customize the sensors or other components by editing the relevant `.sdf` files in the `sub_models/` directory.
3. Update the `world_gui.config` file to define your preferred GUI layout.
4. Launch the simulation in Gazebo:
   ```bash
   gz sim <your_world_name>.sdf --gui-config world_gui.config
   ```

## Configuration Files

### `beetlebot_gazebo/config/beetlebot_ros_bridge.yaml`

This file configures the ROS-Gazebo bridge for topic communication.

```yaml
---
- ros_topic_name: "/cmd_vel"
  gz_topic_name: "/cmd_vel"
  ros_type_name: "geometry_msgs/msg/Twist"
  gz_type_name: "gz.msgs.Twist"
  direction: ROS_TO_GZ

- ros_topic_name: "/clock"
  gz_topic_name: "/world/beetlebot_world/clock"
  ros_type_name: "rosgraph_msgs/msg/Clock"
  gz_type_name: "gz.msgs.Clock"
  direction: GZ_TO_ROS

- ros_topic_name: "/odom"
  gz_topic_name: "/odom"
  ros_type_name: "nav_msgs/msg/Odometry"
  gz_type_name: "gz.msgs.Odometry"
  direction: GZ_TO_ROS

- ros_topic_name: "/lidar"
  gz_topic_name: "/lidar"
  ros_type_name: "sensor_msgs/msg/LaserScan"
  gz_type_name: "gz.msgs.LaserScan"
  direction: GZ_TO_ROS

- ros_topic_name: "/joint_states"
  gz_topic_name: "/joint_states"
  ros_type_name: "sensor_msgs/msg/JointState"
  gz_type_name: "gz.msgs.Model"
  direction: GZ_TO_ROS

- ros_topic_name: "/camera/image_raw"
  gz_topic_name: "/camera/image_raw"
  ros_type_name: "sensor_msgs/msg/Image"
  gz_type_name: "gz.msgs.Image"
  direction: GZ_TO_ROS

- ros_topic_name: "camera/depth/image_raw"
  gz_topic_name: "camera/depth/image_raw"
  ros_type_name: "sensor_msgs/msg/Image"
  gz_type_name: "gz.msgs.Image"
  direction: GZ_TO_ROS

- ros_topic_name: "/tf"
  gz_topic_name: "/model/beetlebot/pose"
  ros_type_name: "tf2_msgs/msg/TFMessage"
  gz_type_name: "gz.msgs.Pose_V"
  direction: GZ_TO_ROS

- ros_topic_name: "/tf_static"
  gz_topic_name: "/model/beetlebot/pose_static"
  ros_type_name: "tf2_msgs/msg/TFMessage"
  gz_type_name: "gz.msgs.Pose_V"
  direction: GZ_TO_ROS

- ros_topic_name: "/camera_angle"
  gz_topic_name: "/camera_angle"
  ros_type_name: "std_msgs/msg/Float64"
  gz_type_name: "gz.msgs.Double"
  direction: ROS_TO_GZ
```

## Future Enhancements

- Add more sensor plugins.
- Improve the robot's navigation algorithms.
- Add support for additional simulation environments.

