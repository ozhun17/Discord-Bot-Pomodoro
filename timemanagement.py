import time
from tracemalloc import start
awaketime=time.time()

#pomodoroCheck
#pomodoroRequest



def fiveMinuteCheck():
    startTime = time.time()
    
    currentTime = time.time()
    if(startTime+pomodoroSeconds > currentTime):
        return "done"
    time.sleep(300)


def pomodoroCheck():#returns 0 if time is done, returns remaining time in seconds if time isnt done
    currentTime = time.time()
    stringTimes = file_read_pomodoro()#returns an array of two strings
    startTime = int(stringTimes[0])
    endTime = int(stringTimes[1])
    if(endTime>currentTime):
        file_write_isactive(0)
        return 0
    else:
        return (endTime-currentTime)

def pomodoroRequest(currenttime, expectedtimeminutes):
    isactive = file_read_isactive()
    if(isactive == 0):
        file_write_pomodoro(currenttime, expectedtimeminutes)
        file_write_isactive(1)
        return 1
    else:
        return 0


def file_read_isactive():
    f = open("pomodoroisactive.txt", "r")
    isactive = f.read(1)
    f.close()
    return int(isactive)

def file_write_isactive(isActive):
    f = open("pomodoroisactive.txt", "w")
    stractive = str(isActive)
    f.write(stractive)
    f.close()

def file_write_pomodoro(startTime, expectedTimeMinutes):
    endEpoch = startTime+(expectedTimeMinutes*60)
    f = open("timeholder.txt", "w")
    str1 = str(startTime) + " "+ str(endEpoch) + "\n"  
    f.write(str1)
    f.close()




def file_read_pomodoro():#returns an array of two integers, first value is starting second in epoch, second is end time in epoch
    f = open("timeholder.txt", "r")
    line = f.readline()
    timearray = line.split()
    f.close()
    return timearray