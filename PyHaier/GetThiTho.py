def GetThiTho(payload):
    """
    Function for displaying Thi and Tho paramameters, return as array
    payload - register from 141 to 156
    :return:
    """
    if len(payload) == 16:
        thitho=[]
        thiob=[f'{divmod(int(hex(payload[7]), 16), 256)[0]:08b}'[0:4], f'{divmod(int(hex(payload[7]), 16), 256)[0]:08b}'[4:]]
        thib=f'{divmod(int(hex(payload[7]), 16), 256)[1]:08b}'
        thob=f'{divmod(int(hex(payload[8]), 16), 256)[0]:08b}'
        thi = int(str(thiob[1])+str(thib), 2)
        if thi > 2047 :
            thi -= 4095
        thitho.append(thi/10)
        tho = int(str(thiob[0])+str(thob), 2)
        if tho > 2047 :
            tho -= 4095
        thitho.append(tho/10)
        return thitho
    else:
        return "Bad payload length"
