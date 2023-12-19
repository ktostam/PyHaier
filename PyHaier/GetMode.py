def GetMode(payload):
    """
    Mode display function
    :return:
    """
    if len(payload) == 1:
        if payload[0] == 0:
            mode="eco"
        elif payload[0] == 1:
            mode="quiet"
        elif payload[0] == 2:
            mode="turbo"
        else:
            mode="Mode Undefinde"

        return mode
    else:
        return "Bad payload length"
