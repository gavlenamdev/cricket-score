import notify2
import os

icon = os.path.abspath("./img/cric_logo.png")
notify2.init("Cricket Score")
n = notify2.Notification(None, icon = icon)

def notifier(message, summery="Cricket Score"):
    n.update(summery,message)
    n.show()
