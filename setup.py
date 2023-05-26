#!/usr/bin/python3
# File name   : setup.py
# Author      : Adeept

import os
import time

curpath = os.path.realpath(__file__)
thisPath = "/" + os.path.dirname(curpath)

def replace_num(file,initial,new_num):
    newline=""
    str_num=str(new_num)
    with open(file,"r") as f:
        for line in f.readlines():
            if(line.find(initial) == 0):
                line = (str_num+'\n')
            newline += line
    with open(file,"w") as f:
        f.writelines(newline)

try:
    replace_num("/boot/config.txt", '#dtparam=i2c_arm=on','dtparam=i2c_arm=on\nstart_x=1\n')
except:
    print('Error updating boot config to enable i2c. Please try again.')



try:
    os.system('sudo touch //home/pi/startup.sh')
    with open("//home/pi/startup.sh",'w') as file_to_write:
        #you can choose how to control the robot
        file_to_write.write("#!/bin/sh\nsleep 10\nsudo python3 " + thisPath + "/server/webServer.py")
#       file_to_write.write("#!/bin/sh\nsudo python3 " + thisPath + "/server/appserver.py")
except:
    pass


os.system('sudo chmod 777 //home/pi/startup.sh')

replace_num('/etc/rc.local','fi','fi\n//home/pi/startup.sh start')

# try: #fix conflict with onboard Raspberry Pi audio
#     os.system('sudo touch /etc/modprobe.d/snd-blacklist.conf')
#     with open("/etc/modprobe.d/snd-blacklist.conf",'w') as file_to_write:
#         file_to_write.write("blacklist snd_bcm2835")
# except:
#     pass

print('The program in Banana Pi has been installed. \nAfter turning on again, the Banana Pi will automatically run the program to set the servos port signal to turn the servos to the middle position, which is convenient for mechanical assembly.')
print('restarting...')
os.system("sudo reboot")
