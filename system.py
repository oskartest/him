import rospy
from std_msgs.msg import Float32
from RPi import GPIO


pin = 18




SERVO_MAX_DUTY = 12.5 
SERVO_MIN_DUTY = 2.5


steer = 0
speed = 0
sub = None

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

p = GPIO.PWM(pin, 50)
p.start(0)


def callback(data):
    steer = data.data
    rospy.loginfo(steer)
    p.ChangeDutyCycle(7.5-steer)
    

def main():
    global sub
    rospy.init_node('sub_steer', anonymous=True)
    sub = rospy.Subscriber('/steers', Float32, callback)
    rospy.spin()
    
    
    
if __name__ == '__main__':
    main()
