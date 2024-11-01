import oracledb

# 학생성적 프로그램
# 1. 학생성적 입력
# 2. 학생성적 출력
# 3. 학생성적 검색
# students테이블 사용해서
# 시퀀스 students_seq 생성
# 김유신,99,98,96,합계,평균,등수,입력일

def connects():
  user="ora_user"
  password = "1111"
  dsn = "localhost:1521/xe"
  try: conn = oracledb.connect(user=user,password=password,dsn=dsn)
  except Exception as e : print("예외처리 : ",e)
  return conn



print("[ 학생성적 프로그램 ]")
print("1. 학생성적 입력")
print("2. 학생성적 출력")
print("3. 학생성적 검색")
choice = input("원하는 번호를 입력하세요.")
if choice == '1':
  name = input("이름를 입력해주세요.")
  kor = int(input("국어성적를 입력해주세요."))
  eng = int(input("영어성적를 입력해주세요."))
  math = int(input("수학성적를 입력해주세요."))
  total = kor+eng+math
  avg = total/3
  rank = 0
  sdate = '20241101'

  conn = connects()
  cursor = conn.cursor()
  sql = "insert into students(students_seq.nextval,:name,:kor,:eng,:math,:total,:avg,:rnak,:sdate) values();"
  cursor.execute(sql,name=name,kor=kor,eng=eng,math=math,total=total,avg=avg,rank=rank,sdate=sdate)
  conn.commit()
  conn.close()
  print("학생성적이 입력되었습니다.")

elif choice == '2':
  conn = connects()
  cursor = conn.cursor()
  sql = "select * from students;"
  cursor.execute(sql)
  rows = cursor.fetchall()
  for row in rows:
    print(row)
    print()
  conn.close()
  print("학생성적이 출력되었습니다.")

elif choice =='3':
  name = input("찾고자 하는 학생의 이름을 검색해주세요")
  conn = connects()
  cursor = conn.cursor()
  sql = "select * from students where name=:name;"
  cursor.execute(sql,name=name)
  row = cursor.fetchone()
  print(f"{name}학생의 성적이 검색되었습니다.")
  print(row)
  conn.close()