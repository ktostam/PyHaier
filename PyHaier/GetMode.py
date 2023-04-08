def GetMode(payload):
    """
    Mode display function
    :return:
    """
    if payload[0] == 0:
        mode="eco"
    elif payload[0] == 1:
        mode="silent"
    elif payload[0] == 2:
        mode="turbo"
    else:
        mode="Mode Undefinde"

    return mode