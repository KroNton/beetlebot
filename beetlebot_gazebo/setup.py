import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'beetlebot_gazebo'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        # Install world files in the share directory
        
        # (os.path.join('share', package_name, 'hooks'), glob('hooks/*')),
        # 
        (os.path.join('share', package_name, 'models','track1'), glob('models/track1/*.sdf')),  
        (os.path.join('share', package_name, 'models','track2'), glob('models/track2/*.sdf')),
        (os.path.join('share', package_name, 'models','house'), glob('models/house/*')),
        (os.path.join('share', package_name, 'launch'), glob('launch/*')),

        (os.path.join('share', package_name, 'config'), glob('config/*')),
        
        (os.path.join('share', package_name, 'worlds'), glob('worlds/*.sdf')),
    ],
    install_requires=['setuptools',
           'beetlebot_description',
                      
                      ],
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
