import sys


def main():
    NESTED_MORSE = {    " ": "/ ",
                        "A": ".- ",
                        "B": "-... ",
                        "C": "-.-. ",
                        "D": "-.. ",
                        "E": ". ",
                        "F": "..-. ",
                        "G": "--. ",
                        "H": ".... ",
                        "I": ".. ",
                        "J": ".--- ",
                        "K": "-.- ",
                        "L": ".-.. ",
                        "M": "-- ",
                        "N": "-. ",
                        "O": "--- ",
                        "P": ".--. ",
                        "Q": "--.- ",
                        "R": ".-. ",
                        "S": "... ",
                        "T": "- ",
                        "U": "..- ",
                        "V": "...- ",
                        "W": ".-- ",
                        "X": "-..- ",
                        "Y": "-.-- ",
                        "Z": "--.. ",
                        "0": "----- ",
                        "1": ".---- ",
                        "2": "..--- ",
                        "3": "...-- ",
                        "4": "....- ",
                        "5": "..... ",
                        "6": "-.... ",
                        "7": "--... ",
                        "8": "---.. ",
                        "9": "----. "}
    try:
        if (len(sys.argv) != 2):
            raise AssertionError("wrong number of arguments.")

    except AssertionError as e:
        print("AssertionError:", e, file=sys.stderr)
        return 0
    
    input_txt = sys.argv[1]
    input_txt = input_txt.upper()

    is_valid = True
    for c in input_txt:
        if not (c.isalnum() or c == ' '):
            is_valid = False
            break

    if not is_valid:
        raise AssertionError("must contain only letters, digits or spaces.")
    
    morse_trad = ""
    for char in input_txt:
        morse_trad += NESTED_MORSE[char]

    print(morse_trad)
    return 0


if __name__ == "__main__":
    main()