#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Imu

def imu_callback(data):
    # Получение данных акселерометра и гироскопа
    accel = data.linear_acceleration
    gyro = data.angular_velocity

    # Отображение данных в консоли
    rospy.loginfo(f"Accelerometer - x: {accel.x}, y: {accel.y}, z: {accel.z}")
    rospy.loginfo(f"Gyroscope - x: {gyro.x}, y: {gyro.y}, z: {gyro.z}")

def main():
    # Инициализация ROS-узла
    rospy.init_node('imu_listener', anonymous=True)

    # Подписка на топик с данными IMU (замените на реальный топик)
    rospy.Subscriber('/imu/data', Imu, imu_callback)

    # Ожидание сообщений
    rospy.spin()

if __name__ == '__main__':
    main()
