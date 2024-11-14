import requests
from bs4 import BeautifulSoup

url = "https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&xfrom=main^gnb"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
# print(res.text)

# soup변환
soup = BeautifulSoup(res.text,"lxml")
#best = soup.find('div',{"id":'bestPrdList'}).find("h3",{"class":"tit"})
best = soup.find('div',{"id":'bestPrdList'}).h3
print(best.text)

# ls0 = soup.find("li",{"id":"thisClick_2190613796"}).find("div",{"class":"pname"}).p
lists = soup.find_all("li")

for idx,list in enumerate(lists):
  p_title = list.find("div",{"class":"pname"}).p.text
  print(f"{idx+1}. {p_title}")


