def computepay(hours, rate):
    #print("In computepay", hours, rate)
    if hours > 40:
        #print("Overtime")
        regular = rate * hours
        overtime = (hours - 40.0) * (rate * 0.5)
        #print(regular,overtime)
        pay = regular + overtime
    else:
        #print("Regular")
        pay = hours * rate
    print("Returning", pay)
    return pay

hours = input("Enter Hours:")
rate = input("Enter Rate: ")
float_hours = float(hours)
float_rate = float(rate)

xp =  computepay(float_hours, float_rate)

print("Pay:", xp)