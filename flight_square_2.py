# Information: https://clover.coex.tech/programming

import rospy
import math
from clover import srv
from std_srvs.srv import Trigger

rospy.init_node('flight')

get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
navigate_global = rospy.ServiceProxy('navigate_global', srv.NavigateGlobal)
set_position = rospy.ServiceProxy('set_position', srv.SetPosition)
set_velocity = rospy.ServiceProxy('set_velocity', srv.SetVelocity)
set_attitude = rospy.ServiceProxy('set_attitude', srv.SetAttitude)
set_rates = rospy.ServiceProxy('set_rates', srv.SetRates)
land = rospy.ServiceProxy('land', Trigger)

def wait_arrival(tolerance=0.2):
    while not rospy.is_shutdown():
        telem = get_telemetry(frame_id='navigate_target')
        if math.sqrt(telem.x ** 2 + telem.y ** 2 + telem.z ** 2) < tolerance:
            break
        rospy.sleep(0.2)
    rospy.sleep(2)


navigate(x = 0, y = 0, z = 1, frame_id = 'body', auto_arm = True)
wait_arrival()
navigate(x = 5, y = 0, z = 0, frame_id = 'body')
wait_arrival()
navigate(x = 0, y = 5, z = 0, frame_id = 'body')
wait_arrival()
navigate(x = -5, y = 0, z = 0, frame_id = 'body')
wait_arrival()
navigate(x = 0, y = -5, z = 0, frame_id = 'body')
wait_arrival()
land()

'''
print('Take off and hover 1 m above the ground')
navigate(x=0, y=0, z=1, frame_id='body', auto_arm=True)

# Wait for 5 seconds
rospy.sleep(5)

# print('Fly forward 1 m')
# navigate(x=1, y=0, z=0, frame_id='body')

# Wait for 5 seconds
rospy.sleep(5)

print('Perform landing')
land()
'''

