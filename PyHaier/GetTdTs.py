def GetTdTs(payload):
    """
    Thanks to Daniel Mentel
    Function for displaying Td and Ts paramameters, return as array
    payload - register from 241 to 261
    :return:
    """
    if len(payload) == 22:
        tdts=[]
        tdtsb=[f'{divmod(int(hex(payload[10]),16), 256)[1]:08b}'[4:], f'{divmod(int(hex(payload[10]), 16), 256)[1]:08b}'[0:4]]
        tdb=f'{divmod(int(hex(payload[11]), 16), 256)[0]:08b}'
        tsb=f'{divmod(int(hex(payload[11]), 16), 256)[1]:08b}'
        td = int(str(tdtsb[0])+str(tdb), 2)
        if (td > 2047) :
            td -= 4095
        tdts.append(td/10)
        ts = int(str(tdtsb[1])+str(tsb), 2)
        if (ts > 2047) :
            ts -= 4095
        tdts.append(ts/10)
        return tdts
    else:
        return "Bad payload length"
