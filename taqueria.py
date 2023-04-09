menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
#setting the total amount to 0
total_amount = 0

while True:
    try:
        item = input("Item: ").title()
        if item in menu:
            #add the item price to total_amount
            total_amount += menu[item]
            #print the current total_amount
            print("Total:$", end="")
            print("{:.2f}".format(total_amount))

    except EOFError:
        print()
        break

