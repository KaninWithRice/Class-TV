# Create a Class
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
tv1 = TV("tv1's", 2, 30, "on")
tv2 = TV("tv2's", 12, 40, "on")
# Print output
tv1.TestTV()
tv2.TestTV()