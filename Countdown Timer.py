import time

t = int(input("How many seconds do you want to set the time for?: "))

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("Pencils Down!") 

countdown(t)
