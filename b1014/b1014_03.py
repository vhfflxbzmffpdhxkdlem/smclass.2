# 두수를 입력받아 더하기를 출력하시오.
def plus(n1,n2):
  return n1+n2

num1 = int(input("숫자를 입력하세요"))
num2 = int(input("숫자를 입력하세요"))
print(plus(num1,num2))




# def plus(n1,n2):
#   result = n1+n2
#   return result

# # def plus(n1,n2):
# #   return n1+n2

# print(plus(1,2))
# print(plus(55,45))
# print(plus(50,50))

# # 2-50까지 3-7까지 5-50까지 사이의 값을 모두 더해서 출력하시오.
# def num_sum(st,end):
#   sum = 0
#   for i in range(st,end+1):
#     sum += i
#   return sum

# total = num_sum(2,50)+num_sum(3,7)+num_sum(5,50)
# print("2-50까지의 합 : ",num_sum(2,50))
# print("2-50까지의 합 : ",num_sum(3,7))
# print("2-50까지의 합 : ",num_sum(5,50))
# print("합계 : ",total)
# print(f"천단위 표시 {num_sum(2,50):,d}")

# def num_sum(st,end):
#   sum = 0
#   for i in range(st,end):
#     sum += i
#   return sum

# total = 0
# num_sum(1,10)
# num_sum(1,100)
# total = num_sum(1,10)+num_sum(1,100)
# # 1,10까지의 합과 1,1000까지의 합의 총합을 출력하시오.
# print("합계 : ",total)
# print("프로그램 종료")

# def num_sum(st,end):  # (매개변수, 매개변수)
#   sum = 0 # 지역변수
#   for i in range(st,end+1):
#     sum = sum + i
#   print("합계 : ",sum)

# # 두수를 입력받아, 그 사이의 숫자 합을 구하시오.
# # num1, num2
# # 함수를 사용해서 출력하시오.

# num1 = int(input("원하는 숫자를 입력하세요."))
# #num2 = int(input("원하는 숫자를 입력하세요."))
# num_sum(num1,int(input("원하는 숫자를 입력하세요.")))

# # 1-10까지 합계를 출력하세오.
# num_sum(1,11)

# # 1-100까지 합계를 출력하세오.
# num_sum(1,101)
# # 2-50까지 합계를 출력하세오.
# num_sum(2,51)
# # 100-1000까지 합계를 출력하세오.
# num_sum(100,1001)
