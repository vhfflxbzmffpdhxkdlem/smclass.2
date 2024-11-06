# 다음사이트에서 검색창에 주식정보 입력해서 페이지 이동을 하시오.
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
# Chrome()  ()안에 chomedriver.exe. 위치 지점을 입력해줘야함.
# root에 파일이 저장되어 있으면 입력하지 않아도 됨.
browser = webdriver.Chrome()
browser.get("https://daum.net")
elem  = browser.find_element(By.ID,'q')
elem.click()  # 클릭
elem.send_keys("주식정보")
elem.send_keys(Keys.ENTER)
time.sleep(100)

browser.get("https://naver.com")
elem  = browser.find_element(By.CLASS_NAME,'search_input')
elem.send_keys("주식정보")
elem.send_keys(Keys.ENTER)

time.sleep(100)

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import requests
# from bs4 import BeautifulSoup
# browser = webdriver.Chrome()
# browser.get("https://naver.com")


# # html위치 찾기 - 
# elem  = browser.find_element(By.CLASS_NAME,'MyView-module__link_login___HpHMW')
# elem.click()  # 클릭
# browser.back() # 뒤로
# browser.forward() # 앞으로
# browser.refresh() # 새로고침
# elem = browser.find_element(By.NAME,'pw')


# elem=browser.find_element(By.ID,"query")
# # 글자입력
# elem.send_keys("네이버영화")
# # enter키 입력
# elem.send_keys(Keys.ENTER)
# # 클릭
# elem.click()

# # 새창이동
# browser.switch_to.window(browser.window_handles[1])

# time.sleep(100)



