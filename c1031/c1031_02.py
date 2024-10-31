import random

# 임시비밀번호 생성 함수선언
def random_pw():
  a = random.randrange(0,10000) # 0~9999
  ran_num = f"{a:4}"  # 5412,0124,0001
  print("랜덤번호 : ",ran_num)
  return ran_num
