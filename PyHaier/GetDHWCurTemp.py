def GetDHWCurTemp(payload):
    """
    DHW current tank temperature display function
    :return:
    """
    dhwcurtemp = int(hex(payload[13]), 16)/10
    return dhwcurtemp