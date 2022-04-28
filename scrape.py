from bs4 import BeautifulSoup
import requests
import pandas as pd

starturl = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

headers = ["name","distance","mass","radius"]
data = []

page = requests.get(starturl)
soup = BeautifulSoup(page.text,"html.parser")

startable = soup.find("table")

templist = []
trtags = startable.find_all("tr")

for tr in trtags :
    tdtags = tr.find_all("td")
    row = [i.text.rstrip() for i in tdtags]    
    templist.append(row)

names = []
distance = []
radius = []
mass = []
Lum = []

for i in range(1,len(templist)) :
    names.append(templist[i][1])
    distance.append(templist[i][3])
    radius.append(templist[i][6])
    mass.append(templist[i][5])
    Lum.append(templist[i][7])

DF = pd.DataFrame(list(zip(names,distance,mass,radius,Lum)),columns=["Star_Name","Distance","Mass","Radius","Luminosity"])
DF.to_csv("STAR.csv")