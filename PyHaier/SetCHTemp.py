
def SetCHTemp(current,new):
    try:
        newtemp = []
        newtemp.append(1024 + (current[0]&255))
        newtemp.append(int(new * 2)<<8 | (current[1]&255))
        newtemp.append(current[2])
        newtemp.append(current[3]&15)
        newtemp.append(current[4]&255)
        newtemp.append(current[5])
        return newtemp
    except:
        return "ERROR"
