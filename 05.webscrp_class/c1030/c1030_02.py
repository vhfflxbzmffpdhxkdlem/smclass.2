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

 # db 접속
conn = connects()
cursor =conn.cursor()

# 입력
user_id = input("아이디를 입력하세요.")   # eee
user_pw = input("패스워드를 입력하세요.") # 2222

# 데이터수정
sql = "update member set pw=:pw where id=:id"
cursor.execute(sql,id=user_id,pw=user_pw)
conn.commit()


print("파일이 수정되었습니다.")
cursor.close()



# a_list = [0,1,2,3,4,5,6,7,8,9]
# a = random.randrange(0,100000000) # 0-9999
# ran_num = f"{a:08}"
# # 랜덤 4자리 숫자
# print(ran_num)




