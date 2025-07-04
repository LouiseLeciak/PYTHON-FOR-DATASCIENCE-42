import sys
from ft_filter import ft_filter


def main():
    try:
        if (len(sys.argv) != 3):
            raise AssertionError("wrong number of arguments")
        elif not sys.argv[2].isdigit():
            raise AssertionError("second argument must be a number")

        N = int(sys.argv[2])
        S = sys.argv[1].split()
        # lambda c;est comme declarer et utiliser une fonction en une ligne
        # fonction lambda qui prend word et return les mot de N ou plus
        filtered = ft_filter(lambda word: len(word) > N, S)
        filtered_list = [word for word in filtered]
        print(filtered_list)

    except AssertionError as e:
        print("AssertionError:", e, file=sys.stderr)


if __name__ == "__main__":
    main()
