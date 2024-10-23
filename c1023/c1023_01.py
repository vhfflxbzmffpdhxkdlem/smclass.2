import os
import requests
from bs4 import BeautifulSoup
import csv
url = "https://finance.naver.com/sise/sise_quant.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    'Accept-Language':'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료
soup = BeautifulSoup(res.text,"lxml")

# 기준점
data = soup.select_one("#contentarea > div.box_type_l > table")
stocks = data.select("tr")
# print(len(stocks))

# 1. 상단 타이틀. csv파일로 저장
f = open('c1023/stock.csv','w',encoding='utf-8-sig')
writer = csv.writer(f)
st_list = [st.text for st in stocks[0].select("th")]
writer.writerow(st_list)
# print(st_list)
print(len(st_list)) # 상단타이들 항목 : 12개

# 30개 주식정보를  csv파일로 저장

print(len(stocks)) # 50개
for stock in stocks:
  sts = stock.select("td")
  if len(sts) <= 1: continue
  sto_list = [ st.text.strip().replace("\t","").replace("\n","")  for st in sts ]
  print(sto_list)
  writer.writerow(sto_list)  # writerow 리스트타입을 저장
f.close


# 2. 
# print(len(stocks[1].select("td"))) # 항목 : 1개
sto_list =  [sto.text.strip().replace("\t","").replace("=n","") for sto in stocks[2].select("td")]
sto_list2 =  [sto.text.strip().replace("\t","").replace("=n","") for sto in stocks[3].select("td")]
sto_list = ['1', 'KODEX 200선물인버스2X', '2,275', '보합0', '0.00%', '72,439,213', '164,495', '2,260', '2,265', '13,140', 'N/A', 'N/A']
sto_list2 = ['2', 'KODEX 코스닥150선물인버스', '3,840', '상승\n35', '+0.92%', '14,888,627', '56,883', '3,815', '3,820', '2,757', 'N/A', 'N/A']
print(sto_list2)



# # 30개 주식정보를  csv파일로 저장
# s_list = []
# for i in range(2,50):
#   if len(stocks[i].select("td")) == 12:
#     s = [sto.text.strip().replace("\t","").replace("=n","") for sto in stocks[i].select("td")]
#     s_list.append(s)
# print(s_list)
# with open('c1023/s.csv','w',encoding='utf-8-sig',newline='')as f:
#   writer = csv.writer(f)
#   writer.writer(s_list)








# list 생성
# sts = stocks[0].select("th")
# for st in sts:
#   print(st.text)
#   st_list.append(st.text)






