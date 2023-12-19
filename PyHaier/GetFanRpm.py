def GetFanRpm(payload):
    """
    Thanks to Daniel Mentel
    Function for displaying Fans rpms, return as array
    payload - register from 241 to 261
    :return:
    """
    if len(payload) == 22:
        fanrpm=[]
        fan1 = divmod(int(hex(payload[3]), 16), 256)[1]/2*10
        fan2 = divmod(int(hex(payload[4]), 16), 256)[0]/2*10
        fanrpm.append(fan1)
        fanrpm.append(fan2)
        return fanrpm
    else:
        return "Bad payload length"
