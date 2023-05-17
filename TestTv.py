# Mohammad Mishal S. Noroña | BSCPE 1-5 | Assignment #6
# Introduction
print("")
print("WELCOME TO THE PROGRAM".center(40," ") )
print("By: Mishal Noroña".center(40," ") )
# Add Loading Time
import time
import sys

done = 'false'

def animate():
        sys.stdout.write('\rLoading Please Wait ▒▒▒▒▒▒▒▒▒▒  0%')
        time.sleep(0.5)
        sys.stdout.write('\rLoading Please Wait █▒▒▒▒▒▒▒▒▒  10%')
        time.sleep(0.5)
        sys.stdout.write('\rLoading Please Wait ██▒▒▒▒▒▒▒▒  20%')
        time.sleep(0.5)
        sys.stdout.write('\rLoading Please Wait ███▒▒▒▒▒▒▒  30%')
        time.sleep(0.5)
        sys.stdout.write('\rLoading Please Wait ████▒▒▒▒▒▒  40%')
        time.sleep(0.5)
        sys.stdout.write('\rLoading Please Wait █████▒▒▒▒▒  50%')
        time.sleep(0.5)
        sys.stdout.write('\rLoading Please Wait ██████▒▒▒▒  60%')
        time.sleep(0.5)
        sys.stdout.write('\rLoading Please Wait ███████▒▒▒  70%')
        time.sleep(0.5)
        sys.stdout.write('\rLoading Please Wait ████████▒▒  80%')
        time.sleep(0.5)
        sys.stdout.write('\rLoading Please Wait █████████▒  90%')
        time.sleep(0.5)
        sys.stdout.write('\rLoading Please Wait ██████████ 100%')
        time.sleep(0.3)
        sys.stdout.write('\nTHE TV IS ON     \n')

animate()

# Import The Class
from ClassTv import TV
# Make a formula for volume up and channel up
def chaplus(channel):
    return channel + 1
def volplus(volumelevel):
    return volumelevel + 1
# Make a formula for volume down and channel down    
def chamin(channel):
    return channel - 1
def volmin(volumelevel):
    return volumelevel - 1
# Create a remote 
while True:
    switch = input("\n List of commands \n\n Off [off] \n Increase Volume [v+] \n Decrease Volume [v-] \n Increase Channel [c+] \n Decrease Channel [c-] \n Enter a command: ")
# If user enters v+ volume will go up
    if switch == "v+": 
        class TV:
            def __init__(tv, name, channel, volumelevel, status):
                tv.name = name
                tv.cha = channel
                tv.vlvl = volumelevel
                tv.stat = status

            def TestTV(tv):
                print("Status: ", tv.stat)
                print(tv.name, " channel is ", tv.cha, " and volume level is ", (volplus(tv.vlvl)))

            tv1 = TV("tv1's", 2, 30, "on")
            tv2 = TV("tv2's", 12, 40, "on")

            tv1.TestTV()
            tv2.TestTV()
# If user enters v- volume will go down
    elif switch == "v-":
        class TV:
            def __init__(tv, name, channel, volumelevel, status):
                tv.name = name
                tv.cha = channel
                tv.vlvl = volumelevel
                tv.stat = status

            def TestTV(tv):
                print("Status: ", tv.stat)
                print(tv.name, " channel is ", tv.cha, " and volume level is ", (volmin(tv.vlvl)))
                
            tv1 = TV("tv1's", 2, 30, "on")
            tv2 = TV("tv2's", 12, 40, "on")

            tv1.TestTV()
            tv2.TestTV()
# If user enters c+ channel will go up
    elif switch == "c+":
        class TV:
            def __init__(tv, name, channel, volumelevel, status):
                tv.name = name
                tv.cha = channel
                tv.vlvl = volumelevel
                tv.stat = status

            def TestTV(tv):
                print("Status: ", tv.stat)
                print(tv.name, " channel is ", (chaplus(tv.cha), " and volume level is ", tv.vlvl))
                
            tv1 = TV("tv1's", 2, 30, "on")
            tv2 = TV("tv2's", 12, 40, "on")

            tv1.TestTV()
            tv2.TestTV()
# If user enters c+ channel will go down
    elif switch == "c-":
        class TV:
            def __init__(tv, name, channel, volumelevel, status):
                tv.name = name
                tv.cha = channel
                tv.vlvl = volumelevel
                tv.stat = status

            def TestTV(tv):
                print("Status: ", tv.stat)
                print(tv.name, " channel is ", (chamin(tv.cha), " and volume level is ", tv.vlvl))
                
            tv1 = TV("tv1's", 2, 30, "on")
            tv2 = TV("tv2's", 12, 40, "on")

            tv1.TestTV()
            tv2.TestTV()
# If user enters off the TV will turn off        
    elif switch == "off":
        print("Thank you for using THE TELEVISION")
        break
    else:
        print("\nInvalid Input")
        print("Thank you for using THE TELEVISION")
        break        