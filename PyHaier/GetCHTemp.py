def GetCHTemp(payload):
    """
    Cenral heating temperature display function
    :return:
    """
    if len(payload) == 6:
        chtemp = int(hex(payload[1])[2:4], 16)/2
        return chtemp
    else:
        return "Bad payload length"
