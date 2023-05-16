class TV:
    def __init__(tv, name, channel, volumelevel, status):
        tv.name = name
        tv.cha = channel
        tv.vlvl = volumelevel
        tv.stat = status

    def TestTV(tv):
        print("Status: ", tv.stat)
        print(tv.name, " channel is ", tv.cha, " and volume level is ", tv.vlvl)
tv1 = TV("tv1's", 22, 50, "on")
tv2 = TV("tv2's", 14, 70, "on")

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

            def TestTV(tv):
                print("Status: ", tv.stat)
                print(tv.name, " channel is ", (tv.cha), " and volume level is ", volplus(tv.vlvl))
        tv1 = TV("tv1's", 22, 50, "on")
        tv2 = TV("tv2's", 14, 70, "on")

        tv1.TestTV()
        tv2.TestTV()
        
    elif switch == "off":
        print("Thank you for using THE TELEVISION")
        break
    else:
        print("\nInvalid Input")
        tv1.TestTV()
        tv2.TestTV()
