def GetState(payload):
    """
    Mode display function
    :return:
    """

    if len(payload) != 6:
        return "Bad payload length"

    state = payload[0]

    if state & 1:
        onoff = 'ON'
    else:
        onoff = 'OFF'

    if state & 128:
        tank = 'TANK '
    else:
        tank = ''

    is_cool = state & 2
    is_heat = state & 4

    heatcool = ''

    if is_cool and is_heat:
        heatcool = ''
    elif is_cool:
        heatcool = 'COOL '
    elif is_heat:
        heatcool = 'HEAT '
    output = f'{heatcool}{tank}{onoff}'.strip()
    return output
