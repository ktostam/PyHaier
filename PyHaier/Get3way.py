def Get3way(payload):
    """
    Function for displaying if pump is on or off
    payload - register from 141 to 157
    :return:
    """
    if len(payload) == 16:
        tmp = divmod(int(hex(payload[0]), 16), 256)[0]
        if tmp == 4:
            threeway = 'CH'
        elif tmp == 6 or tmp == 0:
            threeway = 'DHW'
        elif tmp == 36:
            threeway = 'DEFROST'
        else:
            threeway = str(tmp)
        return threeway
    else:
        return "Bad payload length"
