# 4 * 3 * 2 * 1

result = 1
for i in range(1,5):
  result *= i
print(result) 

# # 퀴즈
# a = [1,2,3,4,5]
# # a리스튿에 전부 10을 더해서 리스트에 담아 출력하시오.
# #리스트 내포, map 람다식 사용

# # 리스트 내포.
# # aArr =[ i+10 for i in a ]
# # print(aArr)


# # 람다식
# # map() - 리스트에 동일한 형태를 적용시킬때
# aArr = list(map(lambda x:x+10,a))
# print(aArr)


# def func(v1,v2):
#   return v1*v2

# lambda v1,v2:v1*v2


# 리스트 내포
# a = [1,2,3,4]
# b = [10,20,30,40]
# aArr = [i+j for i,j in zip(a,b)]
# print(aArr)
# a+b = [11,22,33,44]


# 함수구현

# # 기본함수 사용
# a = [1,2,3,4]
# b = [10,20,30,40]
# # aArr = []
# # def func(a,b):
# #   for i,j in zip(a,b):
# #     aArr.append(i+j)
# #   return aArr
# # print(func(a,b))

# aArr = []
# def func(a):
#   for i in a:
#     aArr.append(i*i)
#   return aArr
# print(func(a))
# # print(func(a,b))


#람다식 구현
# a = [1,2,3,4]
# b = [10,20,30,40]
# # map(lambda 매개변수1,매개변수2:리턴값,복합자료형1,복합자료형2)
# aArr = list(map(lambda i,j:i+j,a,b))
# print(aArr)


# zip함수 : 2개 리스트 1개로 변경
# a = [1,2,3,4]
# b = [10,20,30,40]
# print(list(zip(a,b)))
# print(dict(zip(a,b)))


# filter(함수,반복 가능한 라료형) - 리스트,튜플,딕셔너리

# aArr 값중에 2 의 배수인경우만 리턴
# def func(v):
#   if v%2 == 0:
#     return True 
#   else:
#     return False
# aArr = [1,2,3,4]
# bArr = list(filter(func,aArr))
# print(bArr)

# filter함수 사용, 람다식 사용
# 람다식 변경
# aArr = [1,2,3,4]
# bArr = list(filter(lambda x:x%2==0,aArr))
# print(bArr)


# 기본함수사용방법
# def func(v):
#   if v%2 == 0:
#     return v
  
# aArr = [1,2,3,4]
# bArr = []
# for i in aArr:
#   if func(i) !=None:
#     bArr.append(func(i))
# print(bArr)


# def func(v):
#   return v*2

# lambda v:v*2  # 람다는 두줄식이 안된다 한줄식만 가능하다

# # map함수 - 
# # map(함수,리스트) : 리스트의 내용을 1개씩 함수에 전달해서 결과값을 리스트로 저장
# aArr = [1,2,3,4]
# # bArr = list(map(func,aArr))
# # print(bArr)

# bArr = list(map(lambda x:x*2,aArr))


# 리스트 내포
# aArr = [1,2,3,4]
# print(aArr)
# bArr = [ a*2 for a in aArr]
# print(bArr)


# 기본적인 함수사용
# print(func(2))

# aArr = [1,2,3,4]
# bArr = []
# for a in aArr:
#   bArr.append(func(a))
# print(bArr)
