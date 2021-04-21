''' 
Python library for pulling data out of HTML and XML files.
Parse tree navigating, searching, modifying
http://www.crummy.com/software/BeautifulSoup/

for gathering and organizing web data, BeautifulSoup makes scraping websites easy. BeautifulSoup is great for web pages that use special characters as you can easily pass different encoding formats to its functions when gathering web data.
'''


# BeautifulSoup

import requests
from b4 import BeautifulSoup
def trade_spider(max_pages):
  page = 1
  while page <= max_pages:
    url = 'https://buckysroom.org/trade/search.php?page=' + str(page)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for link in soup.findAll('a', {'class': 'item-name'}):
        href = "https://buckysroom.org" + link.get('href')
        title = link.string
        print(href)
        print(title)
    page += 1
    
trade_spider(1)





#Description:
#This file is alternative solution for web crowler. 
# Mayor reason for this is that website BuckysRoom.com is down, so original code doesnot work anymore. 
# Solution description (what this program does):
#This program goes on website https://www.thenewboston.com/search.php?type=0&sort=reputation ,
#and goes on every user's profile, and on that profile, 
#it prints the first few (approx. 20) links of latest photos. To view photos, click on url or copy in web broser.

# But history is changing and sooner or later this file or program will not work!. 
# On day of the creation this program was working. 

import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://thenewboston.com/search.php?type=0&sort=reputation&page==' + str(page)
        source_code = requests.get(url, allow_redirects=False)
        # just get the code, no headers or anything
        plain_text = source_code.text.encode('ascii', 'replace')
        # BeautifulSoup objects can be sorted through easy
        soup = BeautifulSoup(plain_text,'html.parser')
        for link in soup.findAll('a', {'class': 'user-name'}):
            href = link.get('href')
            title = link.string  # just the text, not the HTML
            print(href)
            print(title)
            #get_single_item_data(href)
        page += 1

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"lxml")
    # if you want to gather photos from that user
    for item_name in soup.findAll('img', {'class': 'img-responsive'}): # all photos of the user
        photo='https://thenewboston.com'+item_name.get('src')
        print(photo)
    # if you want to gather links for a web crawler
    for link in soup.findAll('a'):
        href = link.get('href')
        print(href)

trade_spider(1)








# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

def parser(file):    
    soup = BeautifulSoup(open(f"I:/assets-w/js/learnjs/js in easy steps 5th/{file}"), "html.parser")
    links = soup.findAll('a')
    totalLinks = len(links)
    if (totalLinks == 0 and file[-3:]==".js"):        
        print(f"    {soup.get_text()}")
    if (totalLinks > 0):
        print(f"{totalLinks} LINKS\n")
        for a in links:
            href = a.get('href')
            print(f"{a.get_text()} ==> {href}")
            parser(href)
    else:
        scripts = soup.findAll('script')
        totalScripts = len(scripts)
        if (totalScripts > 0):
            src = scripts[0].get('src')
            if (src == None):
                print(f"    SCRIPT: NONE")
            else:
                print(f"    SCRIPT:{src}")
                print("------------------------------------------------------------")
                parser(f"{file.split('/')[0]}/{src}")
            
        
# Webscrape from
file = 'JSIES.html'
parser(file)







# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
url = 'http://web.mta.info/developers/turnstile.html'

# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(response.text, "html.parser")

# To download the whole data set, let's do a for loop through all a tags
for i in range(36,len(soup.findAll('a'))+1): #'a' tags are for links
    one_a_tag = soup.findAll('a')[i]
    link = one_a_tag['href']
    download_url = 'http://web.mta.info/developers/'+ link
    urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:]) 
    time.sleep(1) #pause the code for a sec
    