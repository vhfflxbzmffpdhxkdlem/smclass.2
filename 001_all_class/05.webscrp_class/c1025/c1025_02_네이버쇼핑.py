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


# 평점 4.8이상,평가수 1000명이상 인 상품을 csv파일로 저장하고 출력하시오.
for i in range(5):
  
  with open(f'c1025/naver_mous{i+1}.html','r',encoding="utf-8")as f:
    soup = BeautifulSoup(f,"lxml")
  

  data = soup.select_one("#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx")
  # pros = data.select("div.adProduct_item__1zC9h")
  # print(len(pros))
  # cl = pros[0]['class']
  # print(cl[0])

  # for pro in pros:
  #   if pro['class'][0] == 'adProduct_item__1zC9h':
  #     print('adProduct_item__1zC9h')
  #     name = pro.select_one("div.adProduct_title__amInq > a").text.strip()
  #     print("상품명 :",name)
  #   else:
  #     print('product_item__MDtDF>div')
  #     name = pro.select_one("div.product_title__Mmw2K > a").text.strip()
  #     print("상품명 :",name)
  def chg(val):
    r_val = 0
    if '만' in val: r_val = float(val[:-1])*10000
    else: r_val = float(val.replace(",","")) 
    return r_val

  sells = data.select("div.product_item__MDtDF>div")
  # sell = data.select_one("div.product_item__MDtDF>div")
  # stars = int(sell.select_one("div.product_etc_box__ElfVA > a > em").text.strip().replace(",","").replace('만','').replace(" ","").replace("\n",'').replace("(",'').replace(")",''))
  # print(f"평가수 : {stars:,}")

  for idx,sell in enumerate(sells):
    try:
      name = sell.select_one("div.product_title__Mmw2K > a").text.strip()
      star = float(sell.select_one("div.product_etc_box__ElfVA > a > span.product_grade__IzyU3").text.strip().replace("\n","").replace(" ","")[2:])
      stars = int(sell.select_one("div.product_etc_box__ElfVA > a > em").text.strip().replace(",","").replace('만','')[1:-2])
      price = int(sell.select_one("div.product_price_area__eTg7I > strong > span.price > span.price_num__S2p_v > em").text.strip().replace(",",""))
      if star < 4.8: #or stars < 1000:
          print(f"[ {44*i+(idx+1)}번째 제외 ]")
          continue
      else:
          print(f"[ {44*i+(idx+1)}번째 ]")
          print("상품명 :",name)
          print("평점 :",star)
          print(f"평가수 : {stars:,}")
          print(f"가격 : {price:,}")
    except Exception as e:
      print(f"{44*i+(idx+1)}번째 오류",e)

  for idx,sell in enumerate(sells):
    try:
      name = sell.select_one("div.product_title__Mmw2K > a").text.strip()
      star = float(sell.select_one("div.product_etc_box__ElfVA > a > span.product_grade__IzyU3").text.strip().replace("\n","").replace(" ","")[2:])
      stars = int(sell.select_one("div.product_etc_box__ElfVA > a > em").text.strip().replace(",","").replace('만','')[1:-2])
      price = int(sell.select_one("div.product_price_area__eTg7I > strong > span.price > span.price_num__S2p_v > em").text.strip().replace(",",""))
      if star < 4.8: #or stars < 1000:
          print(f"[ {44*i+(idx+5)}번째 제외 ]")
          continue
      else:
          print(f"[ {44*i+(idx+5)}번째 ]")
          print("상품명 :",name)
          print("평점 :",star)
          print(f"평가수 : {stars:,}")
          print(f"가격 : {price:,}")
    except Exception as e:
      print(f"{44*i+(idx+5)}번째 오류",e)