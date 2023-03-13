def convert(input_string):
    output_string = input_string.replace(':)', '🙂').replace(':(', '🙁')
    return output_string
def main():
    user_input = input(">>>")
    converted_string = convert(user_input)
    print(converted_string)
main()