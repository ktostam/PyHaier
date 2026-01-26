def Get3way(payload):
    """
    Function for displaying if pump is on or off
    payload - register from 141 to 157
    :return:
    """
    if len(payload) == 16:
        if payload[0] & 8192:
            threeway = 'DEFROST'
        elif payload[0] & 2048:
            threeway = 'ANTIFREEZE'
        elif payload[0] & 512:
            threeway='DHW'
        elif payload[0] & 1024:
            threeway = 'CH'
        else:
            threeway=str(payload[0])
        return threeway
    else:
        return "Bad payload length"
