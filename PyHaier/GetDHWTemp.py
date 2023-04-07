def GetDHWTemp(payload):
    """
    DHW temperature display function
    :return:
    """
    dhwtemp = int(hex(payload[5])[2:4], 16)/2
    return dhwtemp