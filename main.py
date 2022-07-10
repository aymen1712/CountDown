import time


def countdown(t):
    while t:
        minutes, seconds = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(minutes, seconds)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
        print(int(t))
    print("Timer Completed!")


t = input("Enter the timer: ")
countdown(int(t))
