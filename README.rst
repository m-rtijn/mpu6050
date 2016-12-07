mpu6050
=======

A Python module for accessing the MPU-6050 digital accelerometer and gyroscope on a Raspberry Pi.

Example
-------

Assuming that the address of your MPU-6050 is 0x68, you can read read accelerometer data like this:

::

    >>> from mpu6050 import mpu6050

    >>> sensor = mpu6050(0x68)

    >>> accelerometer_data = sensor.get_accel_data()

Dependencies
------------

* smbus-cffi

You can either install smbus-cffi using pip or install the python-smbus package using apt.

Installation
------------

1. pip install from PyPi
::

    pip install mpu6050-raspberrypi

2. Clone the repository and run setup.py
::
    
    git clone https://github.com/Tijndagamer/mpu6050.git
    python setup.py install

Issues & Bugs
-------------

Please report any issues or bugs here:

    https://github.com/Tijndagamer/mpu6050/issues


