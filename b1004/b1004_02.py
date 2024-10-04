import random

# 랜덤숫자 : 1-100
random.randint(1,100)

# 10번도전에서
#입력한 숫자가 더 크면 작은수를 입력하셔야 합니다.
#입력한 숫자가 더 작으면 큰수를 입력하셔야 합니다.
#10번 도전에서 맞추지 못하면 , 10번 도전에 실패했습니다. 랜덤숫자 : 10
#도전에 성공했스빈다. 랜덤숫자 : 10

r_num = random.randint(1,100)
i = 0     #반복 횟수 변수
count = 0 #반복 확인 변호
while i < 10:
  num = int(input(f"{i+1}번째 숫자를 입력해주세요."))
  if num > r_num:
    print("더 작은수를 입력하셔야 합니다.")
  elif  num < r_num:
    print("더 큰수를 입력하셔야 합니다.")
  else:
    print("정답입니다.",r_num)
    count = 1
    break
  i += 1
if count == 0:
  print("10번 도전에 실패하셨습니다.",r_num)

# for i in range(10):
#   num = int(input("숫자를 입력해주세요."))
#   if num > r_num:
#     print("더 작은수를 입력하셔야 합니다.")
#   elif  num < r_num:
#     print("더 큰수를 입력하셔야 합니다.")
#   else:
#     print("정답입니다.",r_num)
#     count = 1
#     break
# if count == 0:
#   print("10번 도전에 실패하셨습니다.",r_num)