# Mohammad Mishal S. Noroña | BSCPE 1-5 | Assignment #6
# Introduction
print("")
print("WELCOME TO THE PROGRAM".center(40," ") )
print("By: Mishal Noroña".center(40," ") )
# Add Loading Time


# Import The Class
from ClassTv import TV
# TestTV Function
def TestTV():
    tv1 = TV(30,7,True)
    tv1.set_channel_num(30)
    tv1.set_volume_lvl(7)
    tv1_volume = tv1.get_volume_lvl
    print("Tv1's Channel is", (tv1.get_channel_num())," and Volume is ", (tv1.get_volume_lvl()))
TestTV()

def TestTV():
    tv2 = TV(40,6,True)
    tv2.set_channel_num(40)
    tv2.set_volume_lvl(6)
    tv2_volume = tv2.get_volume_lvl
    print("Tv2's Channel is", (tv2.get_channel_num())," and Volume is ", (tv2.get_volume_lvl()))
TestTV()
# 

# Create a remote
while True:
    switch = input("\n List of commands \n\n Off [off] \n Increase Volume [v+] \n Decrease Volume [v-] \n Increase Channel [c+] \n Decrease Channel [c-] \n Enter a command: ")

# If user enters v+ volume will go up
    if switch == "v+": 
        print("Tv1's Channel is", (tv1.get_channel_num())," and Volume is ", (volume_plus(tv1_volume())))
        print("Tv2's Channel is", (tv2.get_channel_num())," and Volume is ", (volume_plus(tv2_volume())))

