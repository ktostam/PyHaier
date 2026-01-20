def GetFirmware(payload):
    """
    Function for displaying current firmware version
    payload - register from 241 to 261
    :return:
    """
    if len(payload) == 22:
        firmware = divmod(int(hex(payload[18]), 16), 256)[0]/10
        return firmware
    else:
        return "Bad payload length"
