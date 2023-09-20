import rclpy

def main(agrs = None) -> None:
    rclpy.init(args=agrs)

    node = rclpy.create_node("Going_on")
    node.get_logger().info("Something ...")
    rclpy.spin(node)
    #node.destroy_node() #is the optional for rclpy.shutdown()
    rclpy.shutdown()

if __name__ == "__main__":
    main()