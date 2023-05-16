class TV:
    def __init__(tv, name, channel, volumelevel):
        tv.name = name
        tv.cha = channel
        tv.vlvl = volumelevel

    def TestTV(tv):
        print(tv.name + "channel is" + tv.cha + "and volume level is" + tv.vlvl)

tv1 = TV("tv1", " 22 ", " 50 ")
tv2 = TV("tv2", " 14 ", " 70 ")

tv1.TestTV()
tv2.TestTV()