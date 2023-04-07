def GetState(payload):
    """
    Mode display function
    :return:
    """
    state=hex(payload[0])[4:6]
    if state == "00":
        output = "OFF"
    elif state == "01":
        output = "ON"
    elif state == "03":
        output="Cool ON"
    elif state == "05":
        output="Heat ON"
    elif state == "87":
        output="Tank ON"
    elif state == "83":
        output="Cool+Tank ON"
    elif state == "85":
        output="Heat+Tank ON"
    elif state == "02":
        output="Cool OFF"
    elif state == "04":
        output="Heat OFF"
    elif state == "86":
        output="Tank OFF"
    elif state == "82":
        output="Cool+Tank OFF"
    elif state == "84":
        output="Heat+Tank OFF"
    else:
        output="State Undefinde"

    return output