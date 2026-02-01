def SetPump(current,new):
    """
    Circulation Pump (A05) set function 0=OFF 1=ON
    :return:
    """
    try:
        frame=[]
        pumpstate=current[0]&255
        cpumpstate=new*32+pumpstate
        frame.append(8192+cpumpstate)
        frame.append(current[1])
        frame.append(current[2])
        frame.append(current[3]&15)
        frame.append(current[4]&255)
        frame.append(current[5])

        return frame
    except:
        return "ERROR"
