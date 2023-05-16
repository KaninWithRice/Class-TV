class TV:
    def __init__(tv, channel, volumelevel, onoroff):
        tv.name = tv
        tv.cha = channel
        tv.vlvl = volumelevel
        tv.on = onoroff

    def tv_start(tv):
        print(tv.name + "channel is" + tv.cha + "and volume level is" + tv.vlvl)

tv1 = TV("tv1", "02", "50")
tv2 = TV("tv2", "14", "70")

tv1.tv_start()
tv2.tv_start()