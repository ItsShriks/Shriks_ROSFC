from typing import List
import rclpy
from rclpy.context import Context
from rclpy.node import Node
from rclpy.parameter import Parameter
from std_msgs.msg import String

class increment(Node):
    def __init__(self):
        super().__init__(node_name = "increment")
        self.publisher = self.create_publisher(String, "/world",10)
        #my_publisher = self.create_publisher(String, "Topic Name", QoS)
        timer = self.create_timer(0.69, self.my_callback)
        self.i = 0
    def my_callback(self) -> None:
        my_msg = String()
        my_msg.data = "%d"% self.i
        self.publisher.publish(my_msg)
        #self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i +=1
def main(agrs = None) -> None:
    rclpy.init(args=agrs)
    node = increment()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == "__main__":
    main()