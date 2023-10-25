def GetCompFreq(payload):
    """
    Function for displaying compressor set frequency and actual frequency paramameters, return as array
    payload - register from 241 to 261
    :return:
    """
    fsetfact=[]
    fact = int(hex(payload[2])[2:4],16)
    fset = int(hex(payload[3])[2:4],16)

    fsetfact.append(fset)
    fsetfact.append(fact)
    return fsetfact
