from cricket_score import get_score
from notification import notifier
import time

refresh = 5
while True:
    score = get_score()
    print(score)
    notifier(score)
    time.sleep(refresh)