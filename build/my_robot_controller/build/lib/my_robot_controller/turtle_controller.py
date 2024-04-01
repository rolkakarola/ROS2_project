#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class TurtleControllerNode(Node):
    
    def __init__(self):
        super().__init("turtle_controller")
        self.get_logger().info("Turtle controler has been started. ")



def main(args=None):
    rclpy.init(args=args)
    node = TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()