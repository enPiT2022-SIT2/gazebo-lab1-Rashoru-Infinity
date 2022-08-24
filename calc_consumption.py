import rospy
from std_msgs.msg import String
from sensor_msgs.msg import BatteryState
import time

prev_time = time.time()
total_consumption = 0.0

def callback(data):
    global prev_time
    global total_consumption
    now = time.time()
    total_consumption += data.voltage * abs(data.current) * (now - prev_time)
    print("Total Power Consumption : {}[J]".format(total_consumption))
    prev_time = now
    

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('/mavros/battery', BatteryState, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
