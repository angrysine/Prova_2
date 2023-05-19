
import rclpy as rlc
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math

class Draw(Node):
    def __init__(self):
        super().__init__('draw')
        self.cmd_vel_pub = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.fase = 0
        self.timer = self.create_timer(1, self.send_velocity)
        self.get_logger().info('Drawer started')
        
        
    def send_velocity(self):
        msg = Twist()
        
        if self.fase ==0:
            msg.linear.x= 0
            msg.linear.y= 0.5
        if self.fase ==1:
            msg.linear.x=1.0
        if self.fase ==2:
            msg.angular.z=-2*math.pi/3
            
        if self.fase ==3:
            msg.linear.x=1.0
        if self.fase ==4:
            msg.angular.z=math.pi/3 + math.pi
        self.fase = (self.fase + 1) % 5
        self.get_logger().info('Fase: %d' % self.fase)


        self.cmd_vel_pub.publish(msg)

def main(args=None):
    rlc.init(args=args)
    node = Draw()
    rlc.spin(node)
    rlc.shutdown()