from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
import random

# flight.html 금액이 70,000원 미만 항공권을 출력하시오.
# 김포-제주이하 항공권 개수 : 15개
# 제주-김포이하 항공권 개수 : 15개

with open('flight.html','r',encoding='utf-8')as f:
  soup = BeautifulSoup(f,"lxml")

data = soup.select_one("#__next > div > main > div.domestic_flight_content__vYDHd > div > div.domestic_results__gp5WB")
prs = data.select("div.domestic_Flight__8bR_b")
# print(len(prs))
i = 0
j = 0
for idx,pr in enumerate(prs):
  price = int(pr.select_one("div > div.domestic_prices__WBiv_ > div.domestic_item__5CAye > b > i").text.strip().replace(",",""))
  if price > 70000:
    j += 1
  else: i += 1
print("김포-제주이하 항공권 개수 : ",i)
print("제주-김포이하 항공권 개수 : ",j)
