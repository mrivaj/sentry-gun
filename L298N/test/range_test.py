import RPi.GPIO as GPIO
from stepper import Stepper
import time

motor_base = Stepper("Base", 12,16,20,21)
motor_base.set_speed(3)
print(motor_base.print_info())

try:
    for i in range(1):
        print ("15 steps <--")
        motor_base.move_forward(15)
        time.sleep(1)

        print("30 steps -->")
        motor_base.move_backwards(30)
        time.sleep(1)


        print ("15 steps <--")
        motor_base.move_forward(15+2)
        time.sleep(1)

finally:
    motor_base.off()
    print("DONE. All ok?")
