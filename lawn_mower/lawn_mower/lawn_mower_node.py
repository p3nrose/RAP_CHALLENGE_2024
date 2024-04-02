import rclpy
from rclpy.node import Node

class LawnMowerNode(Node):
    def __init__(self) -> None:
        super().__init__('lawn_mower')
        self.get_logger().info("Hallo Welt von Gruppe 7")

    def our_algorithm():
        pass


def main(args=None):
    rclpy.init(args=args)
    lawnMower_node = LawnMowerNode()

    try:
        rclpy.spin(lawnMower_node)
    finally:
        lawnMower_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
