import requests
from bs4 import BeautifulSoup
import re

def set2str(output):
    final = ""
    for s in output:
        final += s + "\n"
    return final
    
def get_score(team1, team2):
	# returns top 2 scores
    res = requests.get("https://www.cricbuzz.com/cricket-match/live-scores")
    soup = BeautifulSoup(res.text,"html.parser")
    body = soup.find("body")
    text = body.get_text()
    scores = []
    for obj in re.findall("[A-Z]{2,3}\s\d{1,3}[\/\-]{0,1}\d{1,2}\s\(\d{1,2}\.\d Ovs\)",text):
    	if team1 in obj or team2 in obj:
        	scores.append(obj)
        # break
    for obj in re.findall("[A-Z]{2,3}\s\d{1,3}[\/\-][a-z]{3}\s[a-z]{3}\s\(\d{1,2}\.\d Ovs\)",text):
        if team1 in obj or team2 in obj:
        	scores.append(obj)
        # break
    output = set2str(scores)
    return output