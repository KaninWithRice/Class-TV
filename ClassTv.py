vol_input1 = int(input("TV1 Enter a Volume Level: "))
cha_input1 = int(input("TV1 Enter a Channel Number: "))

vol_input2 = int(input("TV2 Enter a Volume Level: "))
cha_input2 = int(input("TV2 Enter a Channel Number: "))
class TV:
    def __init__(tv, name, channel, volumelevel, status):
        tv.name = name
        tv.cha = channel
        tv.vlvl = volumelevel
        tv.stat = status

    def TestTV(tv):
        print("Status: ", tv.stat)
        print(tv.name, " channel is ", tv.cha, " and volume level is ", tv.vlvl)
tv1 = TV("tv1's", cha_input1, vol_input1, "on")
tv2 = TV("tv2's", cha_input2, vol_input2, "on")

tv1.TestTV()
tv2.TestTV()

def chaplus(channel):
    return channel + 1
def volplus(volumelevel):
    return volumelevel + 1
    
def chamin(channel):
    return channel - 1
def volmin(volumelevel):
    return volumelevel - 1

while True:
    switch = input("\n List of commands \n\n Off [off] \n Increase Volume [v+] \n Decrease Volume [v-] \n Increase Channel [c+] \n Decrease Channel [c-] \n Enter a command: ")
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
        
    elif switch == "off":
        print("Thank you for using THE TELEVISION")
        break
    else:
        print("\nInvalid Input")
        tv1.TestTV()
        tv2.TestTV()
