import rospy
import math
from clover import srv
from std_srvs.srv import Trigger

rospy.init_node('flight')

get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
land = rospy.ServiceProxy('land', Trigger)


def wait_arrival(tolerance=0.2):
    while not rospy.is_shutdown():
        telem = get_telemetry(frame_id='navigate_target')
        if math.sqrt(telem.x ** 2 + telem.y ** 2 + telem.z ** 2) < tolerance:
            break
        rospy.sleep(0.2)
    rospy.sleep(2)

# cnt = 0
# def log(data, name = "log.txt"):
#     global cnt
#     file = open(f"log{cnt}", 'w')
#     file.write(f"log_number: {cnt}" + "\n") 
#     file.write(data + "\n")
#     file.close()
#     cnt+=1


navigate(x = 0, y = 0, z = 1, frame_id = 'body', auto_arm = True)
wait_arrival()
navigate(x = 1, y = 0, z = 0, frame_id = 'body')
wait_arrival()
navigate(x = 0, y = 1, z = 0, frame_id = 'body')
wait_arrival()
navigate(x = -1, y = 0, z = 0, frame_id = 'body')
wait_arrival()
navigate(x = 0, y = -1, z = 0, frame_id = 'body')
wait_arrival()
land()
