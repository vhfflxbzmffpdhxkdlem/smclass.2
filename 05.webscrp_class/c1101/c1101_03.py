import oracledb

# 학생성적 프로그램
# 1. 학생성적 입력
# 2. 학생성적 출력
# 3. 학생성적 검색
# students테이블 사용해서
# 시퀀스 students_seq 생성
# 김유신,99,98,96,합계,평균,등수,입력일

s_title = ['번호','이름','국어','영어','수학','합계','평균','등수','등록일']
# db 연결함수
def connects():
  user="ora_user"
  password = "1111"
  dsn = "localhost:1521/xe"
  try: conn = oracledb.connect(user=user,password=password,dsn=dsn)
  except Exception as e : print("예외처리 : ",e)
  return conn


while True:
  print("[ 학생성적 프로그램 ]")
  print("1. 학생성적 입력")
  print("2. 학생성적 출력")
  print("3. 학생성적 검색")
  print("4. 학생성적 정렬")  # 이름순차정렬,이름역순정렬,합계순차정렬,합계역순정렬
  print("5. 등수처리")
  print("0. 프로그램 종료")
  choice = input("원하는 번호를 입력하세요.")
  if choice == '1':
    conn = connects()
    cursor = conn.cursor()
    print("[ 학생성적 입력 ]")
    name = input("이름를 입력해주세요.")
    kor = int(input("국어성적를 입력해주세요."))
    eng = int(input("영어성적를 입력해주세요."))
    math = int(input("수학성적를 입력해주세요."))
    total = kor+eng+math
    avg = total/3
    # list
    s_list = [name,kor,eng,math,total,avg]
    sql = "insert into students values(students_seq.nextval,:1,:2,:3,:4,:5,:6,0,sysdate)"
    # insert,update,delete 경우 conn.commit() 하셔야 반영됨.
    # sql = "insert into students values(students_seq.nextval,:name,:kor,:eng,:math,:kor+:eng+:math,(:kor+:eng+:math)/3,0,sysdate)"
    cursor.execute(sql,s_list)
    conn.commit()
    conn.close()
    print("학생성적이 입력되었습니다.")
    print()

  elif choice == '2':
    print("[ 학생성적 출력 ]")
    for s in s_title :
      print(s,end="\t")
    print()
    print("-"*80)
    # db 연결
    conn = connects()
    cursor = conn.cursor()
    sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'YYYY/mm/dd') from students"
    cursor.execute(sql)
    rows = cursor.fetchall()
    print("개수 : ",len(rows))
    if len(rows)<1:
      print("데이터가 없습니다.")
      break
    for row in rows:
      for r in row:
        print(r,end="\t")
      print()
    print()
    print("데이터 출력완료")
    conn.close()
    print("학생성적이 출력되었습니다.")

  elif choice =='3':
    print("[ 학생성적 검색 ]") # a포함괴어 있는 학생을 검색
    print("1. 이름으로 검색")
    print("2. 합계순 검색")
    choice = input("원하는 번호를 입력하세요.")
    if choice == '1':
      print("[ 이름으로 검색 ]")
      search = input("찾고자 하는 이름을 입력하세요.")
      search = '%'+search+'%'
      sql = f"select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'YYYY/mm/dd') from students where name like :search"


      ### 출력부분 ###

      # db 연결
      conn = connects()
      cursor = conn.cursor()
      cursor.execute(sql,search=search)
      rows = cursor.fetchall()
      print(f"개수 : {len(rows)}")
      for s in s_title :
        print(s,end="\t")
      print()
      print("-"*80)
      if len(rows)<1:
        print("데이터가 없습니다.")
        break
      for row in rows:
        for r in row:
          print(r,end="\t")
        print()
      print()
      print("데이터 출력완료")
      conn.close()
      print("학생성적이 출력되었습니다.")

  elif choice =='4':
    print("[ 학생성적 정렬 ]")
    print("1. 이름 순차정렬")
    print("2. 이름 순차역렬")
    print("3. 성적 순차정렬")
    print("4. 성적 역순정렬")
    choice = input("원하는 번호를 입력하세요.")

    if choice =='1':
      sql = "select  no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'YYYY/mm/dd') from students order by name"
    elif choice =='2':
      sql = "select  no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'YYYY/mm/dd') from students order by name desc"
    elif choice =='3':
      sql = "select  no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'YYYY/mm/dd') from students order by total"
    elif choice =='4':
      sql = "select  no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'YYYY/mm/dd') from students order by total desc"

    # db 연결
    conn = connects()
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    print(f"개수 : {len(rows)}")
    for s in s_title :
      print(s,end="\t")
    print()
    print("-"*80)
    if len(rows)<1:
      print("데이터가 없습니다.")
      break
    for row in rows:
      for r in row:
        print(r,end="\t")
      print()
    print()
    print("데이터 출력완료")
    conn.close()
    print("학생성적이 출력되었습니다.")

  elif choice == '5':
    print("[ 등수처리 ]")
    # db 연결
    conn = connects()
    cursor = conn.cursor()
    sql = "update students a set rank = (select ranks from (select no,rank()over(order by total) ranks from students) b where a.no=b.no)"
    cursor.execute(sql)
    conn.commit()
    print("등수처리가 완료되었습니다.")


    sql = "select  no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'YYYY/mm/dd') from students"
    cursor.execute(sql)
    rows = cursor.fetchall()
    print(f"개수 : {len(rows)}")
    for s in s_title :
      print(s,end="\t")
    print()
    print("-"*80)
    if len(rows)<1:
      print("데이터가 없습니다.")
      break
    for row in rows:
      for r in row:
        print(r,end="\t")
      print()
    print()
    print("데이터 출력완료")
    conn.close()
    print("학생성적이 출력되었습니다.")
  
  elif choice =='0':
    print("프로그램 종료")
    break
