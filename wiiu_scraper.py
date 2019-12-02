import requests
import urllib.request
import time
from bs4 import BeautifulSoup

def getData(char, move, mtype):
    datalist = []
    parts = []
    pointer = 0
    final = '__**'
    url = 'http://kuroganehammer.com/Smash4/{0}'
    
    url2 = url.format(char)
    response = requests.get(url2)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.table


    for section in soup.find_all('tr'):
        if move in str(section):
            try:
                #a = str(section.th).split('<')[1]
                #print(a.split('>')[1])
                parts.append(section.th.contents[0])
                for child in section.find_all('td'):
                    datalist.append(child.contents[0])
            except:
                pass
    if (mtype == 0):
        return("WIP")
    elif (mtype == 1):
        for x in parts:
            final += x + " | "
        final = final[:-2] + "**__\nHitbox Active: "
        for x in parts:
            final += str(datalist[pointer * int(len(datalist)/len(parts))]) + " | "
            pointer += 1
        pointer = 0
        final = final[:-2] + "\nFAF: "
        for x in parts:
            final += str(datalist[1 + pointer * int(len(datalist)/len(parts))]) + " | "
            pointer += 1
        pointer = 0
        final = final[:-2] + "\nBase Dmg: "
        for x in parts:
            final += str(datalist[2 + pointer * int(len(datalist)/len(parts))]) + " | "
            pointer += 1
        pointer = 0
        final = final[:-2] + "\nAngle: "
        for x in parts:
            final += str(datalist[3 + pointer * int(len(datalist)/len(parts))]) + " | "
            pointer += 1
        pointer = 0
        final = final[:-2] + "\nBKB: "
        for x in parts:
            final += str(datalist[4 + pointer * int(len(datalist)/len(parts))]) + " | "
            pointer += 1
        pointer = 0
        final = final[:-2] + "\nKBG: "
        for x in parts:
            final += str(datalist[5 + pointer * int(len(datalist)/len(parts))]) + " | "
            pointer += 1
        final = final[:-2]
    elif (mtype == 2):
        for x in parts:
            final += x + " | "
        final = final[:-2] + "**__\nHitbox Active: "
        for x in parts:
            final += str(datalist[pointer * int(len(datalist)/len(parts))]) + " | "
            pointer += 1
        pointer = 0
        final = final[:-2] + "\nFAF: "
        for x in parts:
            final += str(datalist[1 + pointer * int(len(datalist)/len(parts))]) + " | "
            pointer += 1
        final = final[:-2]
    elif (mtype == 3):
        for x in parts:
            final += x + " | "
        final = final[:-2] + "**__\nWeight Dependent?: "
        for x in parts:
            final += str(datalist[pointer * int(len(datalist)/len(parts))]) + " | "
            pointer += 1
        pointer = 0
        final = final[:-2] + "\nBase Dmg: "
        for x in parts:
            final += str(datalist[1 + pointer * int(len(datalist)/len(parts))]) + " | "
            pointer += 1
        pointer = 0
        final = final[:-2] + "\nAngle: "
        for x in parts:
            final += str(datalist[2 + pointer * int(len(datalist)/len(parts))]) + " | "
            pointer += 1
        pointer = 0
        final = final[:-2] + "\nBKB: "
        for x in parts:
            final += str(datalist[3 + pointer * int(len(datalist)/len(parts))]) + " | "
            pointer += 1
        pointer = 0
        final = final[:-2] + "\nKBG: "
        for x in parts:
            final += str(datalist[4 + pointer * int(len(datalist)/len(parts))]) + " | "
            pointer += 1
        final = final[:-2]
    elif (mtype == 4):
        for x in parts:
            """
            print(x + " data:")
            print(datalist[pointer:(pointer + int(len(datalist)/len(parts)))])
            """
            #final += x + " data:\n" + str(datalist[pointer:(pointer + int(len(datalist)/len(parts)))]) + "\n"
            #pointer += int(len(datalist)/len(parts))
            final += x + " | "
        final = final[:-2] + "**__\nHitbox Active: "
        for x in parts:
            final += str(datalist[pointer * int(len(datalist)/len(parts))]) + " | "
            pointer += 1
        pointer = 0
        final = final[:-2] + "\nFAF: "
        for x in parts:
            final += str(datalist[1 + pointer * int(len(datalist)/len(parts))]) + " | "
            pointer += 1
        pointer = 0
        final = final[:-2] + "\nBase Dmg: "
        for x in parts:
            final += str(datalist[2 + pointer * int(len(datalist)/len(parts))]) + " | "
            pointer += 1
        pointer = 0
        final = final[:-2] + "\nAngle: "
        for x in parts:
            final += str(datalist[3 + pointer * int(len(datalist)/len(parts))]) + " | "
            pointer += 1
        pointer = 0
        final = final[:-2] + "\nBKB: "
        for x in parts:
            final += str(datalist[4 + pointer * int(len(datalist)/len(parts))]) + " | "
            pointer += 1
        pointer = 0
        final = final[:-2] + "\nKBG: "
        for x in parts:
            final += str(datalist[5 + pointer * int(len(datalist)/len(parts))]) + " | "
            pointer += 1
        pointer = 0
        final = final[:-2] + "\nLanding Lag: "
        for x in parts:
            final += str(datalist[6 + pointer * int(len(datalist)/len(parts))]) + " | "
            pointer += 1
        pointer = 0
        final = final[:-2] + "\nAutocancel: "
        for x in parts:
            final += str(datalist[7 + pointer * int(len(datalist)/len(parts))]) + " | "
            pointer += 1
        final = final[:-2]
    elif (mtype == 5):
        return("WIP")
    else:
        return("Something went wrong")


    return(final)

