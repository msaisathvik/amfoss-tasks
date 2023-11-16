import requests
import json
from bs4 import BeautifulSoup
import csv 
import os

url = "https://www.espncricinfo.com/live-cricket-score"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

mydict=[]
'''def getScore():
    
    for x in soup.find_all("div", {"class": "ds-px-4 ds-py-3"}):
        score = []
        for m in x.find_all("span", {"class": "ds-text-raw-red"}):
            if m.text == "Live":
                for y in x.find_all("p", {"class": "ds-text-tight-m"}):
                    score.append(y.text)
                score.append(score[0] + " vs " + score[1])
                for o in x.find_all("div", {"class": "ds-text-compact-s"}):
                    score.append(o.text)
    return score'''


def write(mydict):
    fields= ["team1","team1-score","team2","team2-score"]
    filename = "scores.csv"
    file_exists = os.path.isfile(filename)
    
    with open(filename,'w') as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames = fields)
        writer.writeheader()
        writer.writerows(mydict)
        
    
def getScores():
    for x in soup.find_all("div", {"class": "ds-px-4 ds-py-3"}):
        for m in x.find_all("span", {"class": "ds-text-raw-red"}):
            n=[]
            rows = {}
            if m.text == "Live":
                for y in x.find_all("p", {"class": "ds-text-tight-m"}):
                    n.append(y.text)  
                for o in x.find_all("div", {"class": "ds-text-compact-s"}):
                    n.append(o.text)
                if len(n)==2:
                    n.append("yet to begin")
                    n.append("yet to begin")
                elif len(n)==3:
                    n.append("yet to bat") 
                rows = {"team1": n[0],"team1-score":n[2],"team2":n[1],"team2-score":n[3]}
                mydict.append(rows)
                write(mydict)
getScores()

def getScore():
    score=[]
    score.extend([mydict[0]['team1'],mydict[0]['team2'],mydict[0]['team1']+" vs "+mydict[0]['team2'],mydict[0]['team1-score'],mydict[0]['team2-score']])
    return score