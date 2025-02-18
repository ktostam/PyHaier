def GetTao(payload):
    """
    Thanks to Daniel Mentel
    Function for displaying Tao parameter
    payload - register from 241 to 261
    :return:
    """
    if len(payload) == 22:
        tao=[]
        taomsb=f'{divmod(int(hex(payload[12]), 16), 256)[0]:08b}'[4:]
        taolsb=f'{divmod(int(hex(payload[12]), 16), 256)[1]:08b}'
        tao = int(str(taomsb)+str(taolsb), 2)
        if tao > 2047 :
            tao -= 4095
        return tao/10
    else:
        return "Bad payload length"
