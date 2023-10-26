def GetTdTs(payload):
    """
    Thanks to Daniel Mentel
    Function for displaying Td and Ts paramameters, return as array
    payload - register from 241 to 261
    :return:
    """
    tdts=[]
    td = int(str(hex(payload[10])[4:6])+str(hex(payload[11])[2:4]), 16)/10
    ts = int(hex(payload[11])[4:6], 16)
    tdts.append(td)
    tdts.append(ts)
    return tdts
