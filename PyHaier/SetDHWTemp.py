def SetDHWTemp(current,new):
    try:
        newtemp = []
        newtemp.append(int(hex(current[0])[4:6], 16))
        newtemp.append(current[1])
        newtemp.append(int(hex(current[2])[2:6], 16))
        newtemp.append(int(hex(current[3])[4:6], 16))
        newtemp.append(512 + int(hex(current[4])[4:6], 16))
        newtemp.append(int(str(hex(int(new * 2)) + hex(current[5])[4:6]), 16))
        return newtemp
    except ValueError:
        return "ERROR"