# importing the libraries
from bs4 import BeautifulSoup
import requests


def list_stocks(soup):
    list =[]
    for link in soup.find_all("li")[:-1]:
        link = link.find("span","column stock-name")
        list.append(link)
    return list
    


url="https://money.cnn.com/data/markets/"

html_content = requests.get(url).content

soup = BeautifulSoup(html_content, "lxml")

soup = soup.find("ul","module-body wsod most-popular-stocks")


print (list_stocks(soup))
