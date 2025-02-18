def GetTSatPs(payload):
    """
    Thanks To Daniel Mentel
    Function for displaying saturation temperatures for target and actual Ps, returned as array
    payload - register from 241 to 261
    :return:
    """
    if len(payload) == 22:
        tab=[]
        tab_4bit=[f'{divmod(int(hex(payload[9]),16), 256)[0]:08b}'[4:], f'{divmod(int(hex(payload[9]), 16), 256)[0]:08b}'[0:4]]
        b53_8bit=f'{divmod(int(hex(payload[9]), 16), 256)[1]:08b}'
        b54_8bit=f'{divmod(int(hex(payload[10]), 16), 256)[0]:08b}'
        b53 = int(str(tab_4bit[0])+str(b53_8bit), 2)
        if (b53 > 2047) :
            b53 -= 4095
        tab.append(b53/10)
        b54 = int(str(tab_4bit[1])+str(b54_8bit), 2)
        if (b54 > 2047) :
            b54 -= 4095
        tab.append(b54/10)
        return tab
    else:
        return "Bad payload length"
