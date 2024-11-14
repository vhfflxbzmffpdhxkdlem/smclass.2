
stu_data = ['홍길동',100,100,100,99]
stu_datas = [[1,'유관순',100,100,100,99], [2,'이순신',100,99,98,99],[3,'김구',80,100,90,99]]
stu_title = ['번호','이름','국어','영어','수학','과학','합계','평균']
#for s in stu_data:
#  print(s)

#학생데이터에서 합계, 평군을 추가해서 1줄로 출력하시오
print("                     [학생성적 프로그램]")
#print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(stu_title[0],stu_title[1],stu_title[2],stu_title[3],stu_title[4],stu_title[5],stu_title[6],stu_title[7]))
#print("-"*60)
for s_t in stu_title:
  print("{}".format(s_t),end='\t')
print()
print("-"*60)


for s in stu_datas:
  print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(s[0],s[1],s[2],s[3],s[4],s[5],s[2]+s[3]+s[4]+s[5],(s[2]+s[3]+s[4]+s[5])/4))
## 학번, 이름, 국어, 영어, 수학, 과학, 합계, 평균  


#이순신의 평균을 출력하시오.
#print("이순신의 평균 : {}".format(float((stu_datas[1][1])+(stu_datas[1][2])+(stu_datas[1][3])+(stu_datas[1][4]))/4))

#학생이름 : 홍길동
#국어 : 100
#영어 : 100
#수학 : 100
#과학 : 99
#합계 : 
#평균 : 

#print("학생이름 : ",stu_data[0])
#print("학생이름 : {}".format(stu_data[0]))
#print("국어 : ",stu_data[1])
#print("국어 : {}".format(stu_data[1]))
#print("영어 : ",stu_data[2])
#print("영어 : {}".format(stu_data[2]))
#print("수학 : ",stu_data[3])
#print("수학 : {}".format(stu_data[3]))
#print("과학 : ",stu_data[4])
#print("과학 : {}".format(stu_data[4]))
#print("합계 : ",float(stu_data[1])+float(stu_data[2])+float(stu_data[3])+float(stu_data[4]))
#print("합계 : {}".format(float(stu_data[1])+float(stu_data[2])+float(stu_data[3])+float(stu_data[4])))
#print("평균 : ",(float(stu_data[1])+float(stu_data[2])+float(stu_data[3])+float(stu_data[4]))/4)
#print("평균 : {}".format((float(stu_data[1])+float(stu_data[2])+float(stu_data[3])+float(stu_data[4]))/4))

# 길이를 입력받아 삼각형의 넓이와 직사각형의 넓이를 구하시오
#num1 = float(input("첫번째 길이를 입력하여 주세요"))
#num2 = float(input("두번째 길이를 입력하여 주세요"))
#tr = num1*num2/2
#sc = num1*num2
#print(tr)
#rint(sc)

#length = input("2개의 길이를 입력하세요.")
#print(length.split(" "))

#l_list = length.split(" ")

#print("삼각형 넓이 : {}".format(float(l_list[0])*float(l_list[1])*0.5))
#print("사각형 넓이 : {}".format(float(l_list[0])*float(l_list[1])))

# 원의 넓이 : 반지름 * 반지름 *3.14
#반지름을 입력받아, 원의 넣ㅂ이를 구하시오.
#num1 = float(input("반지름을 입력해주세요."))
#rol = num1**2*3.14
#print("원의넓이 : ",rol)
#print("원의넓이 : {:.2f}".format(rol))



### 복합대입연산자 +-, -=, *=, /=, //=, %=, **=
#a = 10
#a += 5;print(a)
#a -= 5;print(a)
#a *= 5;print(a)
#a /= 5;print(a)
#a //= 5;print(a)
#a **= 5;print(a)
#a %= 5;print(a)

### 숫자를 문자열로 변환 ###
#문자열 + 숫자 : 불가능
#a = 100
#b = 10
#print(str(a)+str(b))

### 문자형숫자 변환 ###
#a = "100"
#b = "10.5"
#c = "안녕"
#print(float(a)) #정수형 문자열->정수타입,실수타입 변경가능
#print(int(b)) # 실수형 문자열->실수타입 변경가능
#print(fleat(c)) # 글자는 숫자형 타입으로 변경불가

#여러줄을 1출 형태로 표현
#1줄 선언 방식
#a = 10 ; b = 5

#1줄 선언 방식
#s1,s2,s3 = 1,2,3

#x = 1,2,3,4,5,6,7,8,9,10
#1
#x = 11,12,13,...,20
#11
#x = 21,22,23,...,30
#21

#특정숫자 a = 0,1,2,3,4,5
#1,3,5,7,9
#2x+1

### 우선순위 ###
#print(2+2-2*2/2*2)
#print(2+2-(((2*2)/2)*2))

### 사칙연산+,-,*,/  , 추가적 연산%,**,//  ###
#a = 5; b = 3 1출형태 표현식 ; 넣어주면 됨. 
# /,%,//,**
#print(a/b)
#print(a%b)
#print(a//b)
#print(a**b)
#print(f"{},{},{},{}"(a/b,a%b,a//b,a**b))
