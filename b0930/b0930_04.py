#변수 선언 
#boolVar : 논리형, intVar : 정수형, floatVar : 실수형, strVar : 문자형(문자열)

#input으로 입력을 받아
# 홍길동, 100 100 99, 합계, 평균은 소수정 둘째 자리 1줄에 출력하시오.
#format 사용, f함수
name = input("이름을 입력해주세요")
kor = input("국어점수를 입력해주세요")
eng = input("영어점수를 입력해주세요")
math = input("수학점수를 입력해주세요")
total = int(kor)+int(eng)+int(math) #문자열에서 정수형으로 타입 변경
avg = total/3
print("{},{},{},{},{},{:.2f}".format(name,kor,eng,math,total,avg))
print(f"{name},{kor},{eng},{math},{total},{avg:.2f}")
 
# name.kor,eng,math,total,avg 출력
#a = '100'
#b = "200"
#print(type(a))
#print(type(b))

#print(a+b) #문자연결 연산자 100200
#print(int(a)+(int(b)))# 타입을 변경
#name =  "홍길동"
#print(int(name)) #문자를 숫자로는 변경이 불가능함, 문자숫자는 가능
#c = "3.14"
#print(int(float(c))) # 실수형으로 변경후 정수형으로 변경
#print(int(c)) 문자실수형은 정수로 바로 변경은 불가
#print(str(c)) #실수형을 문자열로 변경

#d = "True"
#print(bool(d)) #문자불형을 불형으로 변경

#타입 변경 - str,float,int,bool



#name = "홍길동"
#print(type(name))

#leverl = '3레벨'
#print(type(leverl))

#n = 3.14
#print(type(n))

#num = 100
#print(type(num))

#a_bool = True #True,False 대문자로 넣어야함
#print(type(a_bool))





#var1 = 100
#var2 = var1
#var3 = var2
#var4 = var3
#print(var4)

#v4 = v3 = v2 = v1 = 10
#print(v4)