def hexlify_byteString(byteString, delim="%"):
    ''' very simple way to hexlify a bytestring using delimiters '''
    retval = ""
    for intval in byteString:
        retval += ( '0123456789ABCDEF'[int(intval / 16)])
        retval += ( '0123456789ABCDEF'[int(intval % 16)])
        retval += delim
    return( retval[:-2])


x=b'PERF00001'

test = hexlify_byteString(x, r"\x")
print(test)