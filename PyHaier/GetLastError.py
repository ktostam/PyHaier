def GetLastError(payload):
    """
    Function for displaying last known error return int
    payload - register from 241 to 261
    :return:
    """
    if len(payload) == 22:
        error=payload[0] & 0xFF
        return error
    else:
        return "Bad payload length"

