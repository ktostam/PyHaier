def GetTwiTwo(payload):
    """
    Function for displaying Twi and Two paramameters, return as array
    payload - register from 141 to 156
    TODO: need to confirm its good, Two/Twi cannot be more than 51.1°C
    :return:
    """
    twitwo=[]
    twiab = int(hex(payload[5])[5:6],16)
    twoab = int(hex(payload[5])[4:5],16)
    twib = int(hex(payload[6])[2:4],16)
    twob = int(hex(payload[6])[4:6],16)

    twi = int(hex((twiab*256) + twib), 16)/10
    twitwo.append(twi)
    two = int(hex((twoab * 256) + twob), 16) / 10
    twitwo.append(two)
    return twitwo