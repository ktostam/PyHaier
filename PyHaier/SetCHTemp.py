
def SetCHTemp(current,new):
    try:
        newtemp = []
        newtemp.append(1024 + int(hex(current[0])[4:6], 16))
        newtemp.append(int(str(hex(int(int(new) * 2)) + hex(current[1])[4:6]), 16))
        newtemp.append(int(hex(current[2])[2:6], 16))
        newtemp.append(int(hex(current[3])[4:6], 16))
        newtemp.append(int(hex(current[4])[4:6], 16))
        newtemp.append(current[5])
        return newtemp
    except:
        return "ERROR"