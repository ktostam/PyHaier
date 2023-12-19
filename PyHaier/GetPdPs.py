def GetPdPs(payload):
    """
    Thanks to Daniel Mentel
    Function for displaying Pd set and actual and Ts set and actual paramameters, return as array (Pd for now)
    payload - register from 241 to 261
    :return:
    """
    if len(payload) == 22:
        pdps=[]
        pdset = divmod(int(hex(payload[5]), 16), 256)[1]*2/10
        pdact = divmod(int(hex(payload[6]), 16), 256)[0]*2/10
        pdps.append(pdset)
        pdps.append(pdact)
        return pdps
    else:
        return "Bad payload length"
