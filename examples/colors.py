def rgb_to_hex(rgb): # color uses bgr in hex
    bgr = (rgb[2], rgb[1], rgb[0]) # convert rgb into bgr
    str_value = '%02x%02x%02x' % bgr # convert bgr in hex
    int_value = int(str_value, 16) # convert hex to integer
    return int_value
