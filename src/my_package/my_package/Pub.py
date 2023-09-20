from typing import List
import rclpy
from rclpy.context import Context
from rclpy.node import Node
from rclpy.parameter import Parameter
from std_msgs.msg import String
class HelloYT(Node):
    def __init__(self):
        super().__init__(node_name = "hello")
        self.my_publisher = self.create_publisher(String, "/world",10)
        #my_publisher = self.create_publisher(String, "Topic Name", QoS)
        timer = self.create_timer(0.69, self.my_callback)
    def my_callback(self) -> None:
        my_msg = String()
        my_msg.data = "Hello Guy Number %s, Channel to my welcome"
        self.my_publisher.publish(my_msg)
def main(agrs = None) -> None:
    rclpy.init(args=agrs)
    node = HelloYT()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == "__main__":
    main()