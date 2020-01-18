#! usr/bin/python3 

year_dict = { "1":31, "2":29, "3":31, "4":30, "5":31, 
			"6":30, "7":31, "8":31, "9":30, 
			"10":31, "11":30, "12":31
			}


def main():
	month = str(input("Type a number of month:"))
	year = int(input("Type a number of year:"))
	
	if year % 4 == 0 and year % 100 != 0 and int(month) == 2:
		print(year_dict[month])
	elif int(month) == 2:
		print(year_dict[month] - 1)
	else:
		print(year_dict[month])


if __name__ == "__main__":
	main()
