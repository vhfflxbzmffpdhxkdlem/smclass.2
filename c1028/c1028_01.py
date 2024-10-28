import oracledb

# oracle 연결 - sql developer연결
conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
# 연결확인
print(conn.version)

# sql 실행창 오픈
# 1개 검색된 데이터 호출
# cursor = conn.cursor()
# sql = "select count(*) from member"
# cursor.execute(sql)
# count1 = cursor.fetchone()
# print("개수 : ",count1)


# 여러개 검색된 데이터 내용 호출
cursor = conn.cursor()
sql = "select * from member"
cursor.execute(sql)
rows = cursor.fetchall()

# for row in rows:
#   print(row)

for i in range(len(rows)):
  print(f"{i+1}\t{rows[i][0]:10}\t{rows[i][1]}\t{rows[i][2]:8}\t{rows[i][3]:33}\t{rows[i][4]}\t{rows[i][5]}\t{rows[i][6]}\t{rows[i][7]}")


conn.close()





