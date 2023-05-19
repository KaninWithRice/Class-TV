class TV:
    def __init__(tv,name ,channel, volumelevel, status):
        tv.name = name
        tv.cha = channel
        tv.vlvl = volumelevel
        tv.stat = status
        
    def statustv(tv):
        tv.status = True
        print("Status: ON")
    def statustv(tv):
        tv.status = False
        print("Status: OFF")

    def get_channel_num(tv):
        return tv.cha
    def set_channel_num (tv, channel):
        if 0 <= channel <= 120:
            print (tv.name,"'s channel is", tv.cha)
        else:
            print ("Enter a channel Between (1-120)")
            return tv.cha

    def get_volume_lvl(tv):
        return