# Import the MPU6050 class from the MPU6050.py file
from MPU6050 import MPU6050

# Create a new instance of the MPU6050 class
sensor = MPU6050(0x68)

# Get all the values using the GetAllValues() method
accelData = sensor.GetAccelData()
gyroData = sensor.GetGyroData()
temp = sensor.GetTemp()

# Print the sensorData
print("Accelerometer data")
print("x: " + str(accelData['x']))
print("y: " + str(accelData['y']))
print("z: " + str(accelData['z']))

print("Gyroscope data")
print("x: " + str(gyroData['x']))
print("y: " + str(gyroData['y']))
print("z: " + str(gyroData['z']))

print("Temp: " + str(temp) + " C")
