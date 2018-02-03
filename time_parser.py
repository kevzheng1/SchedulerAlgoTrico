def time_parser(time_str):
    # Receive str that indicates time (e.g. "11:20AM-12:35PM")
    # Objective: Convert the string to integer unit >> "11:20AM-12:35PM" will
    # become [680,755]
    n = len(time_str)
    period = time_str.split("-")
    for i in range(len(period)):
        period[i] = period[i].split(":")
        # Clean the hour part
        period[i][0] = int(period[i][0])*60
        # Now, moving on to the minute part: "20AM"
        minute_str = ""
        for j in range(2):
            if j == 0:
                if period[i][1][j] == "0":
                    pass
                else:
                    minute_str += period[i][1][j]
            else:
                minute_str += period[i][1][j]
        minute_int = int(minute_str)
        # Clear the AM, PM stuff
        if period[i][1][2] == "P":
            minute_int += 720
        period[i][1] = minute_int
        total_min = period[i][0] + period[i][1]
        if total_min <= 1440:
            period[i] = total_min
        else:
            period[i] = total_min - 720
    return period

# This function is tested, and it works.
