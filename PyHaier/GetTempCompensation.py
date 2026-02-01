def GetTempCompensation(payload):
    """
    Temperature Compensation (A03) display function
    :return:
    """
    if len(payload) == 6:
        tempcom= int(int(payload[1] &0xFF)-30)/2
        return tempcom
    else:
        return "Bad payload length"
