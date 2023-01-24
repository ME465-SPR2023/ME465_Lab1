from setuptools import setup


package_name = 'ME465_Lab1'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['launch/rviz-launch.py', 'rviz/lab1.rviz']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='todo',
    maintainer_email='todo@todo.todo',
    description='ME465 Lab 1',
    license='TODO',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'lab1_node = ME465_Lab1.lab1_node:main'
        ],
    },
)
