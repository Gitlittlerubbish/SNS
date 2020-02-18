import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

country_list = []

# country = "uk"
# start = "2"

def get_country_code():
	df = pd.read_csv("country_code.csv")
	df = df.drop(['Name'], axis = 1)
	df_l = df.values.tolist()
	rt_list = []

	for item in df_l:
		rt_list.append(str(item[0]))

	return rt_list

def process_page(country, start):
	url = requests.get("https://www.google.com/search?q=filetype:pdf site:" + country + "&start=" + start)
	soup = BeautifulSoup(url.content, features="lxml")
	tags = soup.find_all("a", href=re.compile("(?<=/url\?q=)(htt.*://.*)"))
	rs_list = []

	for tag in tags[:9]:
		tag_str = str(tag)
		rs_list.append(tag_str.split("url?q=")[1].split("&amp")[0])

	return rs_list


def main():
	country_code_list = get_country_code()
	print(country_code_list)

	for code in country_code_list[:10]:
		print("Processing country code:" + code)
		for start in range(10):
			print(".", end='')
			pdf_list = process_page(code, str(start))
			print(pdf_list)
			with open("domains2.txt", "a") as f:
				for pdf in pdf_list:
					f.write(pdf + '\n')
				f.close()
		print("")

if __name__ == "__main__":
	main()

