def GetTdef(payload):
    """
    Function for displaying Tdef parameter
    payload - register from 241 to 261
    :return:
    """
    if len(payload) == 22:
        tdef=[]
        tdefmsb=f'{divmod(int(hex(payload[12]), 16), 256)[0]:08b}'[0:4]
        tdeflsb=f'{divmod(int(hex(payload[13]), 16), 256)[0]:08b}'
        tdef = int(str(tdefmsb)+str(tdeflsb), 2)
        if tdef > 2047 :
            tdef -= 4095
        return tdef/10
    else:
        return "Bad payload length"
