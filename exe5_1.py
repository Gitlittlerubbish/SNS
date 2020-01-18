#! usr/bin/python3


def max_value(n):
    max = n[0]
    for num in n[1:]:
        if num > max:
            max = num

    return max


def main():
    n = [1, 5, 7, 9, 12, 0]
    ans = max_value(n)

    print(ans)


if __name__ == "__main__":
    main()
