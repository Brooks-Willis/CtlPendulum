from math import radians, degrees
from lib_robotis import *

def setup(maxspeed = radians(100)):
    
    dyn = USB2Dynamixel_Device()
    pend = Robotis_Servo(dyn, 1, 'MX')
    return (dyn, pend)

def main():
    dyn, pend = setup()
    command = raw_input('Next Command? ')
    while command != 'end':        
                
        if command == 'float':
            pend.disable_torque()     
            
        elif command == 'pos':
            angle = pend.read_angle() # In radians
            print angle, "radians,", degrees(angle), "degrees"

        elif command == 'alarm':
            print pend.read_alarm()

        elif command == 'goto':
            command = int(raw_input('Angle (radians)? '))
            pend.move_angle(command)

        else:
            print 'Invalid Command'   
        command = raw_input('Next Command? ')     

if __name__ == '__main__':
    main()