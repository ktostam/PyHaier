def GetFanRpm(payload):
    """
    Thanks to Daniel Mentel
    Function for displaying Fans rpms, return as array
    payload - register from 241 to 261
    :return:
    """
    fanrpm=[]
    fan1 = int(hex(payload[3])[4:6], 16)/2*10
    fan2 = int(hex(payload[4])[2:4], 16)/2*10
    fanrpm.append(fan1)
    fanrpm.append(fan2)
    return fanrpm
