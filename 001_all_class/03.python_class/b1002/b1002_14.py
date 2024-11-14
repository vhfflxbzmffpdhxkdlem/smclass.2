import random   ##반듯이 넣어야 랜덤이 돌아감 ##

# r_num = random.randint(1,100)  while 안에있으면 돌때만다 랜덤숫자 같이 변경
r_num = random.randint(1,100)

##### for #####
for i in range(10):
  rull = int(input("숫자를 입력하세요"))
  count = 0
  if rull > r_num:
    print("숫자가 랜덤숫자보다 큽니다.")
  elif rull == r_num:
    print("정답입니다.")
    print("프로그램을 종료합니다.")
    count = 1
    break
  else:
    print("숫자가 랜덤숫자보다 작습니다.")
if count == 0:
  print("10번 도전에 실패했습니다.")

##### while ####
# i = 0           초기값
# while i<10:     조건식
#   rull = int(input("숫자를 입력하세요")) int 타입으로 변경
#   if rull > r_num:
#     print("숫자가 랜덤숫자보다 큽니다.")
#   elif rull == r_num:
#     print("정답입니다.")
#     count = 1
#     print("프로그램을 종료합니다.")
#     break
#   else:
#     print("숫자가 랜덤숫자보다 작습니다.")
#   i += 1        증감식
# if count == 0:
#   print("10번 도전에 실패했습니다.")


print(r_num)