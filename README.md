# beetlebot

This repository contains the **Beetlebot** robot description and its configurations, designed for seamless integration into any custom Gazebo world with custom GUI configurations.

## Repository Structure

```
├── beetlebot_description
│   ├── beetlebot_description
│   │   └── __init__.py
│   ├── models
│   │   ├── beetlebot
│   │   │   ├── model.config
│   │   │   └── model.sdf
│   │   ├── empty_world.sdf
│   │   ├── sub_models
│   │   │   ├── camera_sensor.sdf
│   │   │   ├── ground_plane.sdf
│   │   │   ├── imu_sensor.sdf
│   │   │   ├── lidar_sensor.sdf
│   │   │   └── simple_robot_template.sdf
│   │   └── world_gui.config
│   ├── package.xml
│   ├── resource
│   │   └── beetlebot_description
│   ├── setup.cfg
│   ├── setup.py
│   └── test
│       ├── test_copyright.py
│       ├── test_flake8.py
│       └── test_pep257.py
└── README.md
```

### Key Components

#### 1. **`models/`**
- **`beetlebot/`**: Contains the core robot description files (`model.config` and `model.sdf`).
- **`sub_models/`**: Includes modular components like sensors (`camera_sensor.sdf`, `lidar_sensor.sdf`, etc.), enabling customizable configurations.
- **`empty_world.sdf`**: A base world template.
- **`world_gui.config`**: Configuration file for customizing the GUI layout.

#### 2. **`package.xml`**
Defines the ROS 2 package dependencies and metadata.

#### 3. **`setup.py` and `setup.cfg`**
Standard Python package setup files for easy installation and integration.

#### 4. **`test/`**
Unit tests for ensuring code quality and compliance with Python standards.

---

## Features

- **Separate SDF Robot Module**: Each robot component is defined as a standalone SDF module for maximum flexibility and reusability.
- **Custom World GUI Configuration Plugins**: Includes a configurable GUI plugin to tailor the simulation interface to your needs.
- **360° LIDAR Plugin**: Provides a simulated LIDAR sensor capable of full 360° scanning for obstacle detection and mapping.
- **Differential Drive Plugin**: Implements a differential drive controller for robot mobility, ensuring smooth and accurate navigation.

---

## Getting Started

### Prerequisites

Ensure you have the following:

- **ROS 2 Jazzy** installed on your system.
- **Gazebo Harmonic** for robot simulation.

### Installation

1. Clone the repository :
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

#### To run the robot in the default configuration:

1. Navigate to the models directory:
   ```bash
   cd /beetlebot/beetlebot_description/models
   ```
2. Launch the simulation:
   ```bash
   gz sim empty_world.sdf
   ```

#### To run the robot with a custom GUI configuration:

1. Navigate to the models directory:
   ```bash
   cd /beetlebot/beetlebot_description/models
   ```
2. Launch the simulation with the GUI configuration:
   ```bash
   gz sim empty_world.sdf --gui-config world_gui.config
   ```

### Using Beetlebot in Custom Worlds

1. Add the `beetlebot_description` model to your world by referencing the `model.sdf` file.
2. Customize the sensors or other components by editing the relevant `.sdf` files in the `sub_models/` directory.
3. Update the `world_gui.config` file to define your preferred GUI layout.
4. Launch the simulation in Gazebo:
   ```bash
   gz sim <your_world_name>.sdf --gui-config world_gui.config
   ```


## Future Enhancements

- Add more sensors
  - camera sensors for perciption tasks.
  - IMU sensor
  
- Improve the modularity of sub-models.
    - include sensors as sub-models in robot main .sdf
    - prepare separate pkg for gazebo worlds and config files `beetlebot_gazebo`
  - 
- complete the `URDF format` for beetlebot .

---

For further information, please consult the source files or contact the repository maintainer.

