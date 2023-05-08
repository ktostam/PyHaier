def SetState(current,new):
    """
    function to change pump state

    :param current:
    :param new:
    :return:
    """
    try:
        newstate=[]
        if len(str(current[3])) <4 or len(str(current[0])) <4:
            return "Error"

        if new == "off":
            if int(hex(current[0])[4:6])%2 == 1:
                state=int(hex(current[0])[4:6])-1
            else:
                return -1
        elif new == "on":
            if int(hex(current[0])[4:6]%2) == 0:
                state=int(hex(current[0])[4:6])+1
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

        if state%2 == 0:
            num=256
        else:
            num=34304
        newstate.append(num+int(str(int(state)),16))
        newstate.append(current[1])
        newstate.append(int(hex(current[2])[2:6], 16))
        newstate.append(int(hex(current[3])[4:6], 16))
        newstate.append(int(hex(current[4])[4:6], 16))
        newstate.append(current[5])

        return newstate
    except:
        return "ERROR"
