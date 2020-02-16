import requests
from bs4 import BeautifulSoup
import re

country = "uk"
start = "2"

url = requests.get("https://www.google.com/search?q=filetype:pdf site:" + country + "&start=" + start)
soup = BeautifulSoup(url.content, features="lxml")
tags = soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)"))
rs_list = []
cnt = 0

for tag in tags[:9]:
	tag_str = str(tag)
	cnt = cnt + 1
	rs_list.append(tag_str.split("url?q=")[1].split("&amp")[0])

for item in rs_list:
	print(item)
