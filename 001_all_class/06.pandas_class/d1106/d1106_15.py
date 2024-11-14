from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pyautogui
import time
import requests
from bs4 import BeautifulSoup
import random
import csv

# # 파일 저장하기
# browser = webdriver.Chrome()
# browser.maximize_window()
# for i in range(1,4):
#   url = f"https://search.daum.net/search?w=tot&q=202{i}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
#   browser.get(url)
#   time.sleep(1)

#   soup = BeautifulSoup(browser.page_source,"lxml")
#   with open(f'd1106/daum_movie{i}.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())
#   f.close()
#   time.sleep(2)

#   f.close()

#   input("enter키 입력완료")

# 파일 저장
f = open('d1106/daum_movie.csv','a',encoding='utf-8-sig',newline="")
writer = csv.writer(f)
for i in range(1,4):
  with open(f'd1106/daum_movie{i}.html','r',encoding='utf-8') as f:
    soup = BeautifulSoup(f,"lxml")

  # 기준점
  data = soup.select_one("#mor_history_id_0 > div > div.flipsnap_view > div > div:nth-child(1) > c-flicking-item > c-layout > div > c-list-doc")
  sells = data.select("div.c-item-content")

  for i,sell in enumerate(sells):
    print(f"{i+1}")
    try:
      # 0. 이미지
      # 1. 제목
      title = sell.select_one("div.item-title > c-title > strong > a").text.strip()
      print(f"제목 : {title}")
      # 2. 관객수
      count = int(sell.select_one("div.item-contents > c-contents-desc > p > a").text.strip()[3:-2].replace(",",""))
      print(f"관객수 : {count*10000}")
      # 3. 날짜
      date = sell.select_one("div.item-contents > c-contents-desc-sub > span").text.strip()
      print(f"개봉일 : {date}")
    except Exception as e : print("예외처리",e)
f.close()











