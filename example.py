# Import the MPU6050 class from the MPU6050.py file
from MPU6050 import MPU6050

# Create a new instance of the MPU6050 class
sensor = MPU6050(0x68)

# Get all the values using the GetAllValues() method
accel_data = sensor.get_accel_data()
gyro_data = sensor.get_gyro_data()
temp = sensor.get_temp()

# Print the sensorData
print("Accelerometer data")
print("x: " + str(accel_data['x']))
print("y: " + str(accel_data['y']))
print("z: " + str(accel_data['z']))

print("Gyroscope data")
print("x: " + str(gyro_data['x']))
print("y: " + str(gyro_data['y']))
print("z: " + str(gyro_data['z']))

print("Temp: " + str(temp) + " C")
