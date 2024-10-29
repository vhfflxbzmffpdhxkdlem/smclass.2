import oracledb
## sql developer 실행
conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')

## sql 창이 열림
cursor = conn.cursor()

# sql작성,실행
num1 = input("숫자를 입력하세요>>")

# no = 10,20,30 을 검색해서 출력하시오
# sql = f"select * from students where no=10 or no=20 or no=30"
# sql = f"select * from students where no in(10,20,30)"
# cursor.execute(sql)

# n_list = num1.split(",")
# sql = f"select * from students where no in(:1,:2,:3)"
# cursor.execute(sql,n_list)

# excute함수 : 변수 추가
# sql = f"select * from students where no >= :no"
# cursor.execute(sql,no=num)

# n_list = [num1,num2,num3]
# sql = f"select * from students where no in(:1,:2,:3)"
# cursor.execute(sql,n_list)


# 문자열함수 f 사용
# sql = f"select * from students where no in(no1,no2,no3)"
# cursor.execute(sql,no1 = num1,no2 = num2,no3 = num3)

# sql = f"select * from students where no in({num1},{num2},{num3})"
# cursor.execute(sql)

# 데이터 가져오기 - fetchone():1개 ,fetchmany(10):숫자만큼 ,fetcahll():모든것
rows = cursor.fetchall()
titles = ['번호','이름','국어','영어','수학','합계','평균','등수','등록일']
for idx,title in enumerate(titles):
  if idx == 1:
    print(f"{title:10s}",end="\t")
    continue
  print(title,end='\t')
print()
print("-"*80)

for row in rows:
  for i,r in enumerate(row):
    if i == 1:
      print(f"{r:8}",end="\t")
      continue
    if i == 6:
      print(f"{r:.2f}",end="\t")
      continue
    if i == 8:
      # strftime()함수 : 날짜포맷함수 %Y : 2024, %y ; 24
      print(r.strftime("%Y-%m-%d"),end="\t")
      continue
    print(r,end="\t")
  print()
# 종료
conn.close()












