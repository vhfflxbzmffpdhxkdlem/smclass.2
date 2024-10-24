from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from bs4 import BeautifulSoup
import random
from selenium.webdriver.chrome.options import Options

# 노트북 검색 된 사이트 1,2,3 페이지 에서
# 만족도 95 이상이면서,평가수 100이상, 금액 150만원 이하 검색하시오.

# 화면 숨김처리
# option = Options()
# option.add_argument("--headless")
# option.add_argument("--window-size-1920,1080")
# option.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36")


# url = 'https://www.gmarket.co.kr/n/search?keyword=%EB%85%B8%ED%8A%B8%EB%B6%81&k=53&p=1'
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",'Accept-Language':'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}
# res = requests.get(url,headers=headers)
# soup = BeautifulSoup(res.text,"lxml")

# for i in range(3):
#   url = f'https://www.gmarket.co.kr/n/search?keyword=%EB%85%B8%ED%8A%B8%EB%B6%81&k=53&p={i+1}'
#   print(url)
#   browser = webdriver.Chrome(options=option)
#   browser.maximize_window()
#   browser.get(url)
#   time.sleep(3)
#   soup = BeautifulSoup(browser.page_source,"lxml")
#   browser.get_screenshot_as_file(f"market{i+1}.png")
#   with open(f"c1024/gmarket{i+1}.html",'w',encoding='utf-8')as f:
#     f.write(soup.prettify())
#   input("엔터키 입력완료")

# 파일 불러오기
for i in range(3):
  with open(f"c1024/gmarket{i+1}.html",'r',encoding='utf-8')as f:
    soup = BaseException(f,"lxml")

# 기본값

