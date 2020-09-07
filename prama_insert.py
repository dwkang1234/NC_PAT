#############
# .prm 파일에 parameter 추가



#file_path='D:/00_WORK/compare/bss/02_zone_move/02_zone_move_init/data.ws'


f_name = input("파라미터 name 입력: ")
f_path = "c:/py1530/%s.txt" % f_name
param1 = "parameter:" + f_name
param2 = 'ColumnName=' + f_name
param3 = 'Delimiter=' + ','

try:
    f = open(f_path, "a")  # 내용을 추가하기 위해서 'a'를 사용
    f.write(f"[{param1}]" + "\n") # 입력된 내용을 줄단위로 구분하기 위해 줄바꿈 문자 삽입
    f.write(param2 + "\n")
    f.write(param3 + "\n")
    print("파일 저장 성공!")
except:
    pass
finally:
    f.close()

