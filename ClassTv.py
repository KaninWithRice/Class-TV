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
# Ask for user's input
vol_input1 = int(input("TV1 Enter a Volume Level: "))
cha_input1 = int(input("TV1 Enter a Channel Number: "))

vol_input2 = int(input("TV2 Enter a Volume Level: "))
cha_input2 = int(input("TV2 Enter a Channel Number: "))
# Create a class
class TV:
    def __init__(tv, name, channel, volumelevel, status):
        tv.name = name
        tv.cha = channel
        tv.vlvl = volumelevel
        tv.stat = status

    def TestTV(tv):
        print("Status: ", tv.stat)
        print(tv.name, " channel is ", tv.cha, " and volume level is ", tv.vlvl)
# Create the objects
tv1 = TV("tv1's", cha_input1, vol_input1, "on")
tv2 = TV("tv2's", cha_input2, vol_input2, "on")
# Print output
tv1.TestTV()
tv2.TestTV()
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
            volume1 = "volumelist1.txt"
            with open("volumelist1.txt", "w") as volume1:
                volume1.write(str(volplus(vol_input1)))
            volume2 = "volumelist2.txt"
            with open("volumelist2.txt", "w") as volume2:
                volume2.write(str(volplus(vol_input2)))
            with open("volumelist1.txt","r") as volume1:
                tv1 = TV("tv1's", cha_input1, volume1.read(), "on")
            with open("volumelist2.txt","r") as volume2:
                tv2 = TV("tv2's", cha_input2, volume2.read(), "on")
            def TestTV(tv):
                print("Status: ", tv.stat)
                print(tv.name, " channel is ", tv.cha, " and volume level is ", tv.vlvl)
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
            volume1 = "volumelist1.txt"
            with open("volumelist1.txt", "w") as volume1:
                volume1.write(str(volmin(vol_input1)))
            volume2 = "volumelist2.txt"
            with open("volumelist2.txt", "w") as volume2:
                volume2.write(str(volmin(vol_input2)))
            with open("volumelist1.txt","r") as volume1:
                tv1 = TV("tv1's", vol_input1, volume1.read(), "on")
            with open("volumelist2.txt","r") as volume2:
                tv2 = TV("tv2's", vol_input2, volume2.read(), "on")
            def TestTV(tv):
                print("Status: ", tv.stat)
                print(tv.name, " channel is ", tv.cha, " and volume level is ", tv.vlvl)
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
            channel1 = "channellist1.txt"
            with open("channellist1.txt", "w") as channel1:
                channel1.write(str(chaplus(cha_input1)))
            channel2 = "channellist2.txt"
            with open("channellist2.txt", "w") as channel2:
                channel2.write(str(chaplus(cha_input2)))
            with open("channellist1.txt","r") as channel1:
                tv1 = TV("tv1's", channel1.read(), vol_input1, "on")
            with open("channellist2.txt","r") as channel2:
                tv2 = TV("tv2's", channel2.read(), vol_input2, "on")
            def TestTV(tv):
                print("Status: ", tv.stat)
                print(tv.name, " channel is ", tv.cha, " and volume level is ", tv.vlvl)
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
            channel1 = "channellist1.txt"
            with open("channellist1.txt", "w") as channel1:
                channel1.write(str(chamin(cha_input1)))
            channel2 = "channellist2.txt"
            with open("channellist2.txt", "w") as channel2:
                channel2.write(str(chamin(cha_input2)))
            with open("channellist1.txt","r") as channel1:
                tv1 = TV("tv1's", channel1.read(), vol_input1, "on")
            with open("channellist2.txt","r") as channel2:
                tv2 = TV("tv2's", channel2.read(), vol_input2, "on")
            def TestTV(tv):
                print("Status: ", tv.stat)
                print(tv.name, " channel is ", tv.cha, " and volume level is ", tv.vlvl)
            tv1.TestTV()
            tv2.TestTV()
# If user enters off the TV will turn off        
    elif switch == "off":
        print("Thank you for using THE TELEVISION")
        break
    else:
        print("\nInvalid Input")
        tv1.TestTV()
        tv2.TestTV()