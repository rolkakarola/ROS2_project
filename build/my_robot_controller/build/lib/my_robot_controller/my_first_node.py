#!/usr/bin/env python3
import rclpy 
from rclpy.node import Node

class myNode(Node): #class inhertis from the node that is from rclpy.node

    def __init__(self): #constructor
        super().__init__("first_node") #initialazing the node
        self.counter_ = 0
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info("Hello " + str(self.counter_))
        self.counter_ += 1

def main(args=None):
    rclpy.init(args=args) #starting ros2 communication, initializing ros2 communications and featires
    node = myNode() #creating node inside the main
    rclpy.spin(node) #node is going to run until we kiil it with ctrl c

    rclpy.shutdown() #closing ros2 communication


if __name__ == '__main__':
    main()
