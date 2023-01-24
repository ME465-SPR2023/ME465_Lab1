import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist


class Lab1Node(Node):
    def __init__(self):
        super().__init__("lab1_node")
        self.create_timer(0.05, self.timer_callback)
        
    def timer_callback(self):
        pass
        

def main(args=None):
    rclpy.init(args=args)
    node = Lab1Node()
    rclpy.spin(node)
    
    
if __name__ == "__main__":
    main()
