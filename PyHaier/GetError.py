def GetError(payload):
    """
    Function for displaying archive errors 1,2,3, return as array
    payload - register from 241 to 261
    :return:
    """
    if len(payload) == 22:
        error = divmod(int(hex(payload[1]), 16), 256)[1]

        return error
    else:
        return "Bad payload length"
