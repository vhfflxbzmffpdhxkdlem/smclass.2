# Student클래스 생성 후 
# 데이터를 직접 입력을 받아, 클래스 선언후 저장
# 번호 - 자동부여, 이름,국어,영어,수학,합계,평균,등수
# 클래스 전체 출력 
# 클래스 수정

# [ 학생성적 프로그램 ]
# 1. 학생성적입력
# 2. 학생성적출력
# 3. 학생성적수정


class Student():
  count = 1
  students = []

  @classmethod
  def stu_print(cls):
    print("-"*70)
    for s in cls.students:
      print(str(s))

  def __init__(self,name,kor,eng,math):
    self.no = Student.count
    self.name = name
    self.kor = kor
    self.eng = eng
    self.math = math
    self.total = kor+eng+math
    self.avg = (kor+eng+math)/3
    self.rank = 0
    Student.students.append(self)
    Student.count += 1

  def __str__(self):
    return f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg:.2f}\t{self.rank}"



### 프로그램 시작 ###
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수']


while True:
  print("[ 학생성적 프로그램 ]")
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적수정")
  print("0. 프로그램종료")
  choice = int(input("원하는 번호를 입력해주세요"))
  if choice == 1:
    print("[ 학생성력입력 ]")
    s1 = Student(name = input("이름을 입력해주세요"),kor = int(input("국어점수를 입력해주세요")),eng = int(input("영어점수를 입력해주세요")),math = int(input("수학점수를 입력해주세요")))
    
  elif choice == 2:
    print("[ 학생성적출력 ]")
    print(*s_title,sep='\t')
    Student.stu_print()

  elif choice == 3:
    print("[ 학생성적수정 ]")
    name = input("찾고자 하는 학생의 이름을 입력해주세요.")
    flag = 0
    for s in Student.students:
      if s.name == name:
        print(f"{name}학생을 찾았습니다.")
        print("1. 국어")
        print("2. 영어")
        print("3. 수학")
        print("0. 이전페이지")
        choice = int(input("수정을 원하는 과목을 선택해주세요."))
        if choice == 1:
          print(f"현재{s_title[choice+1]}성적은 {s[choice+1]}입니다.")
          s[choice+1] = int(input("수정할 점수를 입력해주세요."))
        elif choice == 2:
          print(f"현재{s_title[choice+1]}성적은 {s[choice+1]}입니다.")
          s[choice+1] = int(input("수정할 점수를 입력해주세요."))
        elif choice == 3:
          print(f"현재{s_title[choice+1]}성적은 {s[choice+1]}입니다.")
          s[choice+1] = int(input("수정할 점수를 입력해주세요."))
        elif choice == 0:
          break
      s[5] = s[2]+s[3]+s[4]
      s[6] = s[5]/3
      flag = 1
      break
    if flag == 0:
      print(f"{name}학생이 없습니다. 다시 검색해주세요.")
      

  elif choice == 0:
    print("프로그램을 종료합니다")
    break