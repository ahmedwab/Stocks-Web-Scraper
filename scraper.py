# importing the libraries
from bs4 import BeautifulSoup
import requests


url="https://money.cnn.com/data/markets/"

html_content = requests.get(url).content

soup = BeautifulSoup(html_content, "lxml")

soup = soup.find("ul","module-body wsod most-popular-stocks")


for link in soup.find_all("li")[:-1]:
    print(link.find("span","column stock-name").text)
