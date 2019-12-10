from bs4 import BeautifulSoup
import urllib.request

def get_
html 

soup = BeautifulSoup(html)
print(soup.get_text())


fp = urllib.request.urlopen("http://www.python.org")
mybytes = fp.read()
fp.close()

mystr = mybytes.decode("utf8")


print(mystr)