### list 추가방법 : append - 제일뒤에 추가, insert - 원하는 위치에 추가
a_list = [1,2,3]
print(a_list)
a_list.append(4) 
print(a_list)
a_list.append(10)
print(a_list)
a_list.insert(4,5)
print(a_list)
a_list.insert(3,20)
print(a_list)

### 삭제 del - index위치에 데이터 삭제, remove - 데이터값으로 삭제
del a_list[3]
print(a_list)
a_list.remove(4)
print(a_list)
a_list.remove(10)
print(a_list)

stu = [1,'홍길동',100,100,100,99]
#합계,평균 추가
a = stu[2]+stu[3]+stu[4]+stu[5]
b = (stu[2]+stu[3]+stu[4]+stu[5])/4
stu.append(a)
stu.append(b)

print(stu)