def SetMode(payload):

    if payload == "eco":
        mode=0
    elif payload == "silent":
        mode=1
    elif payload == "turbo":
        mode=2
    else:
        return -1

    newmode=[]
    newmode.append(256+int(mode))
    return newmode