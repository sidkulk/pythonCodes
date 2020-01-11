import calendar
import pandas as pd
import sys

def CalProg():
    months = {
                'january':1,
                'January':1,
                'february':2,
                'February':2,
                'march':3,
                'March':3,
                'april':4,
                'April':4,
                'may':5,
                'june':6,
                'June':6,
                'july':7,
                'July':7,
                'august':8,
                'August':8,
                'september':9,
                'September':9,
                'october':10,
                'October':10,
                'november':11,
                'November':11,
                'december':12,
                'December':12
            }
    print('Enter the year and month to display the calendar: ')
    yr = input()
    if yr.isdecimal()==False:
        print('Enter a valid year!')
    else:
        yr = int(yr)
        mon = input()
        if mon.isalpha()==False:
            print('Enter a valid month!')
        else:
            monstr = mon
            mon = months[mon]
            cal = calendar.month(yr, mon)
            print('The calendar for the month of',monstr, yr, ': \n')
            print(cal)

        
def MainFun():
    print('Program to print the calendar of any month of the year')
    ch = 'y'
    while ch:
        CalProg()
        ch = input('Do you want to repeat?(y/n)')
        if ch=='y':
            pass
        else:
            sys.exit()

MainFun()
