def GetTao(payload):
    """
    Thanks to Daniel Mentel
    Function for displaying Tao parameter
    payload - register from 241 to 261
    :return:
    """
    if len(payload) == 22:
        tao = divmod(int(hex(payload[12]), 16), 256)[1]
        if tao > 127 :
            tao -= 254
        return tao/10
    else:
        return "Bad payload length"
