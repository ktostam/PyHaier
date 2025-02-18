def GetPdPs(payload):
    """
    Thanks to Daniel Mentel
    Function for displaying Pd set and actual and Ts set and actual paramameters, return as array (Pd for now)
    payload - register from 241 to 261
    :return:
    """
    if len(payload) == 22:
        pdps=[]
        pdset = divmod(int(hex(payload[5]), 16), 256)[1]*2/10 #B4D
        pdact = divmod(int(hex(payload[6]), 16), 256)[0]*2/10 #B4E
        psset = divmod(int(hex(payload[8]), 16), 256)[0]*2/10 #B51
        psact = divmod(int(hex(payload[8]), 16), 256)[1]*2/10 #B52

        pdps.append(pdset)
        pdps.append(pdact)
        pdps.append(psset)
        pdps.append(psact)
        return pdps
    else:
        return "Bad payload length"
