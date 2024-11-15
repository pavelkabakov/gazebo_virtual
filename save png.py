
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from std_msgs.msg import Int32

rospy.init_node('cv')

bridge = CvBridge()


tag_pub = rospy.Publisher('/tag', Int32, queue_size=10)

state = 6
cnt = 0
def status_callback(data):
    global state
    state = data
    
def image_callback(data):
    global cnt
    img = bridge.imgmsg_to_cv2(data, 'bgr8')
    cv2.imwrite(f"{cnt}.png", img)
    cnt+=1
        


image_sub = rospy.Subscriber('/pioneer_max_camera/image_raw', Image, image_callback)
state_sub = rospy.Subscriber('/geoscan/flight/callback_event', Int32, status_callback)

rospy.spin()
