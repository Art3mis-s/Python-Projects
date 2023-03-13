#prompting the user to input their office hours
hours = input("Enter Hours:")
rate = input("Enter Rate: ")
#changing the user's input into floating point number for accurate calculation
float_hours = float(hours)
float_rate = float(rate)
#print(float_rate, float_hours)
if float_hours > 40:
    print("Overtime")
    regular = float_rate * float_hours
    overtime = (float_hours - 40.0) * (float_rate * 0.5)
    print(regular,overtime)
    #'xp' s the payment variable name
    xp = regular + overtime
else:
    print("Regular")
    xp = float_hours * float_rate
print(xp)