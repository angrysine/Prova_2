
import rclpy as rlc
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math


class Fila():
    def __init__(self,lista = []) -> None:
        self.values = lista

    def add(self,value):
        self.values.insert(0,value)

    def remove(self):
        return self.values.pop()
    
class Pilha():
    def __init__(self) -> None:
        self.values = []
    def add(self,value):
        self.values.append(value)
    def remove(self):
        return self.values.pop()
    def __repr__(self) -> str:
        return str(self.values)
    

class Draw(Node):
    def __init__(self):
        super().__init__('draw')

        self.cmd_vel_pub = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.fase = 0
        self.fila = None
        self.pilha = None
        self.volta = False
        self.first_time = True
        self.timer = self.create_timer(1, self.send_velocity)
        self.get_logger().info('Drawer started')
        
        
    def send_velocity(self):
        msg = Twist()
        if self.fase == 0:
            if not self.volta:
                self.fila = Fila([[1.0,0.0],[0.0,1.0],[0.5,0.0],[0.0,0.5],[0.5,0.0],[0.0,0.5]])
            if not self.volta or self.first_time:
                self.pilha = Pilha()
                self.first_time = False
        print(self.pilha)
        if self.fase ==0:
           
            if self.volta:
                val = self.pilha.remove()
                msg.linear.x= -val[0]
                msg.linear.y= -val[1]
            else:
                val = self.fila.remove()
                msg.linear.x= val[0]
                msg.linear.y= val[1]
                self.pilha.add(val)
        if self.fase ==1:
            if self.volta:
                val = self.pilha.remove()
                msg.linear.x= -val[0]
                msg.linear.y= -val[1]
            else:
                val = self.fila.remove()
                msg.linear.x= val[0]
                msg.linear.y= val[1]
                self.pilha.add(val)
        if self.fase ==2:
            if self.volta:
                val = self.pilha.remove()
                msg.linear.x= -val[0]
                msg.linear.y= -val[1]
            else:
                val = self.fila.remove()
                msg.linear.x= val[0]
                msg.linear.y= val[1]
                self.pilha.add(val)
        if self.fase ==3:
            if self.volta:
                val = self.pilha.remove()
                msg.linear.x= -val[0]
                msg.linear.y= -val[1]
            else:
                val = self.fila.remove()
                msg.linear.x= val[0]
                msg.linear.y= val[1]
                self.pilha.add(val)
        if self.fase ==4:
            if self.volta:
                val = self.pilha.remove()
                msg.linear.x= -val[0]
                msg.linear.y= -val[1]
            else:
                val = self.fila.remove()
                msg.linear.x= val[0]
                msg.linear.y= val[1]
                self.pilha.add(val)
        if self.fase == 5:
            if self.volta:
                val = self.pilha.remove()
                msg.linear.x= -val[0]
                msg.linear.y= -val[1]
            else:
                val = self.fila.remove()
                msg.linear.x= val[0]
                msg.linear.y= val[1]
                self.pilha.add(val)

                
            

        if self.fase ==5:
            self.volta =  not self.volta
        self.fase = (self.fase + 1) % 7
        self.get_logger().info('Fase: %d' % self.fase)


        self.cmd_vel_pub.publish(msg)

def main(args=None):
    rlc.init(args=args)
    node = Draw()
    rlc.spin(node)
    rlc.shutdown()

main()