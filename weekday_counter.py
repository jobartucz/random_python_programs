import time
import calendar

def most_frequent_days(year_in):
    year = str(year_in).zfill(4)

    newyear = time.strptime("31 Dec " + year, "%d %b %Y")
    weekday = time.strftime("%A", newyear)

    count = {}
    count['Monday'] = 52
    count['Tuesday'] = 52
    count['Wednesday'] = 52
    count['Thursday'] = 52
    count['Friday'] = 52
    count['Saturday'] = 52
    count['Sunday'] = 52

    count[weekday] = count[weekday] + 1

    if (calendar.isleap(int(year)) == True):
        newyear = time.strptime("30 Dec " + year, "%d %b %Y")
        weekday = time.strftime("%A", newyear)
        count[weekday] = count[weekday] + 1
        
    toreturn = []
    for day in count:
        if (count[day] == 53):
            toreturn.append(day)

    return toreturn
