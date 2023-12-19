def GetDHWCurTemp(payload):
    """
    DHW current tank temperature display function
    :return:
    """
    if len(payload) == 16:
        dhwcurtemp = int(hex(payload[13]), 16)/10
        return dhwcurtemp
    else:
        return "Bad payload length"
