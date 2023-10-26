def GetPdPs(payload):
    """
    Thanks to Daniel Mentel
    Function for displaying Pd set and actual and Ts set and actual paramameters, return as array (Pd for now)
    payload - register from 241 to 261
    :return:
    """
    pdps=[]
    pdset = int(hex(payload[5])[4:6], 16)*2/10
    pdact = int(hex(payload[6])[2:4], 16)*2/10
    pdps.append(pdset)
    pdps.append(pdact)
    return pdps
