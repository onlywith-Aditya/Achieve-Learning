from datetime import datetime

w = datetime.now()
print(w)
currentTime = w.strftime("%H:%M:%S")
print(currentTime)