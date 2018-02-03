def weekday_parser(weekday_str):
    # weekday_str = "MWF", "TTH", "MTH", etc.
    weekday_lst = []
    n = len(weekday_str)
    for i in range(n):
        if weekday_str[i] == "H":
            pass
        else:
            if weekday_str[i] == "T" and weekday_str[i+1] == "H":
                weekday_lst.append("H")
            else:
                weekday_lst.append(weekday_str[i])
    # At this point, we have created the list of ["M","T","W","H","F"]
    return weekday_lst
