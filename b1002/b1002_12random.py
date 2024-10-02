import random

# 램덤숫자 생성 - random
# random() : 0<= x < 1 실수값 추출
print(random.random())
# 0-9
print(int(random.random()*10))
#1-10
print(int(random.random()*10)+1)

#램던 int 추출 - 1-10까지 
print(random.randint(1,10))

# 램덤 범위 추출 - 1-10사이(10포함 안됨)
print(random.randrange(1,10))

# 리스트에서 램덤 추출
a = [1,4,5,9]
print(random.choice(a))

#리스트에서 여러개 랜덤 추출 (중복가능)
print(random.choices(a,k=2))

#리스트에서 여러개 랜덤 추출 (중복불가)
print(random.sample(a,2))
# 