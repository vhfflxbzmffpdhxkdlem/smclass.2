import random
# tName = ["이름","국어","영어","수학","합계"]
# fName = ["바나나","오렌지","체리","파인애플","코코넛"]
fruit = {"바나나":"banana","오렌지":"orange","체리":"cherry","파인애플":"pineapple","코코넛":"coconut"}
fName = list(fruit.keys())
print(fName)

# random.shuffle(fName)  # 원본이 변경됨.

# fName 램덤순서로 영문퀴즈 시작
re_fName = random.sample(fName,5) 
for i in re_fName:
  search = input(f"{i}의 영문을 입력하세요")
  if fruit[i] == search:
    print("정답입니다.",fruit[i],search)
  else:
    print("오답입니다.",fruit[i],search)


# for i in range(5):
#   ran = fName[random.randint(0,4)]
#   print(ran)

# for key in fruit.keys():
#   search = input(f"{key}의 영문을 입력하세요")
#   if fruit[key] == search:
#     print("정답입니다.",fruit[key],search)
#   else:
#    print("오답입니다.",fruit[key],search)

# fName 순서대로 영문퀴즈 시작
# print("[ 영단어 맞추기 ]")
# search = input("바나나의 영문을 입력하세요.")
# if fruit['바나나'] == search:
#   print("정답입니다.",fruit['바나나'],search)
# else:
#   print("오답입니다.",fruit['바나나'],search)


# 바나나를 입력하면 영어로 banana 로 출력하시오.
# print(fruit["바나나"])
# print(fruit["오렌지"])

# while True:
#   search = input("과일 이름을 입력하세요")
#   if search in fruit:
#     print(fruit[search])
#   else:
#     print("찾는 단어가 없습니다.")
#     break