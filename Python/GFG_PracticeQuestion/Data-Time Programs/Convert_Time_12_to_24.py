from datetime import datetime
def convert24(time):
    t = datetime.strptime(time, '%I:%M:%S %p')
    return t.strftime('%H:%M:%S')


print(convert24('11:21:30 PM'))  
print(convert24('12:12:20 AM'))