from seasons import check_birthday

def main():
    test_check_birthday()

def test_check_birthday():
    assert check_birthday("2003-08-23") == ("2003", "08", "23")
    assert check_birthday("2003-8-23") == None 
    assert check_birthday("August-23-2003") == None 

if __name__ == "__main__":
    main()

    