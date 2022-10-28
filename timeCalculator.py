def add_time(start, duration, currentDay=""):

    daysarr = [
        ", Sunday",
        ", Monday",
        ", Tuesday",
        ", Wednesday",
        ", Thursday",
        ", Friday",
        ", Saturday",
    ]
    daysDict = {
        "Sunday": 1,
        "Monday": 2,
        "Tuesday": 3,
        "Wednesday": 4,
        "Thursday": 5,
        "Friday": 6,
        "Saturday": 7,
    }

    currentDay = currentDay.capitalize()
    day = ""
    daynum = -1
    if currentDay != "":
        day = f", {currentDay}"
        daynum = daysDict[currentDay]

    time = start.split(" ")
    hr, mi = time[0].split(":")
    meridiem = time[1]
    dhr, dmi = duration.split(":")

    totalHr = int(hr) + int(dhr)
    totalMin = int(mi) + int(dmi)

    if totalMin > 59:
        totalMin -= 60
        totalHr += 1
    totalMin = totalMin if totalMin > 9 else "0" + str(totalMin)

    que = totalHr / 12
    # print(int(que))
    if totalHr >= 12:
        if meridiem == "PM" and int(que) <= 1 or meridiem == "AM" and int(que) == 2:
            if daynum == 7:
                daynum -= 7
                day = daysarr[int(daynum)]
            day += " (next day)"
        elif meridiem == "AM" and int(que) >= 4 or meridiem == "PM" and int(que) >= 3:
            if daynum != -1:
                daynum += int(que / 2)
                if daynum > 7:
                    totalDay = int(daynum / 7)
                    daynum -= 7 * int(totalDay)
                    day = daysarr[int(daynum)]
                else:
                    day = daysarr[int(daynum)]
            day += f" ({int(que/2+1)} days later)"
        if int(que) % 2 != 0 or int(que) == 0:
            swap = {"AM": "PM", "PM": "AM"}
            meridiem = swap[meridiem]
        totalHr -= 12 * int(que)
        if totalHr == 0:
            totalHr = 12

    new_time = str(totalHr) + ":" + str(totalMin) + " " + meridiem + day

    return new_time
