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


url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    'Accept-Language':'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료
soup = BeautifulSoup(res.text,"lxml")


data = soup.select_one("#wrap > div.rankingnews._popularWelBase._persist > div.rankingnews_box_wrap._popularRanking > div")
sells = data.select(".rankingnews_box")
with open('c1025/news.txt','w',encoding='utf-8')as f:
  for i,sell in enumerate(sells):
    # 뉴스사
    news = sell.select_one("a > strong").text
    f.write(f"[ {i+1} ]. 언론사 : {news}\n")
    # 뉴스제목
    nw1 = sell.select_one("ul > li:nth-child(1) > div > a").text
    nw2 = sell.select_one("ul > li:nth-child(2) > div > a").text
    nw3 = sell.select_one("ul > li:nth-child(3) > div > a").text
    nw4 = sell.select_one("ul > li:nth-child(4) > div > a").text
    nw5 = sell.select_one("ul > li:nth-child(5) > div > a").text
    f.write(f"{i+1} : {nw1}\n")
    f.write(f"{i+1} : {nw2}\n")
    f.write(f"{i+1} : {nw3}\n")
    f.write(f"{i+1} : {nw4}\n")
    f.write(f"{i+1} : {nw5}\n")


smtpName = "smtp.naver.com"
smtpPort = 587

sendEmail = "aaa"
pw = "1111"
recvEmail = 'aaa'


title = "제목 : 파이썬 이메일보내기 안애"
content = "파일을 첨부합니다."
# with open("c1025/news.txt",'r',encoding='utf-8')as f:

msg = MIMEMultipart()
msg['"Subject'] = title
msg['From'] = sendEmail
msg['To'] = recvEmail
msg.attach(MIMEText(content))

# 파일첨부
with open("c1025/news.txt",'rb')as f:
  attachment = MIMEApplication(f.read()) # 파일첨부
  attachment.add_header('Content-Disposition','attachment',filename = "news.txt")
  msg.attach(attachment)

s = smtplib.SMTP(smtpName,smtpPort)
s.starttls() # 보안인증
s.login(sendEmail,pw)
s.sendmail(sendEmail,recvEmail,msg.as_string())
print("msg :")
print(msg.as_string())
s.quit()

print("메일이 발송되었습니다.!")