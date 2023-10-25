def GetEEVLevel(payload):
    """
    Function for displaying EEV open level
    payload - register from 241 to 261
    :return:
    """
    eevlevel = int(hex(payload[5])[2:4],16)

    return eevlevel
