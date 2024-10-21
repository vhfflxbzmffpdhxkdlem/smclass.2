import random
r_num = random.randint(1,100)
# i = 0 
# while i<10:
#   in_num = int(input("숫자를 입력하세요"))
#   count = 0
#   if in_num > r_num:
#     print("숫자가 랜덤숫자보다 큽니다.")
#   elif in_num < r_num:
#     print("숫자가 랜덤숫자보다 작습니다.")
#   else:
#     print("정답입니다.",r_num)
#     count = 1
#     break
#   i += 1
# if count == 0:
#   print("10번의 도전에 실패했습니다. 정답은 : ",r_num)

for i in range(10):
    in_num = int(input("숫자를 입력하세요"))
    count = 0
    if in_num > r_num:
      print("숫자가 랜덤숫자보다 큽니다.")
      print(f"{i}번째 도전입니다.")
    elif in_num < r_num:
      print("숫자가 랜덤숫자보다 작습니다.")
      print(f"{i}번째 도전입니다.")
    else:
      print("정답입니다.",r_num)
      print(f"{i}번째 도전입니다.")
      count = 1
      break
if count == 0:
  print("10번의 도전에 실패했습니다. 정답은 : ",r_num)
