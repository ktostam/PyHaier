def GetHeater(payload):
    """
    Function for displaying if heater is on or off
    payload - register from 141 to 157
    :return:
    """
    if len(payload) == 16:
        if payload & 256:
            heater = 'ON'
        else:
            heater = 'OFF'
        return heater
    else:
        return "Bad payload length"
