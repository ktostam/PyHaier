def SetDHWCompensation(current, newcompe):
    """
    DHW Compensation (A0d) set function
    :return:
    """
    try:
        frame=[]
        pumpstate=current[0]&255
        currtemp=current[5] >>8
        compensation=30+newcompe*2
        frame.append(2048+pumpstate)
        frame.append(current[1])
        frame.append(current[2])
        frame.append(current[3]&15)
        frame.append(current[4]&255)
        frame.append((currtemp <<8)|compensation)
        return frame
    except:
        return "ERROR"
