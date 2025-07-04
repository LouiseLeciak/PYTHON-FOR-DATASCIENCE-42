import sys

def count_uppercase(s: str) -> int:
    """
    Counts the number of upper-case characteres
    """
    res = 0
    for i in s:
        if(i.isupper()):
            res += 1
    return (res)

def count_lowercase(s: str) -> int:
    """
    Counts the number of lower-case characteres
    """
    res = 0
    for i in s:
        if(i.islower()):
            res += 1
    return (res)

def count_punctuation(s: str) -> int:
    """
    Count the number of punctuation
    """
    punctuation_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    res = 0
    for i in s:
        if (i in punctuation_chars):
            res += 1
    return (res)

def count_space(s: str) -> int:
    """
    Count the number of space
    """
    res = 0
    for i in s:
        if (i == ' '):
            res += 1
    return res

def count_digit(s: str) -> int:
    """
    Count the number of space
    """
    res = 0
    for i in s:
        if (i.isdigit()):
            res += 1
    return res

def main():
    """
    Main block to print the informations on the inpt
    """
    if (len(sys.argv) > 2):
        print("AssertionError: more than one argument is provided")
        exit(1)
    elif (len(sys.argv) < 2):
        print("What is the text to count?")
        inpt = input()
    else:
        inpt = sys.argv[1]   
   
    result = len(inpt)
    print(f"The text contains {result} characters:")

    result = count_uppercase(inpt)
    print(f"{result} upper letters")

    result = count_lowercase(inpt)
    print(f"{result} lower letters")

    result = count_punctuation(inpt)
    print(f"{result} punctuation marks")

    result = count_space(inpt)
    print(f"{result} spaces")

    result = count_digit(inpt)
    print(f"{result} digits")



if __name__ == "__main__":
    main()