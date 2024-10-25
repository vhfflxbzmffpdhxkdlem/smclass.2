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

# 제목,금액,평점,평가수,찜 정보를 1-5페이지 까지 가져와서
# 평점 4.8이상,평가수 1000명이상 인 상품을 csv파일로 저장하고 출력하시오.

# 네이버 쇼핑 검색창 입력  enter키 입력 
# 네이버 쇼핑 클릭
# 네이버 쇼핑에서 무선마우스 검색창 입력 enter키 입력

# url1 = "https://www.naver.com"
# borwser1 = webdriver.Chrome()
# borwser1.maximize_window()
# borwser1.get(url1)
# time.sleep(1)
# borwser1.find_element(By.XPATH,'//*[@id="query"]').click()
# time.sleep(1)
# borwser1.find_element(By.XPATH,'//*[@id="query"]').send_keys("네이버쇼핑")
# time.sleep(1)
# borwser1.find_element(By.XPATH,'//*[@id="query"]').send_keys(Keys.ENTER)
# time.sleep(1)
# borwser1.find_element(By.XPATH,'//*[@id="main_pack"]/section[1]/div/div/div[1]/div/div[2]/a').click()
# time.sleep(2)
# # 새로운 탭으로 이동
# borwser1.switch_to.window(borwser1.window_handles[1])
# time.sleep(1)
# borwser1.find_element(By.XPATH,'//*[@id="gnb-gnb"]/div[2]/div/div[2]/div/div[2]/form/div[1]/div/input').click()
# time.sleep(1)
# borwser1.find_element(By.XPATH,'//*[@id="gnb-gnb"]/div[2]/div/div[2]/div/div[2]/form/div[1]/div/input').send_keys("무선마우스")
# time.sleep(1)
# borwser1.find_element(By.XPATH,'//*[@id="gnb-gnb"]/div[2]/div/div[2]/div/div[2]/form/div[1]/div/input').send_keys(Keys.ENTER)
# time.sleep(1)



browser = webdriver.Chrome()
browser.maximize_window()
for i in range(5):
  url = f'https://search.shopping.naver.com/search/all?adQuery=%EB%AC%B4%EC%84%A0%20%EB%A7%88%EC%9A%B0%EC%8A%A4&origQuery=%EB%AC%B4%EC%84%A0%20%EB%A7%88%EC%9A%B0%EC%8A%A4&pagingIndex={i+1}&pagingSize=40&productSet=total&query=%EB%AC%B4%EC%84%A0%20%EB%A7%88%EC%9A%B0%EC%8A%A4&sort=rel&timestamp=&viewType=list'
  browser.get(url)
  time.sleep(2)
  prev_height = browser.execute_script("return document.body.scrollHeight")
  while True:
      browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
      time.sleep(1)
      curr_height = browser.execute_script("return document.body.scrollHeight")
      if prev_height == curr_height:
          break
      prev_height = curr_height
  soup = BeautifulSoup(browser.page_source,"lxml")
  with open(f'c1025/naver_mous{i+1}.html','w',encoding="utf-8")as f:
      f.write(soup.prettify())
  time.sleep(random.randint(7,10))











