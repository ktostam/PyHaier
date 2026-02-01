def GetDHWCompensation(payload):
    """
    DHW? Compensation (A0d) display function
    :return:
    """
    if len(payload) == 6:
        dhwcom= int(int(payload[5] &0xFF)-30)/2
        return dhwcom
    else:
        return "Bad payload length"
