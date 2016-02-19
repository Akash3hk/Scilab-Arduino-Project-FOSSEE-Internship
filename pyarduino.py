#!/usr/bin/env python

"""
Its the solution of the Scilab-Arduino problem
that was asked by me to solve.

My Details ...
Name: Akash Parakandy

This module includes the Classes Analog, Digital,
Dcmotor and Servomotor

Also contains functions [checkfirmware()] for checking if
the firmware is correctly loaded or not, and
The function [locateport()] for identifying the Operating System(OS)
the script is running and COM port the Arduino Board is plunged in.
Also contains the functions [open_serial and close_serial]
"""

__author__ = "Akash Parakandy"

import serial
import sys
from serial import Serial
from serial.tools.list_ports import comports
from time import sleep

p1 = 0               # Initial Position of servo motor
p2 = 0               # Final Position of servo motor


class Analog:   # This class contains analog in/out functions

    def cmd_analog_in(Ano, pin):
        """
        Function Name:  cmd_analog_in(Ano, pin)
        Input Args:     Ano, pin no
        """
        self.cmd = ""
        a = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", "A", "B", "C", "D"]
        self.cmd = "A" + a[pin]
        ser.write(self.cmd)
        a = ser.read()
        return (int((1023-0)*int(ord(a))/(255-0)))

    def cmd_analog_out(Ano, pin, val):
        """
        Function Name:  cmd_analog_out(Ano, pin, val)
        Input Args:     Ano, pin no, val
        """
        a = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", "A", "B", "C", "D"]
        cmd = "W" + a[pin] + chr(val)  # numeric val converted to hex
        ser.write(cmd)


class Digital:  # This class contains digital in/out functions

    def cmd_digital_out(Ano, pin, val):
        """
        Function Name:  cmd_digital_out(Ano, pin, val)
        Input Args:     Ano, pin no, val
        """
        self.cmd = ""
        a = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", "A", "B", "C", "D"]
        self.cmd = "D"+"a"+a[pin]+"1"
        ser.write(self.cmd)
        self.cmd = ""
        self.cmd = "D"+"w"+a[pin]+str(val)  # val converted to string
        ser.write(self.cmd)

    def cmd_digital_in(Ano, pin):
        """
        Function Name:  cmd_digital_in(Ano, pin)
        Input Args:     Ano, pin
        """
        b = []        # Didn't understand why this  {b = []} was declared. But as was said not to change the
                    # declared variables, I kept it as it is.
                    # But according to me it shouldn't be here.
        self.cmd=""
        a = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", "A", "B", "C", "D"]
        self.cmd = "D"+"a"+a[pin]+"0"
        ser.write(self.cmd)
        self.cmd = ""
        self.cmd = "D"+"r"+a[pin]
        ser.write(self.cmd)
        a = ser.read()
        return a


class DCmotor:  # This class contains functions to operate the DC motor

    def cmd_dcmotor_setup(Ano, mode, mno, pin1, pin2):
        """
        Function Name:  cmd_dcmotor_setup(Ano, mode, mno, pin1, pin2)
        Input Args:     Ano, mode, mno, pin1, pin2
        Description:    This function connects the DC motor with the arduino board
        in the specified mode.
        """
        self.cmd = ""
        a = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", "A", "B", "C", "D"]
        self.cmd = "C"+a[mno]+a[pin1]+a[pin2]+a[mode]
        ser.write(self.cmd)

    def cmd_dcmotor_run(Ano, mno, val):
        """
        Function Name:  cmd_dcmotor_run(Ano, mno, val)
        Input Args:     Ano, mno, val
        Description:    This function operates the Dc motor as per the specified values
        """
        self.cmd = ""
        if (val <0):
            dirc = 0
        else:
            dirc = 1
        a = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", "A", "B", "C", "D"]
        self.cmd = "M"+a[mno]+a[dirc]+chr(abs(val))
        ser.write(self.cmd)

    def cmd_dcmotor_release(Ano, mno):
        """
        Function Name:  cmd_dcmotor_release(Ano, mno)
        Input Args:     Ano, mno
        Description:    This function detaches the DC motor from the Arduino board
        """
        self.cmd = ""
        a = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", "A", "B", "C", "D"]
        self.cmd = "M"+a[mno]+"r"
        ser.write(self.cmd)


class Servomotor:   # This class contains functions to operate the DC motor

    def cmd_servo_attach(Ano, servo): #1->pin=9  #2->pin=10
        """
        Function Name:  cmd_servo_attach(Ano, servo)
        Input Args:     Ano, servo
        Description:    This function attach["a"] the servo motor to arduino board
        """
        self.cmd = ""
        a = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", "A", "B", "C", "D"]
        self.cmd = "S"+"a"+a[servo]
        ser.write(self.cmd)

    def cmd_servo_detach(Ano, servo): #1->pin=9  #2->pin=10
        """
        Function Name:  cmd_servo_detach(Ano, servo)
        Input Args:     Ano, servo
        Description:    This function detach["d"] the servo motor to arduino board
        """
        self.cmd = ""
        a = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", "A", "B", "C", "D"]
        self.cmd = "S"+"d"+a[servo]
        ser.write(self.cmd)

    def cmd_servo_move(Ano, servo, angle): #1->pin=9  #2->pin=10
        """
        Function Name:  cmd_servo_move(Ano, servo, angle)
        Input Args:     Ano, servo, angle
        Description:    This function operates["w"] the servo motor to rotate with the specified angle
        """
        self.cmd = ""
        a = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", "A", "B", "C", "D"]
        self.cmd = "S"+"w"+a[servo]+chr(angle)
        ser.write(self.cmd)


def checkfirmware():
    """
    Function Name:  checkfirmware()
    Input Args:     None
    Description:    This function checks if the firmware is loaded correctly or not
    """
    global ser
    ser.write(chr(118))
    try:
        x = ser.read()
        if x == 'o':
            try:
                x = ser.read()
            except:
                sys.exit("aa..! error..! it seems correct firmware not loaded")
        else:
            sys.exit("aa..! error..! it seems correct firmware not loaded")
    except:
        sys.exit("aa..! error..! it seems correct firmware not loaded")


def locateport():
    """
    Function Name:  locateport()
    Input Args:     None
    Output:         port        The port at which the arduino is connected
    Description:    This function checks th OS it is running on and
    also identifies the com port the ARDUINO BOARD is connected to.
    And also returns the COM port the ARDUINO BOARD is connected.
    """
    port = ''
    if sys.platform.startswith('win'):      # For WINDOWS
        # port = ''
        ports = list(comports())
        for i in ports:
            for j in i:
                if 'Arduino' in j:
                    port = i[0]

    elif sys.platform.startswith('linux'):  # For LINUX
        b = []
        # port = ''
        ports = list(comports())
        for i in range(len(ports)):
            for x in range(7):
                portname = "/dev/ttyACM"+str(x)
                if ports[i][0] == portname:
                    b.append(ports[i][0])
        port = b[0]
    return port


def open_serial(ard_no, PortNo, baudrate):
    """
    Function Name:  open_serial(ard_no, PortNo, baudrate)
    Input Args:     ard_no, PortNo, baudrate
    Description:    Opens serial communication with the given PortNo
    and the specified Board Rate
    """
    global ser
    if PortNo == '':
        sys.exit("aa..error..! arduino not found")
    else:
        ser = Serial(PortNo, baudrate)
    sleep(2)
    checkfirmware()


def close_serial():
    """
    Function name:  close_serial()
    Input Args:     None
    Description:    Closes the serial communication channel
    """
    global ser
    ser.close()

