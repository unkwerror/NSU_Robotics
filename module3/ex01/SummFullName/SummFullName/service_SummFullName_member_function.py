from full_name_interface.srv import FullNameSum

import rclpy
from rclpy.node import Node


class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(FullNameSum, 'full_name_sum', self.full_name_sum_callback)

    def full_name_sum_callback(self, request, response):
        response.full_name = request.first_name + " " + request.name + " " + request.last_name
        self.get_logger().info('Incoming request\nfirst_name: %s name: %s last_name: %s' % (request.first_name, request.name, request.last_name))

        return response


def main():
    rclpy.init()

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()