import winsound
import time
from datetime import datetime

def sound():
    winsound.Beep(1000, 1000)

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
        print(t)

    print('Enough for today!!')
    sound()

def rest_calculator():
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)

    a = int(input("La ce ora doriti sa finalizati activitatea?"))
    b = int(input("La ce minut al orei doriti sa finalizati activitatea?"))
    c = int(input("La ce secunda al minutului doriti sa finalizati activitatea?"))
    rest_total = 0
    rest_ora_secunde = 0
    rest_minute_secunde = 0
    rest_secunde = 0

    if c < int(now.strftime("%M")):
        rest_secunde = 60 - int(now.strftime("%S"))
    else:
        rest_secunde = c - int(now.strftime("%S"))
    if b >= int(now.strftime("%M")):
        rest_minute = b - int(now.strftime("%M"))
        rest_minute_secunde = rest_minute * 60
        xyz = False
    else:
        rest_minute = (60 - (int(now.strftime("%M")) - b)) * 60
        rest_minute_secunde = rest_minute * 60
        xyz = True
    if a == int(now.strftime("%H")):
        rest_ora = 0
    else:
        if xyz == False:
            rest_ora = a - int(now.strftime("%H"))
            rest_ora_secunde = rest_ora * 3600
        else:
            rest_ora = a - int(now.strftime("%H")) - 1
            rest_ora_secunde = rest_ora * 3600
    rest_total = rest_ora_secunde + rest_minute_secunde + rest_secunde
    print(rest_total)
    return rest_total

t = rest_calculator()

countdown(int(t))