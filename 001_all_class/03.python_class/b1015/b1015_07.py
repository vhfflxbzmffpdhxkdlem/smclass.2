students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]
stu = "6,홍길자,100,100,100,300,100.0,0" #파일에 저장하는 형태
sArr = stu.split(",")

# 문자열 -> 리스트변경 -> 타입을 변경
for i,s in enumerate(sArr):
  if str.isdigit(s)  :  # int타입이 변경이 가능한지??
    sArr[i] = int(s)
sArr[6] = float(sArr[6])

students.append(sArr)
# sudents 리스트에 1명 추가
print(students)



# stu = "6,홍길자,100,100,100,300,100.0,0"
# sArr = stu.split(",")
# print(sArr)

# for i,s in enumerate(sArr):
#   if str.isdigit(s)  :  # int타입이 변경이 가능한지??
#     sArr[i] = int(s)
# sArr[6] = float(sArr[6])
# print(sArr)

# s = "11"   # 문자열
# print(str.isdigit(s))  # 문자열이 숫자이면 True, 아니면 False
# ss = "a"
# print(str.isdigit(ss))

# students = [
#   {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
#   {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
#   {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
#   {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
#   {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
# ]

# stu_1 = "6,홍길자,100,100,100,300,100.0,0"
# key_1 = ["no","name","kor","eng","math","total","avg","rank"]
# stuArr = stu_1.split(",")
# print(stuArr)
# print(type(int(stuArr[2])))


# # 딕셔너리 생성방범
# dict_1 = {"no":int(stuArr[0]),"name":stuArr[1],"kor":int(stuArr[2]),"eng":int(stuArr[3]),"math":int(stuArr[4]),"total":int(stuArr[5]),"avg":int(stuArr[6]),"rank":int(stuArr[7])}
# print(dict_1)
# # zip 
# dict_list = dict(zip(key_1,stuArr))
# print(dict_list)
