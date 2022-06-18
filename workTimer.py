import time, winsound

def countdown(hours, mins, secs):
    timesecs = hours * 3600 + mins * 60 + secs
    while timesecs > -1:
        # delay by one second
        time.sleep(1)
        timesecs -= 1


# input
workH = int(input("In a whole number, input how many hours you want to work: "))
workM = int(input("In a whole number, input how many minutes you want to work: "))
workS = int(input("In a whole number, input how many seconds you want to work: "))

breakH = int(input("In a whole number, input how many hours you want to take a break: "))
breakM = int(input("In a whole number, input how many hours you want to take a break: "))
breakS = int(input("In a whole number, input how many hours you want to take a break: "))

keepRun = True

while keepRun:
    print("Let's get to work!")
    countdown(workH, workM, workS)
    winsound.Beep(400, 1000)
    print("Time to take a break!")
    countdown(breakH, breakM, breakS)
    winsound.Beep(500, 1000)
    timerRun = input("Would you like to run the timer for the same duration again?  Answer Y for yes, or N for no: ")
    if timerRun.lower() == 'n':
        print("Good job!")
        keepRun = False
