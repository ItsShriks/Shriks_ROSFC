from typing import List
import rclpy
from rclpy.context import Context
from rclpy.node import Node
from rclpy.parameter import Parameter
from std_msgs.msg import String


class Subscriber(Node):
    def __init__(self):
        super().__init__(node_name = "my_subscribe")
        self.my_subscriber = self.create_subscription(String,"/world", self.my_callback,10)
    def my_callback(self, msg) -> None:
        self.get_logger().info(f"{msg.data}")


def main(agrs = None) -> None:
    rclpy.init(args=agrs)
    node = Subscriber()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()