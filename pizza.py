import csv
import sys
from tabulate import tabulate

def main():
    check_command_line_arg()
    # creating a variable to store the table data
    table = []
    # try to open the file
    try:
        with open(sys.argv[1], "r") as csvfile:
            file_reader = csv.reader(csvfile)
            for row in file_reader:
                table.append(row)

    except FileNotFoundError:
        sys.argv("File does not exist")
    # printing the table
    print(tabulate(table[1:], headers=table[0], tablefmt="grid"))

def check_command_line_arg():
    # checking how many elements in the command line
    if len(sys.argv) < 2:
        sys.exit("Too few command line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command line arguments")
    # checking if it is a CSV file
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()