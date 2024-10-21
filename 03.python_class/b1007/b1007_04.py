import random

# 1,25 사이의 랜덤숫자를 생성해서 출력하시오.
# num = int(random.random()*25+1)

# a_list = []
#1-25 까지 랜덤숫자를 입력, 중복은 제거하고 출력을 하시오.
# while True:
#   num = random.randint(1,25)
#   if num not in a_list:
#     a_list.append(num)
#     if len(a_list) == 25:
#       break
# print(a_list)

# while len(a_list)<25:
#   num = random.randint(1,25)
#   if num not in a_list:
#     a_list.append(num)
# print(a_list)
# print(len(a_list))

# 1-25까지 램덤으로 배치 - random.sample()
# 범위 리스트 ,25개 추출(중복추출 안됨.)
# a_list = []
# for i in range(25):
#   a_list.append(i+1)

# 1-25까지 램덤으로 배치 - random.choices()
# 범위 리스트 ,25개 추출(중복추출 가능.)
# b_list = random.choices(a_list,k=25)
# print(b_list)


# random.sample()
# b_list = random.sample(a_list,25)  
# print(b_list)