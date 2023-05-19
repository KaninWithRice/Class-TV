# Mohammad Mishal S. Noroña | BSCPE 1-5 | Assignment #6
# Introduction
print("")
print("WELCOME TO THE PROGRAM".center(40," ") )
print("By: Mishal Noroña".center(40," ") )
# Add Loading Time
import time
import sys

done = 'false'
def animation():
        sys.stdout.write('\n\rTurning ON Please Wait ▒▒▒▒▒▒▒▒▒▒  0%')
        time.sleep(0.5)
        sys.stdout.write('\rTurning ON Please Wait █▒▒▒▒▒▒▒▒▒  10%')
        time.sleep(0.5)
        sys.stdout.write('\rTurning ON Please Wait ██▒▒▒▒▒▒▒▒  20%')
        time.sleep(0.5)
        sys.stdout.write('\rTurning ON Please Wait ███▒▒▒▒▒▒▒  30%')
        time.sleep(0.5)
        sys.stdout.write('\rTurning ON Please Wait ████▒▒▒▒▒▒  40%')
        time.sleep(0.5)
        sys.stdout.write('\rTurning ON Please Wait █████▒▒▒▒▒  50%')
        time.sleep(0.5)
        sys.stdout.write('\rTurning ON Please Wait ██████▒▒▒▒  60%')
        time.sleep(0.5)
        sys.stdout.write('\rTurning ON Please Wait ███████▒▒▒  70%')
        time.sleep(0.5)
        sys.stdout.write('\rTurning ON Please Wait ████████▒▒  80%')
        time.sleep(0.5)
        sys.stdout.write('\rTurning ON Please Wait █████████▒  90%')
        time.sleep(0.5)
        sys.stdout.write('\rTurning ON Please Wait ██████████ 100%')
        time.sleep(0.3)
        sys.stdout.write('\n                SAMSUNG\n')
animation()
# Import The Class
from ClassTv import TV
# TestTV1 Function
def TestTV():
    tv1 = TV(30,7,1)
    tv1.set_statustv()
    tv1.set_channel_num(30)
    tv1.set_volume_lvl(7)
    print("Tv1's Channel is", (tv1.get_channel_num())," and Volume is ", (tv1.get_volume_lvl()),"\n") # Print output
TestTV()
# TestTV2 Function
def TestTV():
    tv2 = TV(40,6,True)
    tv2.set_statustv()
    tv2.set_channel_num(40)
    tv2.set_volume_lvl(6)
    print("Tv2's Channel is", (tv2.get_channel_num())," and Volume is ", (tv2.get_volume_lvl())) # Print Output
TestTV()

