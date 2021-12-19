
import winsound
import time

def sound():
    winsound.Beep(1000, 1000)

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Enough for today!!')
    sound()

t = input("Enter the time in seconds: ")


countdown(int(t))