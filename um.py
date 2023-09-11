import re


def main():
    print(count(input("Text: ")))


def count(s):
    um_repetition = re.findall(r'\bum\b', s, re.IGNORECASE)
    return len(um_repetition)


if __name__ == "__main__":
    main()