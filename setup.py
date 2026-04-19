from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'Cropcare'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    install_requires=[
        'setuptools',
        'pyserial',
        'pynput',
    ],
    zip_safe=True,
    maintainer='atharv',
    maintainer_email='atharvmudse@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'teleop_serial = Cropcare.teleop_serial:main',
            'cmd_vel_serial = Cropcare.cmd_vel_serial:main',
            'wasd_teleop = Cropcare.wasd_teleop:main',
        ],
    },
)
