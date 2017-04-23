from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='mpu6050-raspberrypi',
      version='1.0.3.4',
      description='A Python module for accessing the MPU-6050 digital accelerometer and gyroscope on a Raspberry Pi.',
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Topic :: Software Development :: Libraries',
          'Programming Language :: Python :: 2.7',
          'Operating System :: POSIX :: Linux',
      ],
      keywords='mpu6050 raspberry',
      url='https://github.com/Tijndagamer/mpu6050',
      author='MrTijn/Tijndagamer',
      author_email='mrtijn@riseup.net',
      license='MIT',
      packages=['mpu6050'],
      scripts=['bin/mpu6050-example'],
      zip_safe=False,
      long_description=readme())
