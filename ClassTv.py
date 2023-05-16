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