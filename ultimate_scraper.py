#CURRENTLY UNUSED


import requests
import urllib.request
import time
from bs4 import BeautifulSoup


chars = ['pt_charizard']
move = 'Neutral Air'

url = 'https://ultimateframedata.com/{0}.php'
for c in chars:
    url2 = url.format(c)
    response = requests.get(url2)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.table
    counter = 0


    for section in soup.find_all('div'):
        if move in str(section):
            try:
                for child in section.find_all('div'):
                    counter += 1
                    if move in str(child):
                        break
                for x in range(counter, counter + 10):
                    print(section.find_all('div')[x].contents[0])
                        
            except:
                pass

        
    time.sleep(0.05)
