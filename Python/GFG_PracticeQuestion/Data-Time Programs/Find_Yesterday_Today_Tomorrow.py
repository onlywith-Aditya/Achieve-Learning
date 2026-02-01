from datetime import datetime, timedelta

presentday=  datetime.now()

yesterday= presentday-timedelta(1)
tomorrow= presentday + timedelta(1)
print("Present: ", presentday.strftime('%d-%m-%Y'))
print("Yesterday: ", yesterday.strftime('%d-%m-%Y'))
print("Tomorrow: ", tomorrow.strftime('%d-%m-%Y'))
