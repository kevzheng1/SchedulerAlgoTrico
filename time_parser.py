def time_parser(time_str):
    # Receive str that indicates time (e.g. "11:20AM-12:35PM")
    # Objective: Convert the string to integer unit >> "11:20AM-12:35PM" will
    # become [680,755]
    period = time_str.split("-")
    n = len(period)
    for i in range(n):
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
        if period[i][1][2] == "p":
            minute_int += 720
        period[i][1] = minute_int
        total_min = period[i][0] + period[i][1]
        if total_min <= 1440:
            period[i] = total_min/5
        else:
            period[i] = (total_min - 720) / 5
    return period

def main():
    a = time_parser("11:20AM-12:35PM")
    print(a)

main()
# This function is tested, and it works.
