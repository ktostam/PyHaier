def GetEEVLevel(payload):
    """
    Function for displaying EEV open level
    payload - register from 241 to 261
    :return:
    """
    if len(payload) == 22:
        eevlevel = divmod(int(hex(payload[5]), 16), 256)[0]
        return eevlevel
    else:
        return "Bad payload length"
