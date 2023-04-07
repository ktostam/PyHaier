def GetMode(payload):
    """
    Mode display function
    :return:
    """
    if payload == "0":
        mode="eco"
    elif payload == "1":
        mode="silent"
    elif payload == "2":
        mode="turbo"
    else:
        mode="Mode Undefinde"

    return mode