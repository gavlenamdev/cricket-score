import requests
from bs4 import BeautifulSoup
import re

def set2str(output):
    final = ""
    for s in output:
        final += s + "\n"
    return final
    
def get_score():
    res = requests.get("https://www.cricbuzz.com/")
    soup = BeautifulSoup(res.text,"html.parser")
    body = soup.find("body")
    text = body.get_text()
    output = set()
    for obj in re.findall("[A-Z]{3}\d{1,3}[\/\-]\d{1,2}\s\(\d{1,2}\.\d Ovs\)",text):
        output.add(obj[:3]+' '+ obj[3:])
    for obj in re.findall("[A-Z]{3}\d{1,3}[\/\-][a-z]{3}\s[a-z]{3}\s\(\d{1,2}\.\d Ovs\)",text):
        output.add(obj[:3]+' '+ obj[3:])
    output = set2str(output)
    return output