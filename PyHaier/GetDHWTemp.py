def GetDHWTemp(payload):
    """
    DHW temperature display function
    :return:
    """
    if len(payload) == 6:
        dhwtemp = int(hex(payload[5])[2:4], 16)/2
        return dhwtemp
    else:
        return "Bad payload length"
