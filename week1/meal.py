def main():
    time = input("What time is it? ")
    time_converted = convert(time)
    if time_converted >= 7 and time_converted <= 8:
        print("breakfast time")
    elif time_converted >= 12 and time_converted <= 13:
        print("lunch time")
    elif time_converted >= 18 and time_converted <= 19:
        print("dinner time")
    else:
        print("Not meal time")


def convert(time):
    if "p.m." in time:
        time, _ = time.split(" ")
        hours, minutes = time.split(":")
        if hours != "12":
            return float(hours) + 12 + float(minutes) / 60
        else:
            return float(hours) + float(minutes) / 60
    elif "a.m." in time:
        time, _ = time.split(" ")
        hours, minutes = time.split(":")
        return float(hours) + float(minutes) / 60
    else:
        hours, minutes = time.split(":")
        return float(hours) + float(minutes) / 60


if __name__ == "__main__":
    main()