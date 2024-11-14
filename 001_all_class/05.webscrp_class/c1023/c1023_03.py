from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
# Chrome()  ()안에 chomedriver.exe. 위치 지점을 입력해줘야함.
# root에 파일이 저장되어 있으면 입력하지 않아도 됨.
browser = webdriver.Chrome()
browser.get("https://naver.com")


# html위치 찾기 - 
elem  = browser.find_element(By.CLASS_NAME,'search_input')
elem.click()

time.sleep(10)