import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from std_msgs.msg import String


class TextToCmdVel(Node):
    def __init__(self):
        super().__init__('text_to_cmd_vel')

        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

        self.subscription = self.create_subscription(
            String,
            'cmd_text',
            self.listener_callback,
            10
        )

        self.get_logger().info("text_to_cmd_vel node started. Listening on 'cmd_text'...")

    def listener_callback(self, msg: String):
        command = msg.data.strip().lower()
        twist = Twist()

        if command == 'move_forward':
            twist.linear.x = 1.0
            twist.angular.z = 0.0
        elif command == 'move_backward':
            twist.linear.x = -1.0
            twist.angular.z = 0.0
        elif command == 'turn_left':
            twist.linear.x = 0.0
            twist.angular.z = 1.5
        elif command == 'turn_right':
            twist.linear.x = 0.0
            twist.angular.z = -1.5
        else:
            self.get_logger().warn(f"Unknown command: {command}")
            return

        self.publisher_.publish(twist)
        self.get_logger().info(f"Published Twist for command: {command}")


def main(args=None):
    rclpy.init(args=args)
    node = TextToCmdVel()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()


# usage example:
# ros2 run text_to_cmd_vel text_to_cmd_vel
# ros2 topic pub /cmd_text std_msgs/msg/String "data: 'turn_left'"
