def GetArchError(payload):
    """
    Function for displaying archive errors 1,2,3, return as array
    payload - register from 241 to 261
    :return:
    """
    archerr=[]
    err1 = int(hex(payload[19])[2:4],16)
    err2 = int(hex(payload[19])[4:6],16)
    err3 = int(hex(payload[20])[2:4],16)

    archerr.append(err1)
    archerr.append(err2)
    archerr.append(err3)
    return archerr
