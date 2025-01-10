import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'beetlebot_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),

    
    data_files=[

            ('share/ament_index/resource_index/packages',
                ['resource/' + package_name]),

        # Include our package.xml file       
        ('share/' + package_name, ['package.xml']),
        
        # Install model files in the share directory
        (os.path.join('share', package_name, 'models','beetlebot'), glob('models/beetlebot/*.sdf')),
        (os.path.join('share', package_name, 'models','beetlebot','sub_models','camera_sensor'), glob('models/beetlebot/sub_models/camera_sensor/*.sdf')),

        (os.path.join('share', package_name, 'sub_models','camera_sensor'), glob('sub_models/camera_sensor/*.sdf')),
        (os.path.join('share', package_name, 'launch'), glob('launch/*')),

        (os.path.join('share', package_name, 'config'), glob('config/*')),
        
        (os.path.join('share', package_name, 'worlds'), glob('worlds/*.sdf')),
    ],

    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kyrillosfekry',
    maintainer_email='kyrlosfekry@gmail.com',
    description='Beetlebot description package',
    license='Apache License 2.0',
    tests_require=['pytest'],

    entry_points={
        'console_scripts': [
        ],
    },
)
