def replacePram(original, old, new, count_right):
    repeat = 0
    text = original
    old_len = len(old)

    count_find = original.count(old)
    if count_right > count_find:  # 바꿀 횟수가 문자열에 포함된 old보다 많다면
        repeat = count_find  # 문자열에 포함된 old의 모든 개수(count_find)만큼 교체한다
    else:
        repeat = count_right  # 아니라면 입력받은 개수(count)만큼 교체한다

    while (repeat):
        find_index = text.rfind(old)  # 오른쪽부터 index를 찾기위해 rfind 사용
        text = text[:find_index] + new + text[find_index + old_len:]

        repeat -= 1

    return text


file_path = 'D:/00_WORK/compare/bss/02_zone_move/02_zone_move_init/data.ws'
#file_path = 'C:/tool/WinSock1/data.ws'
with open(file_path,"r+")as f:
    string=f.read()
    print(string)
#print(string[3])

#text = 'PERF00001\x00\x00'
print("*" * 40)

t2 = string[27:36:1]
print(t2)
print(string.replace(t2, '\x02\x03'))
#text = '123,456,789,999'
# text.replace(",", "", -1); print(text) #안됨

# text = replaceRight(text, ",", "", 2)
#print("결과 :")
#print(replaceRight(text, ",", "", 0))
#print(replacePram(text, "PERF00001", "PERF09999", 1))


#print(replaceRight(text, ",", "", 2))
#print(replaceRight(text, ",", "", 3))
#print(replaceRight(text, ",", "", 4))