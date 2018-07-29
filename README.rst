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

Either the ``python-smbus`` or ``python3-smbus`` package, according to your
Python version.

Installation
------------

There are two ways of installing this package: via PyPi or via the git repository.
Installing from the git repository insures that you have the absolute latest
version installed, but this can be prone to bugs.

1. install the python-smbus package
::

    sudo apt install python3-smbus

2a. Install this package from PyPi repository
::

    pip install mpu6050-raspberrypi

Or:

2b. Clone the repository and run setup.py
::
    
    git clone https://github.com/Tijndagamer/mpu6050.git
    python setup.py install

Issues & Bugs
-------------

Please report any issues or bugs here:

    https://github.com/Tijndagamer/mpu6050/issues


License
-------

::

    Copyright (c) 2015, 2016, 2017, 2018 Martijn (MrTijn) and contributors
    Licensed under the MIT License. For more information, see ``LICENSE``.
