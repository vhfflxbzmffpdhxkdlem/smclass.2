import oracledb

# db 연결 함수선언
def connections():
  try:
    conn = oracledb.connect(user='ora_user',password='1111',dsn = 'localhost:1521/xe')
    print("db연결 : ",conn.version)
  except Exception as e : print("예외발생 : ",e)
  return conn

# 함수호출
conn = connections()
cursor = conn.cursor()
# 범위를 입력받아서 그 사이의 사원을 출력하시오.
# number = input("월급의 범위를 입력하세요")
# number = number.split(",")
# sql = "select employee_id,emp_name,salary from employees where salary >= :number and salary <= :number"
# cursor.execute(sql,[number])

num1 = input("범위1 입력")
num2 = input("범위2 입력")
sql = "select employee_id,emp_name,salary from employees where salary >= :num1 and salary <= :num2"
cursor.execute(sql,num1=num1,num2=num2)

# 월급이 4000~8000 사이의 사원을 모두 출력하시오.
# sql = "select employee_id,emp_name,salary from employees where salary >= 4000 and salary<=8000"
# cursor.execute(sql)




# 입력한 값을 가지고 이름이 포함되어 있는 데이터를 출력하시오.
# search = input("이름을 입력하세요.>>")
# search = '%'+search+'%'
# sql = "select * from employees where emp_name like :search"
# cursor.execute(sql,search=search)

# search = input("번호 검색 >>")
# sql = "select * from employees where emp_name like '%:search%'"
# 키워드
# sql = "select * from employees where employee_id>=:search"
# cursor.execute(sql,search=search)

# 번호순서
# sql = "select * from employees where employee_id>=:1"
# cursor.execute(sql,[search])


title = ['employee_id','emp_name','salary']
a_list = [] # dict타입으로 변경해서 저장하시오.
rows = cursor.fetchall()

for row in rows:
  a_list.append(dict(zip(title,row)))
  print(row)
print(a_list)


# 검색한
# search = input("검색할 이름을 입력하세요")


# employees테이블. emp_name a 가 포함되어있는 row모두 출력하시오.
# sql = "select * from employees where emp_name like ('%:search%')"
# cursor.execute(sql,search=search)

# sql = "select * from employees where emp_name like ('%:1%')"
# cursor.execute(sql,search)

# rows = cursor.fetchall()

# for row in rows:
#   for r in row:
#     print(r,end="\t")
#   print()

cursor.close()



# employees 테이블에서 이름이 a가 포함되어 있는 이름, 모든 컬럼 출력