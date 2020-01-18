#! usr/bin/python3


def fact(num):
    if num == 1 or num == 0:
        return 1
    return fact(num-1) + fact(num-2)


def main():
    num = 20
    print("Factorial of 20 is ", fact(num))


if __name__ == "__main__":
    main()