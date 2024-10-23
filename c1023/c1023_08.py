from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
import random

url = "https://flight.naver.com/"

browser = webdriver.Chrome()
browser.maximize_window()  # 창 최대화
browser.get(url)
# 서울제주 11.6 11.9 성인2인 항공검색
# 출발지 클릭
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[1]').click()
# 출발지 입력
time.sleep(1)
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div/div/ul[1]/li[3]/button').click()
time.sleep(1)

# 도착지 클릭
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[2]').click()
time.sleep(1)
# 도착지 검색
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[1]/div/input').send_keys("제주")
time.sleep(1)
# 제주도 선택
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/section/ul/li/a').click()
time.sleep(1)

# 일정 클릭
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[2]/button[1]').click()
time.sleep(1)
# 가는날 클릭
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[4]/button').click()
time.sleep(1)
# 오는날 클릭
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[7]/button').click()
time.sleep(1)

# 인원 클릭
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[3]/button').click()
time.sleep(1)
# 인원 변경
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[4]/div/div/div[1]/div[1]/button[2]').click()
time.sleep(1)
# 항공권 클릭
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/button[1]').click()
time.sleep(1)
# 항공권 검색
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/button[1]').send_keys(Keys.ENTER)

# 데이터가 나타날때까지 대기상태
# 검색중
# time.sleep(8)

# 화면 대기 함수
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 화면대기 - 30초 동안 대기

# 화면에 찾으려고 하는 <html>요소가 있는지 확인
elem = WebDriverWait(browser, 120).until(lambda x: x.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div[2]'))

# 화면 스크롤 내리기
# 현재 스크롤 높이 검색
prev_height = browser.execute_script("return document.body.scrollHeight")
print("최초 높이 :",prev_height)

# 스크롤 내리기 - 1000
while True:
  browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
  time.sleep(2)  # 다른정보가 추가될때까지 대기
  # 높이 확인 - 2000
  curr_height = browser.execute_script("return document.body.scrollHeight")
  if prev_height == curr_height:
    break
  prev_height = curr_height  
  print("현재 높이 :",curr_height)

# 데이터 가져와서 처리
# BeautifulSoup 데이터 처리
# 웨스크래핑
soup = BeautifulSoup(browser.page_source,"lxml")
with open('flight.html','w',encoding='utf-8')as f:
  f.write(soup.prettify())

  input("enter키를 입력하면 프로그램이 종료됩니다.")
  browser.quit()


print("완료")
time.sleep(100000000)






# browser = webdriver.Chrome()
# browser.get(url)
# elem = browser.find_element(By.ID,"query")
# elem.send_keys("네이버항공권")
# elem.send_keys(Keys.ENTER)
# elem = browser.find_element(By.CLASS_NAME,"link_name").click()
