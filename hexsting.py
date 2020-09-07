import binascii
from binascii import unhexlify

t= 'PERF00001'
a= f"{t}".encode()

#a=f'b{t}'
print(a)
x=binascii.hexlify(a, '-')
#=binascii.b2a_hex(a)
y=str(x,'ascii')
print(x)
print(y)

z= y.replace("-", "\\x")
print(z)
w = "\\x" + z
print(w)


