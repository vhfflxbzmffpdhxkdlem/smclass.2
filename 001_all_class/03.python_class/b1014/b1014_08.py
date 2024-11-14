
# 전역변수인 경우 함수내에서도 사용이 가능하고
# 함수 외부에서도 사용이 가능함.
# 지역변수는 return 없이는 값이 함수 밖으로 나오지 못함.

# def calc():
#   global sum   # 전역변수인 경우, 함수에서 변경시 외부에서도 같이 변경이 됨.
#   sum = 200

# sum = 10
# calc()   # 함수에서 sum을 200으로 변경이 됨.
# print(sum)  # 결과값은 sum이 200됨

# 매개변수가 일반변수 일경우, return 하지 않으면 변수값이 변동이 없음.
# hh = 100

# def add(hh):
#   hh = hh+100
#   return hh
# add(hh)
# print(hh)

# ---------------------------

# 복합변수 - 리스트, 딕셔너리
# hong = [1,2,3,4,5]

# # 매개변수가 복합변수일 경우, return 없이도 값이 변경이 되어 전달됨.
# def add(h):
#   for i in range(len(h)):
#     h[i]-h[i]+100

# add(hong)
# print(hong)

# kim = []
# kim = hong # 얕은복사
# kim[0] = 100

# print(hong)


# def calc(n1,n2):
#   s1 = n1+n2
#   s2 = n1-n2
#   s3 = n1*n2 
#   s4 = n1/n2
#   s5 = [s1,s2,s3,s4]
#   return s5
# s1,s2,s3,s4 = calc(10,5)
# s2 = calc(10,5)
# # print(s1)
# # print(s2)
# # print(s3,s4)
# print("프로그램 종료")



# # 함수 내에 선언된 변수는 외부에서 사용할수 없음.
# def calc(v1,v2):
#   global sum    # 전역변수
#   # sum = 0     # 지역변수
#   for i in range(v1,v2+1):
#     sum += i
#   return sum

# sum = 100  # 외부의변수를 사용해서 계산을 하고 싶은 경우
# sum = calc(1,10)
# print(sum)


# print(1,2,3,4,5,6,7,8,9,sep=",",end="\t")  # 가변매개변수
# print("안녕")

# 키워드 매개변수
# def calc(n1 = 10,n2 = 20):
#   print(n1)
#   print(n2)

# calc()   # 매개변수가 없으면 기본값으로 출력 됨.
# calc(20) # n1 = 20,20  # 키가 없으면 무조건 1번째로 전달이 됨.
# calc(300)  # 키가 없으면 무조건 1번째로 전달이 됨.
# calc(n2 = 100) # 키가 있으면 키값으로 전달이 됨.

# 기본 매개변수 - 매개변수의 개수가 동일
# def calc(n1,n2):
#   print(n1,n2)

# calc(1,2)

# def calc(*n): # 가변매개변수
#   print(n)
#   print(len(n))
# calc(1,2,3,4,5,6,7)

# numStr = input("숫자를 입력하세요.(12,5)")
# numStr = input("숫자를 입력하세요.(12,5)")

# def nunum(num,num2):
#   print(f"두수 더하기 : {num+num2}")
#   print(f"두수 빼기 : {num-num2}")
#   print(f"두수 곱하기 : {num*num2}")
#   print(f"두수 나누기 : {num/num2}")


# # 문자열, 숫자로 변경 num,num2

# numStr2 = numStr.split(",")  # 문자열 타입
# num = int(numStr2[0])        # 문자열차입 -> 숫자형
# num2 = int(numStr2[1])

# nunum(num,num2)

# 3개의 숫자를 입력받아 숫자를 계산하시오.

# def calc(num,num2):

# def calc(numStr2):
#   s1 = 0
#   s2 = 0
#   s3 = 1
#   s4 = 1
#   for i in range(len(numStr2)):
#     s1 += numStr2[i]
#     s2 -= numStr2[i]
#     s3 *= numStr2[i]
#     s4 /= numStr2[i]
#   print(f"두수 더하기 : {s1}")
#   print(f"두수 빼기 : {s2}")
#   print(f"두수 곱하기 : {s3}")
#   print(f"두수 나누기 : {s4}")


# numStr1 = input("숫자를 3개 입력해 주세요.(12,5,3)")
# numStr2 = numStr1.split(",")
# numStr3 = [int(i) for i in numStr2 ]
# print(numStr2)
# calc(numStr2)

# 함수사용
# num = [10,20,30]
# num2 = [5,7,3]
# def nunum():
#   for i in range(len(num)):
#     print(f"두수 더하기 : {num[i]+num2[i]}")
#     print(f"두수 빼기 : {num[i]-num2[i]}")
#     print(f"두수 곱하기 : {num[i]*num2[i]}")
#     print(f"두수 나누기 : {num[i]/num2[i]}")
#     print("-"*50)
# nunum()
# def nunum(num,num2):
#   print(f"두수 더하기 : {num+num2}")
#   print(f"두수 빼기 : {num-num2}")
#   print(f"두수 곱하기 : {num*num2}")
#   print(f"두수 나누기 : {num/num2}") 

# for i in range(len(num)):
#   nunum(num[i],num2[2])


# for문을 활용한 계산
# num = [10,20,30]
# num2 = [5,7,3]
# for i in range(len(num)):
#   print(f"두수 더하기 : {num[i]+num2[i]}")
#   print(f"두수 빼기 : {num[i]-num2[i]}")
#   print(f"두수 곱하기 : {num[i]*num2[i]}")
#   print(f"두수 나누기 : {num[i]/num2[i]}")


