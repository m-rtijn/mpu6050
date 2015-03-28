# This program handles the communication over I2C
# between a Raspberry Pi and a MPU-6050 Gyroscope / Accelerometer combo
# Made by: MrTijn/Tijndagamer
# Copyright 2015

import smbus

class MPU6050:

    # Global Variables
    gravityMS2 = 9.80665
    address = None
    bus = smbus.SMBus(1)

    # Scale Modifiers
    accelScaleModifier2G = 16384.0
    accelScaleModifier4G = 8192.0
    accelScaleModifier8G = 4096.0
    accelScaleModifier16G = 2048.0
    gyroScaleModifier250Deg = 131.0
    gyroScaleModifier500Deg = 65.5
    gyroScaleModifier1000Deg = 32.8
    gyroScaleModifier2000Deg = 16.4

    # Pre-defined ranges
    accelRange2G = 0x00
    accelRange4G = 0x08
    accelRange8G = 0x10
    accelRange16G = 0x18

    gyroRange250Deg = 0x00
    gyroRange500Deg = 0x08
    gyroRange1000Deg = 0x10
    gyroRange2000Deg = 0x18

    # MPU-6050 Registers
    PWR_MGMT_1 = 0x6B
    PWR_MGMT_2 = 0x6C
    
    ACCEL_XOUT0 = 0x3B
    ACCEL_XOUT1 = 0x3C
    ACCEL_YOUT0 = 0x3D
    ACCEL_YOUT1 = 0x3E
    ACCEL_ZOUT0 = 0x3F
    ACCEL_ZOUT1 = 0x40

    TEMP_OUT0 = 0x41
    TEMP_OUT1 = 0x42

    GYRO_XOUT0 = 0x43
    GYRO_XOUT1 = 0x44
    GYRO_YOUT0 = 0x45
    GYRO_YOUT1 = 0x46
    GYRO_ZOUT0 = 0x47
    GYRO_ZOUT1 = 0x48

    ACCEL_CONFIG = 0x1C
    GYRO_CONFIG = 0x1B

    def __init__(self, address):
        self.address = address

        # Wake up the MPU-6050 since it starts in sleep mode
        self.bus.write_byte_data(self.address, self.PWR_MGMT_1, 0x00)

    # I2C communication methods

    def ReadI2CWord(self, register):
        # Read the data from the registers
        high = self.bus.read_byte_data(self.address, register)
        low = self.bus.read_byte_data(self.address, register + 1)

        # Bit magic
        value = (high << 8) + low

        if (value >= 0x8000):
            return -((65535 - value) + 1)
        else:
            return value

    # MPU-6050 Methods

    # Returns the temperature in degrees celcius read from the temperature sensor in the MPU-6050
    def GetTemp(self):
        # Get the raw data
        rawTemp = self.ReadI2CWord(self.TEMP_OUT0)

        # Get the actual temperature using the formule given in the
        # MPU-6050 Register Map and Descriptions revision 4.2, page 30
        actualTemp = (rawTemp / 340) + 36.53

        # Return the temperature
        return actualTemp

    # Sets the range of the accelerometer to range
    def SetAccelRange(self, accelRange):
        # First change it to 0x00 to make sure we write the correct value later
        self.bus.write_byte_data(self.address, self.ACCEL_CONFIG, 0x00)

        # Write the new range to the ACCEL_CONFIG register
        self.bus.write_byte_data(self.address, self.ACCEL_CONFIG, accelRange)

    # Reads the range the accelerometer is set to
    # If raw is True, it will return the raw value from the ACCEL_CONFIG register
    # If raw is False, it will return an integer: -1, 2, 4, 8 or 16. When it returns -1 something went wrong.
    def ReadAccelRange(self, raw = False):
        # Get the raw value
        rawData = self.bus.read_byte_data(self.address, self.ACCEL_CONFIG)

        if raw is True:
            return rawData
        elif raw is False:
            if rawData == self.accelRange2G:
                return 2
            elif rawData == self.accelRange4G:
                return 4
            elif rawData == self.accelRange8G:
                return 8
            elif rawData == self.accelRange16G:
                return 16
            else:
                return -1

    # Gets and returns the X, Y and Z values from the accelerometer
    # If g is True, it will return the data in g
    # If g is False, it will return the data in m/s^2
    def GetAccelData(self, g = False):
        # Read the data from the MPU-6050
        x = self.ReadI2CWord(self.ACCEL_XOUT0)
        y = self.ReadI2CWord(self.ACCEL_YOUT0)
        z = self.ReadI2CWord(self.ACCEL_ZOUT0)

        accelScaleModifier = None
        accelRange = self.ReadAccelRange(True)

        if accelRange == self.accelRange2G:
            accelScaleModifier = self.accelScaleModifier2G
        elif accelRange == self.accelRange4G:
            accelScaleModifier = self.accelScaleModifier4G
        elif accelRange == self.accelRange8G:
            accelScaleModifier = self.accelScaleModifier8G
        elif accelRange == self.accelRange16G:
            accelScaleModifier = self.accelScaleModifier16G
        else:
            print("Unkown range - accelScaleModifier set to self.accelScaleModifier2G")
            accelScaleModifier = self.accelScaleModifier2G
        
        x = x / accelScaleModifier
        y = y / accelScaleModifier
        z = z / accelScaleModifier

        if g is True:
            return {'x': x, 'y': y, 'z': z}
        elif g is False:
            x = x * gravityMS2
            y = y * gravityMS2
            z = z * gravityMS2
            return {'x': x, 'y': y, 'z': z}
        

    # Sets the range of the gyroscope to range
    def SetGyroRange(self, gyroRange):
        # First change it to 0x00 to make sure we write the correct value later
        self.bus.write_byte_data(self.address, self.GYRO_CONFIG, 0x00)

        # Write the new range to the ACCEL_CONFIG register
        self.bus.write_byte_data(self.address, self.GYRO_CONFIG, gyroRange)

    # Reads the range the gyroscope is set to
    # If raw is True, it will return the raw value from the GYRO_CONFIG register
    # If raw is False, it will return 250, 500, 1000, 2000 or -1. If the returned value is equal to -1 something went wrong.
    def ReadGyroRange(self, raw = False):
        # Get the raw value
        rawData = self.bus.read_byte_data(self.address, self.GYRO_CONFIG)

        if raw is True:
            return rawData
        elif raw is False:
            if rawData == self.gyroRange250Deg:
                return 250
            elif rawData == self.gyroRange500Deg:
                return 500
            elif rawData == self.gyroRange1000Deg:
                return 1000
            elif rawData == self.gyroRange2000Deg:
                return 2000
            else:
                return -1

    # Gets and returns the X, Y and Z values from the gyroscope
    def GetGyroData(self):
        # Read the raw data from the MPU-6050
        x = self.ReadI2CWord(self.GYRO_XOUT0)
        y = self.ReadI2CWord(self.GYRO_YOUT0)
        z = self.ReadI2CWord(self.GYRO_ZOUT0)

        gyroScaleModifier = None
        gyroRange = self.ReadGyroRange(True)
        
        if gyroRange == self.gyroRange250Deg:
            gyroScaleModifier = self.gyroScaleModifier250Deg
        elif gyroRange == self.gyroRange500Deg:
            gyroScaleModifier = self.gyroScaleModifier500Deg
        elif gyroRange == self.gyroRange1000Deg:
            gyroScaleModifier = self.gyroScaleModifier1000Deg
        elif gyroRange == self.gyroRange2000Deg:
            gyroScaleModifier = self.gyroScaleModifier2000Deg
        else:
            print("Unkown range - gyroScaleModifier set to self.gyroScaleModifier250Deg")
            gyroScaleModifier = self.gyroScaleModifier250Deg
        
        x = x / gyroScaleModifier
        y = y / gyroScaleModifier
        z = z / gyroScaleModifier

        return {'x': x, 'y': y, 'z': z}      

    # Gets and returns the X, Y and Z values from the accelerometer and from the gyroscope and the temperature from the temperature sensor
    def GetAllData(self):
        temp = GetTemp()
        accel = GetAccelData()
        gyro = GetGyroData()

        return [accel, gyro, temp]
