#! usr/bin/python3

from math import inf

def main():
	cnt = 3
	a = -inf
	while cnt > 0:
		tmp = int(input("Type an interger:"))
		if tmp > a:
			a = tmp
		cnt = cnt - 1
	print(a)	


if __name__ == "__main__":
	main()
