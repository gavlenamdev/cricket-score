from cricket_score import get_score
from notification import notifier
import time

refresh = 60
while True:
    team1 = 'IND'
    team2 = 'PAK'
    score = get_score(team1, team2)
    print(score)
    notifier(score)
    time.sleep(refresh)