def GetCompInfo(payload):
    """
    Thanks to Daniel Mentel
    Function for displaying compressor paramameters(set frequency, actual frequency, compressor current and compressor voltage), return as array
    payload - register from 241 to 261
    :return:
    """
    if len(payload) == 22:
        compressor=[]
        fact = divmod(int(hex(payload[2]), 16), 256)[1]
        fset = divmod(int(hex(payload[3]), 16), 256)[0]
        compcurr = divmod(int(hex(payload[15]), 16), 256)[0]*2/10
        compvolt = divmod(int(hex(payload[15]), 16), 256)[1]*4
        comptemp = divmod(int(hex(payload[14]), 16), 256)[1]/10
        compressor.append(fset)
        compressor.append(fact)
        compressor.append(compcurr)
        compressor.append(compvolt)
        compressor.append(comptemp)
        return compressor
    else:
        return "Bad payload length"
