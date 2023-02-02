import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist


class Lab1Node(Node):
    def __init__(self):
        super().__init__("lab1_node")
        self.create_timer(0.05, self.timer_callback)
        self.vel = self.create_publisher(
            Twist,
            "/ctrl_vel",
            5,
        )
        self.start_time = self.get_clock().now().nanoseconds / 1e9
        
    def timer_callback(self):
        msg = Twist()
        time = self.get_clock().now().nanoseconds / 1e9
        if time - self.start_time <= 2:
            msg.linear.x = 0.2
            msg.angular.z = -0.5
        self.vel.publish(msg)
        

def main(args=None):
    rclpy.init(args=args)
    node = Lab1Node()
    rclpy.spin(node)
    
    
if __name__ == "__main__":
    main()
