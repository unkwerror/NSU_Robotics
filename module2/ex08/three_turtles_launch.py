from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Первое окно симулятора
        Node(
            package='turtlesim',
            namespace='turtlesim1',
            executable='turtlesim_node',
            name='sim'
        ),
        # Второе окно симулятора
        Node(
            package='turtlesim',
            namespace='turtlesim2',
            executable='turtlesim_node',
            name='sim'
        ),
        # Третье окно симулятора
        Node(
            package='turtlesim',
            namespace='turtlesim3',
            executable='turtlesim_node',
            name='sim'
        ),
        # Узел mimic для второй черепахи (следует за первой)
        Node(
            package='turtlesim',
            executable='mimic',
            name='mimic1',
            remappings=[
                ('/input/pose', '/turtlesim1/turtle1/pose'),
                ('/output/cmd_vel', '/turtlesim2/turtle1/cmd_vel'),
            ]
        ),
        # Узел mimic для третьей черепахи (следует за второй)
        Node(
            package='turtlesim',
            executable='mimic',
            name='mimic2',
            remappings=[
                ('/input/pose', '/turtlesim2/turtle1/pose'),
                ('/output/cmd_vel', '/turtlesim3/turtle1/cmd_vel'),
            ]
        )
    ])