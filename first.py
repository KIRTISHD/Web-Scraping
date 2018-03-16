#Check Latest


#Open url and get page source
from urllib.request import urlopen
wiki = "http://m.fanfox.net"
page = urlopen(wiki)

#playing with site
from bs4 import BeautifulSoup
soup = BeautifulSoup(page)
soup.prettify()


"""
#find all links in page

all_links=soup.find_all("a",class_="post")
for link in all_links:
    print (link.get("href"))
print ()
"""

"""
#Find links for mangas -
mydivs = soup.findAll("div", {"class": "post"})
for div in mydivs:
    print(div.find('a')['href'])
"""


def crlist(a):
    import re
    pattern = r"http://m.fanfox.net/manga/"
    text = a
    subs = re.sub(pattern, "", text)

    return str.replace(subs,"_"," ")


A = [[]]
mydivs = soup.findAll("div", {"class": "post"})
for div in mydivs:
    A[-1].append([div.find('a')['href']])
    #A[-1].append(crlist(str([div.find('a')['href']])))
    A[-1].append(crlist(str(A[-1][0])))
    A.append([])


print (type(A))
