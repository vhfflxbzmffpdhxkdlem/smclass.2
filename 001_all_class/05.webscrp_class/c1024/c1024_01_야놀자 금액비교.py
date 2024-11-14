from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from bs4 import BeautifulSoup
import random


url = "https://www.yanolja.com/?trackcode=mkt_google_sa&utm_source=google_sa&utm_medium=cpc&utm_campaign=20738115572&utm_content=160897187931&utm_term=kwd-298391364620&gad_source=1&gclid=EAIaIQobChMI29CvyuKliQMVBQt7Bx1CWiIrEAAYASAAEgJVavD_BwE"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)
time.sleep(1)
# 야놀자 검색창 클릭
browser.find_element(By.XPATH,'//*[@id="__next"]/div/div/header/section/a[2]').click()
time.sleep(1)
# 날짜 선택
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div/div[1]/form/div/div[2]/div[1]/button').click()
time.sleep(1)
# 시작날짜 선택하기
browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td[2]').click()
time.sleep(1)
# 끝 날짜 선택하기
browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td[4]').click()
time.sleep(1)
# 날짜 선택 완료
browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[4]/button').click()

# 검색 클릭
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div/div[1]/form/div/div[1]/div/input').click()
time.sleep(1)
# 검색 입력
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div/div[1]/form/div/div[1]/div/input').send_keys("강릉호텔")
time.sleep(1)
# 페이지 이동
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div/div[1]/form/div/div[1]/div/input').send_keys(Keys.ENTER)
# time.sleep(3)
# 자동시 로딩 대기
# 화면의 호텔검색내용이 뜰때까지 대기, 최대 30초 까지 대기
WebDriverWait(browser,30).until(lambda x:x.find_element(By.XPATH,'//*[@id="__next"]/div/main/section/div[2]/div[1]'))

# 화면 스크롤 내리기
prev_height = browser.execute_script("return document.body.scrollHeight")
print("최초 높이 :",prev_height)
while True:
  browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
  time.sleep(1)
  # 페이지가 로딩되면서 길어진 길이를 다시 가져옴
  curr_height = browser.execute_script("return document.body.scrollHeight")
  if prev_height == curr_height:
    break
  prev_height = curr_height
  print("현제 높이 :",curr_height)
print("스크롤 내리기 완료")
soup = BeautifulSoup(browser.page_source,"lxml")


# html 저장하기
with open('c1024/yanolja.html','w',encoding='utf-8')as f:
  f.write(soup.prettify())

#  평점이 4.8이상 금액: 17만원 이하 검색해서 출력
# 1. 
# 호텔명 :
# 평점 :
# 금액 :
#--------------------
# 2.


# 기준점
data = soup.select_one("#__next > div > main > section > div.PlaceListBody_listContainer__2qFG1")
# 호텔 여러개 정보리스트
sells = data.select("a.common_clearfix__M6urU")
j = 0 # 맞지 않는 개수
k = 0 # 예외처리 - 마감(금액없을시)
search_list = []
count = 0
for i,sell in enumerate(sells):
  try:
    name = sell.select_one("strong.PlaceListTitle_text__2511B").text.strip()
    star = float(sell.select_one("span.PlaceListScore_rating__3Glxf").text.strip())
    price = int(sell.select_one("span.PlacePriceInfoV2_discountPrice__1PuwK").text.strip().replace(",",""))
    if star < 4.8 or price > 180000: 
      print(f'[ {i+1} ]')
      print("제외")
      j += 1
      continue
    else: 
      print(f'[ {i+1} ]')
      print("호텔명 :",name)
      print("평점 :",star)
      print("가격 :",price)
      print("-"*80)
      search_list.append([i+1,name,star,price])
  except Exception as e:
    print((i+1),": 예외 처리",e)
    k += 1
i = len(sells)-(k+j)
print("조건에 맞는 개수 :",i)
print("조건에 안맞는 개수 :",j)
print("에러 개수 :",k)
print(len(sells))


# 평점 역순 정렬
search_list.sort(key = lambda x:x[2],reverse=True)
print(search_list[:5])

# 금액 순차정렬
search_list.sort(key = lambda x:x[3])
print(search_list[:5])

#__next > div > main > section > div.PlaceListBody_listContainer__2qFG1

# 파일을 불러와서 soup으로 파싱
# with open('c1024/yanolja.html','r',encoding='utf-8')as f:
#   soup = BeautifulSoup(f,'lxml')


print("완료")
time.sleep(100)





