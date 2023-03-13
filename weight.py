#prompting the user to enter their weight
weight = int(input('Weight: '))
#asking if the input is in KG or Lbs
unit = input('(L)bs or (K)g: ')
#converting the kg to lbs or lbs to kg
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")

