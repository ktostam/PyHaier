def SetHeater(current,new):
    """
    Heater (A04) set function 0=OFF 1=ON
    :return:
    """
    try:
        frame=[]
        pumpstate=current[0]&255
        heaterstate=new*8+pumpstate
        frame.append(4096+heaterstate)
        frame.append(current[1])
        frame.append(current[2])
        frame.append(current[3]&15)
        frame.append(current[4]&255)
        frame.append(current[5])
        return frame
    except:
        return "ERROR"
