#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

import curses
import math



class TurtleControllerNode(Node):
    
    def __init__(self):
        super().__init__("turtle_controller")
        self.cmd_vel_publisher_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 20)
        self.pose_subscriber = self.create_subscription(Pose, "/turtle1/pose", self.pose_callback, 10)
        self.get_logger().info("Turtle controler has been started. ")
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.stdscr.keypad(True)


    def pose_callback(self, pose: Pose):
        cmd = Twist()
        keycode = self.stdscr.getch()

        if keycode == curses.KEY_UP:
            cmd.linear.x = 1.0
        elif keycode == curses.KEY_DOWN:
            cmd.linear.x = -1.0
        elif keycode == curses.KEY_LEFT:
            cmd.angular.z = 1.0
        elif keycode == curses.KEY_RIGHT:
            cmd.angular.z = -1.0
        elif keycode == ord('q'):
            curses.nocbreak()
            self.stdscr.keypad(False)
            curses.echo()
            curses.endwin()
            rclpy.shutdown()
            exit()

        self.cmd_vel_publisher_.publish(cmd)

def main(args=None):
    rclpy.init(args=args)
    node = TurtleControllerNode()
    rclpy.spin(node) 
    rclpy.shutdown()