def GetPump(payload):
    """
    Function for displaying if pump is on or off
    payload - register from 141 to 157
    :return:
    """
    if len(payload) == 16:
        tmp = divmod(int(hex(payload[3]), 16), 256)[0]
        if tmp != 16:
            pump = 'ON'
        else:
            pump = 'OFF'
        return pump
    else:
        return "Bad payload length"
