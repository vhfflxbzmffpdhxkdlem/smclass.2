import oracledb
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from bs4 import BeautifulSoup
import random
import csv
# email 발송관련
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication




def connects():
  user = "ora_user"
  password = "1111"
  dsn = "localhost:1521/xe"
  try:
    conn = oracledb.connect(user=user,password=password,dsn=dsn)
  except Exception as e : print("예외발생",e)
  return conn

while True:
  print("[ 커뮤니티 ]")
  print("1. 로그인")
  print("2. 비밀번호 찾기")
  print("3. 회원가입")
  print("0. 프로그램 종료")
  print("-"*30)
  choice = input("원하는 번호를 입력하세요.>>")
  if choice == '1':
    user_id = input("아이디를 입력하세요.")
    user_pw = input("패스워드를 입력하세요.")

    # db 접속
    conn = connects()
    cursor =conn.cursor()
    sql = "select * from member where id=:id and pw=:pw"
    cursor.execute(sql,id=user_id,pw=user_pw)
    row = cursor.fetchone()  # None
    print(row)
    if row != None:
      print(f"로그인 성공! {row[2]}님 환영합니다.")
    else:
      print("아이디 또는 패스워드가 일치하지 않습니다. 정확히 입력하세요!!")

    cursor.close()

    # 오라클 db에 접속해서 member테이블에서 검색 가져옴.
    
    # if user_id =='aaa' and user_pw =="1111": print("로그인 성공")
    # else: 
      # print("로그인 실패")
      # continue
    
    
    print("[ 학생성적 프로그램에 접속합니다. ]")
    
    ## 프로그램 구현 ##

  elif choice == '2':
    print("[ 비밀번호 찾기 ]")
    search = input("해당 아이디를 입력하세요.")
    # 아이디가 있는지 확인
    conn = connects()
    cursor = conn.cursor()
    sql = "select * from member where id=:id"
    cursor.execute(sql,id=search)
    row = cursor.fetchone()
    print(row)
    cursor.close()
    if row != None:
      print("아이디가 존재합니다. 임시 패스워드를 발급합니다.")

      # 임시 비밀번호 생성
      a = random.randrange(0,10000)
      ran_num = f"{a:4}"

      # 임시 패스워드 이메일로 발송
      smtpName = "smtp.naver.com"
      smtpPort = 587

      sendEmail: "aaa@naver.com"
      pw = "1111"
      recvEmail = "aaa@naver.com"

      title = "제목 : 오라클 임시비밀번호 발송"
      content = ran_num

      msg = MIMEText(content)
      msg['Subject'] = title
      msg['From'] = sendEmail
      msg['To'] = recvEmail
      print("msg 데이터 :",msg.as_string())

      s = smtplib.SMTP(smtpName,smtpPort)
      s.starttls()
      s.login(sendEmail,pw)
      s.sendmail(sendEmail,recvEmail,msg.as_string())
      s.quit()

      print("메일이 발송되었습니다.")

      # 임시 비밀번호로 변경
      conn = connects()
      cursor = conn.cursor()

      user_id = search
      user_pw = ran_num

      sql = "update member set pw=:pw where id=:id"
      cursor.execute(sql,id=user_id,pw=user_pw)
      conn.commit()

      cursor.close()

      # 1. 임시비빌번호를 생성해서 
      # 2. 이메일로 보냅니다.
      # 3. 아이디에 비밀번호를 임시비밀번호를 수정합니다.
      # 4. 임시번호로 로그인을 했을 경우 로그인 성공이 나타나도록 하시오.
    else:
      print("아이디가 존재하지 않습니다. 다시 입력해주세요.")

  elif choice == '3':
    pass
  elif choice == '0':
    print("프로그램을 종료합니다.")
    break
