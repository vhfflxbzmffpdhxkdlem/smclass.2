# 두수를 입력받아 , 두수까지 합계를 구하시오.
# 예) 3,8 -> 3+4+5+6+7+8

# 3. if문 사용
# a = int(input("첫번째 숫자를 입력해주세요."))
# b = int(input("두번째 숫자를 입력해주세요."))
# c = 0
# if a > b:
#   a,b = b,a   #파이썬만 가능 - 두개 변수 취환
# #   c = a; a = b; b = c   # 나머지 언어들의 변수취환
# sum = 0
# for i in range(a,b+1):
#   sum += i
# print("합계 : ",sum)


# 1. if문 사용
# a = int(input("첫번째 숫자를 입력해주세요."))
# b = int(input("두번째 숫자를 입력해주세요."))
# min_num = a ; max_num = b
# if a > b:
#   min_num = b; max_num = a
# sum = 0
# for i in range(min_num,max_num+1):
#   sum += i
# print("합계 : ",sum)

# 2. min,max함수 사용
# a = int(input("첫번째 숫자를 입력해주세요."))
# b = int(input("두번째 숫자를 입력해주세요."))
# sum = 0
# for i in range(min(a,b),max(a,b)+1):
#   sum += i
# print("합계 : ",sum)

# sum = 0
# for i in range(1,100,2):
#   sum += i
# print("합계 : ",sum)
# sum = 0
# for i in range(1,100,2):
#   if i %2 !=0:
#     sum += i
# print("합계 : ",sum)

# # 1,100까지 숫자의 합
# sum = 0
# for i in range(1,101):
#   sum += i
# print("합계 : ",sum)

# for i in range(3):
#   print(f"{i} : 안녕하세요")

# for _ in range(3):
#   print("안녕하세요.")

# 1 - 1번출력, 2-2번출력, 3-3번출력
# for i in [1,2,3]:
#   for j in range(i):
#     print("안녕하세요.")
#   print("-"*10)

# for i in [1,2,3]:
#   print("안녕\n"*i,end="")
#   print("-"*30)

# for i in [1,2,3]:
#   print("안녕하세요")

# for i in range(5,0,-1):  # -1씩 감소
#   print("*"*i)

# *****
# ****
# ***
# **
# *

# for i in range(1,6):
#   print("*"*i)

# # for문을 사용해서
# for i in range(1,6):
#   for j in range(5):
#     print("*"*i)

# *
# **
# ***
# ****
# *****

#  range(시작값,끝값+1,증가값)
# for i in range(1,10,2): 
#   print(f"[ {i}단 ]")
#   for j in range(1,10):
#     print(f"{i}x{j}={i*j}")

# # 구구단 1,3,5,7,9단 출력하시오.
# for i in range(1,10):
#   if i%2 != 0:
#     print(f"[ {i}단 ]")
#     for j in range(1,10):
#       print(f"{i}x{j}={i*j}")

# # 구구단을 출력하시오.
# for i in range(2,9+1):
#   print(f"[ {i}단 ]")
#   for j in range(1,9+1):
#     print(f"{i}x{j}={i*j}")
#   print("-"*10)

# # 1,3,5,7,9 까지 출력하시오.
# for i in range(1,10,2):
#   print(i)
# for i in range(10):
#   if i%2 != 0:
#     print(i)

# 1,10까지 for문을 사용해서 출력하시오.
# for i in range(1,10+1):
#   print(i)