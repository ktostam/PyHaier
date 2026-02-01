def SetState(current,new):
    """
    function to change pump state

    :param current:
    :param new:
    :return:
    """
    if len(current) !=6:
        return 'Bad current frame length'

    try:
        newstate=[]
        if new == "off":
            state=int(current[0] & 0xff) -1
        elif new == "on":
            state=int(current[0] & 0xff) +1
        elif new == "C":
            state=3
        elif new == "H":
            state=5
        elif new == "T":
            state=135
        elif new == "CT":
            state=131
        elif new == "HT":
            state=133
        else:
            return -1

        if new == "on" or new == "off":
            num=256
        else:
            num=34304
        newstate.append(num+state)
        newstate.append(current[1])
        newstate.append(current[2])
        newstate.append(current[3]&15)
        newstate.append(current[4]&255)
        newstate.append(current[5])


        return newstate
    except:
        return "ERROR"
