import sys
import os
import struct
import binascii

#file_path = "D:/00_WORK/compare/bss/002.txt"
#file_path='D:/002.pcap'
file_path='D:/00_WORK/compare/bss/02_zone_move/02_zone_move_init/data.ws'

# data.ws 파일 데이터를 한줄씩 문자열로 만들어 리스트 형태로 리턴 "\n" 붙음
# readlines()   read()와 readline()과 다름

with open(file_path, "r+") as f:
    string = f.readlines()
    print(string)
    print(string[3])

# 리스트에 찾고자하는 문자열이 포함된 모든 데이터(element) 검색하여 리스트 형태로 반환
    search = "nick"
    match_list = list()
    for word in string:
        if search in word:
            match_list.append(word)
    print(match_list)

 # 추출한 리스트에서 특정 문자를 다른 문자로 모두 치환
    new_value = [s.replace('nickName', 'Testdata') for s in match_list]
    print(new_value)

print("_" * 80)
# 특정 문자를 hex값으로 표현

def str_to_hex(t):
#    t = 'PERF00001'
    a = f"{t}".encode()
    print(a)
    x=binascii.hexlify(a, '-')
    #=binascii.unhexlify(a)
    y=str(x,'ascii')
    print(x)
    print(y)

    z= y.replace("-", "\\x")
    print(z)
    w = "\\x" + z
    print(w)
    return w

print('hex 값은:', str_to_hex('PERF00001'))
