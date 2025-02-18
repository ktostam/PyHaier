def GetTSatPd(payload):
    """
    Thans to Daniel Mentel
    Function for displaying saturation temperatures for target and actual Pd, returned as array
    payload - register from 241 to 261
    :return:
    """
    if len(payload) == 22:
        tab=[]
        tab_4bit=[f'{divmod(int(hex(payload[6]),16), 256)[1]:08b}'[4:], f'{divmod(int(hex(payload[6]), 16), 256)[1]:08b}'[0:4]]
        b4f_8bit=f'{divmod(int(hex(payload[7]), 16), 256)[0]:08b}'
        b50_8bit=f'{divmod(int(hex(payload[7]), 16), 256)[1]:08b}'
        b4f = int(str(tab_4bit[0])+str(b4f_8bit), 2)
        if (b4f > 2047) :
            b4f -= 4095
        tab.append(b4f/10)
        b50 = int(str(tab_4bit[1])+str(b50_8bit), 2)
        if (b50 > 2047) :
            b50 -= 4095
        tab.append(b50/10)
        return tab
    else:
        return "Bad payload length"
