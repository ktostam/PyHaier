def GetCompInfo(payload):
    """
    Thanks to Daniel Mentel
    Function for displaying compressor paramameters(set frequency, actual frequency, compressor current and compressor voltage), return as array
    payload - register from 241 to 261
    :return:
    """
    compressor=[]
    fact = int(hex(payload[2])[2:4],16)
    fset = int(hex(payload[3])[2:4],16)
    compcurr = int(hex(payload[15])[2:4], 16)*2/10
    compvolt = int(hex(payload[15])[4:6], 16)*4
    comptemp = int(hex(payload[14])[4:6], 16)/10
    compressor.append(fset)
    compressor.append(fact)
    compressor.append(compcurr)
    compressor.append(compvolt)
    compressor.append(comptemp)
    return compressor
