def GetAntifreeze(payload):
    """
    Function for displaying if pump is on or off
    payload - register from 141 to 157
    :return:
    """
    if len(payload) == 16:
        if payload[0] & 2048:
            threeway = 'ANTIFREEZE'
        else:
            threeway = ''
        return threeway
    else:
        return "Bad payload length"
