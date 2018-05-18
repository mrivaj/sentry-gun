#!/usr/bin/python
#import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_Stepper
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import sys, os, atexit, curses

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT()

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

# Inicializamos el motor de la base
myStepper = mh.getStepper(200, 1)  # 200 steps/rev, motor port #1
myStepper.setSpeed(30)             # 30 RPM

# Activamos curses para controlar la impresion
screen = curses.initscr()     # Cogemos el cursor
curses.noecho()               # Desactivamos el echo del input
curses.cbreak()               # Reconocemos inmediatamente las teclas
screen.keypad(True)           # Reconocemos teclas "especiales"

# Desactivamos el output
def disablePrint():
    sys.stdout = open(os.devnull, 'w')

# Activamos de nuevo
def enablePrint():
    sys.stdout = sys.__stdout__

def make_movement(direction, movement):
    disablePrint()
    myStepper.step(1, direction, movement)
    enablePrint()


try:
    while True:
        char = screen.getch()
        if char == ord('q'):
            break
        elif char == curses.KEY_RIGHT:
            screen.addstr(0, 0, 'Moviendo a derecha...')
            make_movement(Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.SINGLE)
        elif char == curses.KEY_LEFT:
            screen.addstr(0, 0, 'Moviendo a izquierda...')
            make_movement(Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.SINGLE)

finally:
    curses.nocbreak();
    screen.keypad(0);
    curses.echo()
    curses.endwin()