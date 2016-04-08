#!/usr/local/bin/python3
# By Joshua Wolfe
# Github: WolfeCub
import time
import datetime
from random import randint

def main():
    print(" ____                                _               _____         _   ")
    print("|  _ \  ___   ___  _ __ ___  ___  __| | __ _ _   _  |_   _|__  ___| |_ ")
    print("| | | |/ _ \ / _ \| '_ ` _ \/ __|/ _` |/ _` | | | |   | |/ _ \/ __| __|")
    print("| |_| | (_) | (_) | | | | | \__ \ (_| | (_| | |_| |   | |  __/\__ \ |_ ")
    print("|____/ \___/ \___/|_| |_| |_|___/\__,_|\__,_|\__, |   |_|\___||___/\__|")
    print("                                              |___/                    ")

    f = open('log.csv', 'a')

    rsp = input("Enable response checking (y/n): ")

    while True:
        var = input()

        if var == "exit":
            break

        year = randint(1900, 2016)
        month = randint(1,12)

        if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or
                month == 10 or month == 12):
            day = randint(1,31)
        elif (month != 2):
            day = randint(1,30)
        elif (month == 2 and isLeapYear(year)):
            day = randint(1,29)
        else:
            day = randint(1,28)

        form = numToMoth(month) + " " + str(day) + ", " + str(year)
        print(form)

        start_time = time.time()

        if (rsp == "y" or rsp == "Y"):
            var = input("Day: ")
        else:
            var = input()

        elapsed_time = time.time() - start_time
        print("Time: " + '{:.2f}'.format(elapsed_time))

        correct = datetime.datetime.strptime(form , '%B %d, %Y').strftime('%A')

        rspck = responseCheck(var, correct)
        split = rspck.split()

        print(correct)

        f.write(time.strftime("%d/%m/%Y") + ',' + time.strftime("%H:%M:%S") + ',' + str(day) + '/' + str(month) + '/' + str(year) + ',' +\
                str(elapsed_time) + ',' + split[0] + ',' + split[4] + ',' + var + '\n')


def isLeapYear(year):
    if (year / float(4) == 0):
        if (year / float(100) == 0):
            if (year / float(400) == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def numToMoth(num):
    if (num == 1):
        return "January"
    elif (num == 2):
        return "February"
    elif (num == 3):
        return "March"
    elif (num == 4):
        return "April"
    elif (num == 5):
        return "May"
    elif (num == 6):
        return "June"
    elif (num == 7):
        return "July"
    elif (num == 8):
        return "August"
    elif (num == 9):
        return "September"
    elif (num == 10):
        return "October"
    elif (num == 11):
        return "November"
    elif (num == 12):
        return "December"

def responseCheck(response, correctDay):
    if (response.lower() in correctDay.lower()):
        return "Correct it was a " + correctDay
    else:
        return "Incorrect it was a " + correctDay

if __name__ == "__main__": main()
