from datetime import *


dt = datetime.strptime(str(datetime.today())[2:-7], "%y-%m-%d %H:%M:%S")
week = dt.isocalendar()[1]

print()

for i in range(0, 37, 6):
    print(i)
