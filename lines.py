import sys

def main():
    # Checking the command line argument
    check_command_line_arg()
    # trying to open the file
    try:
        # opening the file in read mode
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()
    # if it can't open this means that the file does not exist
    except FileNotFoundError:
        sys.exit("File does not exist")
    # Looping through the lines and check if starts with # or whitespace
    count_lines = 0
    for line in lines:
        if check_comment_or_empty_line(line) == False:
            count_lines += 1
    print(count_lines)

# Funciton to check the command line arguments
def check_command_line_arg():
    # checking how many elements in the command line
    if len(sys.argv) < 2:
        sys.exit("Too few command line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command line arguments")
    # checking if it is a python file
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")

def check_comment_or_empty_line(line):
    if line.isspace():
        return True
    # we use the "lstrip" to remove the space and "startwith" to check if the line start with # so we don't count that line
    if line.lstrip().startswith("#"):
    # we wont count it so we write "return True"
        return True
    # otherwise if we pass this test then we "return False"
    return False

if __name__ == "__main__":
    main()
