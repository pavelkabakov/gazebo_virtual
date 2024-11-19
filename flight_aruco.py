# Information: https://clover.coex.tech/programming

import rospy
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

print('Take off and hover 1 m above the ground')
navigate(x=0, y=0, z=2, frame_id='body', auto_arm=True)
rospy.sleep(15) # Wait for 10 seconds

print('Fly forward 5 m')
navigate(x=0, y=5, z=2, frame_id='aruco_map')
rospy.sleep(30) # Wait for 30 seconds
print('Fly forward 5 m')
navigate(x=5, y=5, z=2, frame_id='aruco_map')
rospy.sleep(30) # Wait for 30 seconds
print('Fly forward 5 m')
navigate(x=5, y=0, z=2, frame_id='aruco_map')
rospy.sleep(30) # Wait for 30 seconds
print('Fly forward 5 m')
navigate(x=0, y=0, z=2, frame_id='aruco_map')
rospy.sleep(30) # Wait for 30 seconds

print(get_telemetry()) # Print drone's state

rospy.sleep(30) # Wait for 30 seconds

print('Perform landing')
land()

