  # 변수 3종류 : 
  # 지역변수 : 함수내에 선언된 변수,  함수가 종류가 되면 사라짐.
  # 인스턴스 변수 : 객체선언할때 만들어짐, 각각의 객체마다 변수가 생성됨.
  # - 참조변수명.변수면.
  # 클래스 변수 : 객체가 선언되지 않아도 만들어짐, 모든 객체가 공통으로 상용
  # - 클래스명.변수명

  # 객체선언 한 참조변수를 출력하면 -> 주소값이 출력됨.
  # - 참조변수를 출력해서 워하는 데이터를 출력하려면, __str__ 함수르 사용
  # - 리턴값 : 문자열이여야함

  # 함수 2종류
  # 인스턴스 함수 : 객체선언할때 만들어짐, 각각의 객체마다 함수가 생성됨.
  # - 참조변수명.함수명
  # 클래스 함수 : 객체사 선언되지 않아도 만들어짐, 모든객체가 공통으로 사용
  # - 클래스명.함수명
  # @classmethod  #클래스 함수표시


# 클래스 생성
class Student:
  # 1. 생성자 정의가 없음
  # 기본생선자
  count = 1  # 클래스 변수
  students = []

  @classmethod   # 클래스 함수 표시
  def stu_print(cls):
    for s in cls.students:
      print(str(s))


  def __init__(self,name,kor,eng,math):
    self.no = Student.count  # 클래스 변수 : 클래스명.변수명
    self.name = name         # 인스턴스 변수 : 참조변수명.변수명
    self.kor = kor
    self.eng = eng
    self.math = math
    Student.count += 1
    Student.students.append(self)

  def __str__(self):
    return f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}"   # 리턴값 : 문자열이여야함

  # no getter를 사용하지 않으면 접근 불가
  def get_no(self):
    return self.no
  def set_no(self,no):
    if no <0: raise "0이하는 입력할수 없습니다."
    self.no = no


s1 = Student("홍길동",100,100,99)
print(s1)
s2 = Student("유관순",100,90,90)
print(s2)
s3 = Student("강감찬",90,90,90)
print(s3)
s4 = Student("이순신",80,80,80)
print(s4)
s5 = Student("김구",70,70,70)
print(s5)

print("-"*50)
# 클래스__str__
Student.stu_print()
# Student.students




















# class Student:

#   def __init__(self,name,kor,eng,math):
#     self.no = 0
#     self.name = name
#     self.kor = kor
#     self.eng = eng
#     self.math = math
#     self.total = kor+eng+math
#     self.avg = (kor+eng+math)/3
#     self.rank = 0

#   def __str__(self):
#     return("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}".format(self.no,self.name,self.kor,self.eng,self.math,self.total,self.avg,self.rnak))

# # 1. 학생성적입력
# # 이름, 국어, 영어, 수학 -> 번호,국어,영어,수학,합계,평균,등수
# # 클래스 1개가 생성이 되고
# # 클래스이 참조변수(__str__) 출력을 해보세요.



# #### 프로그램 시작 #####

# s_title = ['번호','이름','국어','영어','수학','합계','평균','등수']
# s_t = ['no','name','kor','eng','math','total','avg','rank']

# # 학생성적입력
# print("[ 학생성적출력 ]")
# s1 = Student("홍길동",100,100,99)
# print(*s_title,sep='\t')
# print("-"*70)
# Student.stu_print()  # 클래스함수 호출

#   # 클래스 함수
#   # @classmethod # 클래스 함수 표시
#   # def stu_print(cls):
#   #   print("-"*70)
#   #   for s in cls.students:
#   #     print(str(s))