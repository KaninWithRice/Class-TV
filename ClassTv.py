# Create a Class
class TV:
    # Define TV Objects
    def __init__(tv, name, channel, volumelevel, status):
        tv.name = name
        tv.cha = channel
        tv.vlvl = volumelevel
        tv.stat = status
    # TV Status Function    
    def statustv(tv):
        tv.status = True
        print("Status: ON")
    def statustv(tv):
        tv.status = False
        print("Status: OFF")
    # Channel Function
    def get_channel_num(tv):
        return tv.cha
    def set_channel_num(tv, channel):
        if 0 <= channel <= 120:
            print (tv.name,"'s Channel is : ", tv.cha)
        else:
            print ("Enter a Channel Between (1-120)")
            return tv.cha
    # Volume Function
    def get_volume_lvl(tv):
        return tv.vlvl
    def set_volume_lvl(tv, volumelevel):
        if 0 <= volumelevel <= 7:
            print (tv.name,"'s Volume Level is : ", tv.vlvl)
        else:
            print ("Enter a Volume Level Between (1-7)")
            return tv.vlvl
    # Channel and Volume Up
    def channel_plus(tv):
        tv.cha += 1
    def volume_plus(tv):
        tv.vlvl += 1    
    # Channel and Volume Down
    def channel_minus(tv):
        tv.cha -= 1
    def volume_minus(tv):
        tv.vlvl -= 1