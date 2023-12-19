def GetArchError(payload):
    """
    Function for displaying archive errors 1,2,3, return as array
    payload - register from 241 to 261
    :return:
    """
    if len(payload) == 22:
        archerr=[]
        err1 = divmod(int(hex(payload[19]), 16), 256)[0]
        err2 = divmod(int(hex(payload[19]), 16), 256)[1]
        err3 = divmod(int(hex(payload[20]), 16), 256)[0]

        archerr.append(err1)
        archerr.append(err2)
        archerr.append(err3)
        return archerr
    else:
        return "Bad payload length"
