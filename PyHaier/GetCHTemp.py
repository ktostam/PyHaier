def GetCHTemp(payload):
    """
    Cenral heating temperature display function
    :return:
    """
    chtemp = int(hex(payload[1])[2:4], 16)/2
    return chtemp
