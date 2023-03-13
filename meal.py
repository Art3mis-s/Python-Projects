def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    return hours + minutes / 60

def main():
    meal = input("What time is it? ")
    time = convert(meal)

    if time >= 6 and time < 9:
        print("breakfast time")
    elif time >= 12 and time < 14:
        print("lunch time")
    elif time >= 18 and time < 21:
        print("dinner time")

if __name__ == "__main__":
    main()