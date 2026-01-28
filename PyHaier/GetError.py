def GetError(payload):
    """
    Function for displaying active error, return as int
    payload - register from 141 to 157
    :return:
    """
    if len(payload) == 16:
        error=payload[0] & 0xFF
        return error
    else:
        return "Bad payload length"
