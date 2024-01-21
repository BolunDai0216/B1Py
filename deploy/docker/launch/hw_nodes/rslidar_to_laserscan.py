from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            name='scanner', default_value='scanner',
            description='Namespace for sample topics'
        ),
        # Node(
        #     package='pointcloud_to_laserscan', node_executable='dummy_pointcloud_publisher',
        #     remappings=[('cloud', [LaunchConfiguration(variable_name='scanner'), '/cloud'])],
        #     parameters=[{'cloud_frame_id': 'cloud', 'cloud_extent': 2.0, 'cloud_size': 500}],
        #     node_name='cloud_publisher'
        # ),
        # Node(
        #     package='tf2_ros',
        #     node_executable='static_transform_publisher',
        #     node_name='static_transform_publisher',
        #     arguments=['0', '0', '0', '0', '0', '0', '1', 'map', 'cloud']
        # ),
        Node(
            package='pointcloud_to_laserscan', node_executable='pointcloud_to_laserscan_node',
            remappings=[
                        # ('cloud_in', [LaunchConfiguration(variable_name='scanner'), '/cloud']),
                        ('cloud_in', '/rslidar_points'),
                        ('scan', [LaunchConfiguration(variable_name='scanner'), '/scan'])
                       ],
            parameters=[{
                'target_frame': 'rslidar',
                'transform_tolerance': 0.01,
                'min_height': 0.0,
                'max_height': 1.0,
                'angle_min': -1.5708,  # -M_PI/2
                'angle_max': 1.5708,  # M_PI/2
                'angle_increment': 0.0087,  # M_PI/360.0
                'scan_time': 0.1,
                'range_min': 0.45,
                'range_max': 20.0,
                'use_inf': True,
                'inf_epsilon': 1.0
            }],
            node_name='pointcloud_to_laserscan'
        )
    ])
