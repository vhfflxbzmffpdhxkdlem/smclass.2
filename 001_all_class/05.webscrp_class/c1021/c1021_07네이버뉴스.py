import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")



newList = soup.find("div",{"class":"rankingnews_box_wrap"}).find("div",{"class":"rankingnews_box"})
print(newList.find("strong",{"class":"rankingnews_name"}).text)
rank = newList.find("ul",{"class":"rankingnews_list"})

# newList = soup.find("a",{"class":"rankingnews_box_head nclicks('RBP.rnkpname')"}).find("strong",{"class":"rankingnews_name"})
# print(newList.text)


# ranks = soup.find("ul",{"calss":"rankingnews_list"})
# tlists = ranks.find_all("li")

# 5번 반복
# for i,t in enumerate(tlists):
#   pass
