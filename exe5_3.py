#! usr/bin/python3


def sorted_list(my_list):
    my_list.sort()
    return my_list


def main():
    my_list = [3, 2, 1]
    print(sorted_list(my_list))


if __name__ == "__main__":
    main()
