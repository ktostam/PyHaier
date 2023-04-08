def SetState(current,new):
    """
    function to chance pump state

    :param current:
    :param new:
    :return:
    """
    newstate=[]
    if new%2 == 0:
        num=256
    else:
        num=34304

    if new == "off":
        if new%2 == 1:
            state=current[0]-1
        else:
            return -1
    elif new == "on":
        if new%2 == 0:
            state=current[0]+1
        else:
            return -1
    elif new == "C":
        state=3
    elif new == "H":
        state=5
    elif new == "T":
        state=87
    elif new == "CT":
        state=83
    elif new == "HT":
        state=85
    else:
        return -1
    newstate.append(num+int(str(int(state)),16))
    newstate.append(current[1])
    newstate.append(int(hex(current[2])[2:6], 16))
    newstate.append(int(hex(current[3])[4:6], 16))
    newstate.append(int(hex(current[4])[4:6], 16))
    newstate.append(current[5])

    return newstate
