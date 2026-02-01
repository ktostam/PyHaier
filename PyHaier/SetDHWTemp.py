def SetDHWTemp(current,new):
    try:
        newtemp = []
        newtemp.append(current[0]&255)
        newtemp.append(current[1])
        newtemp.append(current[2])
        newtemp.append(current[3]&15)
        newtemp.append(512 + (current[4]&255))
        newtemp.append(int(new * 2)<<8 | (current[5]&255))
        return newtemp
    except ValueError:
        return "ERROR"
