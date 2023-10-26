def GetTao(payload):
    """
    Thanks to Daniel Mentel
    Function for displaying Tao parameter
    payload - register from 241 to 261
    :return:
    """
    tao = int(hex(payload[12])[2:4],16)/10

    return tao
