def GetDHWCurTemp(payload):
    """
    DHW current temperature display function
    :return:
    """
    dhwcurtemp = int(hex(payload[0]), 16)/10
    return dhwcurtemp