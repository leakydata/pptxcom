def rgb_to_hex(rgb):
    '''
    ws.Cells(1, i).Interior.color uses bgr in hex
    '''
    bgr = (rgb[2], rgb[1], rgb[0])
    strValue = '%02x%02x%02x' % bgr
    # print(strValue)
    iValue = int(strValue, 16)
    return iValue
