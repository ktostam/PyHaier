def SetTempCompensation(current, newcompe):
    """
    Temperature Compensation (A03) set function
    :return:
    """
    try:
        frame=[]
        pumpstate=current[0]&255
        currtemp=current[1] >>8
        compensation=30+newcompe*2
        frame.append(2048+pumpstate)
        frame.append((currtemp <<8)|compensation)
        frame.append(current[2])
        frame.append(current[3]&15)
        frame.append(current[4]&255)
        frame.append(current[5])
        return frame
    except:
        return "ERROR"
