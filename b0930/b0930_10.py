

a = [1,2,3,4,5] 
# 얕은 복사 - 주소값만 복사됨.
b = a    
print(a)#[1,2,3,4,5]
b[0] = 100
print(a)#[100,2,3,4,5]

### 데이터 값이 1개일때 ###
#num = 10  # num메모리주소값
#num2 = num # num2메모리주소값이 다름
#num2 = 20   #num2를 변경해도 num의 값은 변경이 안됨.
#print(num)
#print(num2)

#a = [1,2,3,4,5]
#b = a

#print(a)
#print(b)