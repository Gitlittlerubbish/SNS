#! usr/bin/python3

dns_dict = { "google.com":"216.239.38.10",
				"ucl.ac.uk":"144.82.250.24",
				"facebook.com":"31.13.90.36"
			}

def main():
	while True:
		cmd = str(input(">"))
		if cmd == "exit":
			break

		if cmd == "printall":
			for k, v  in dns_dict.items():
				print(k + ":" + v)
		else:
			print(cmd + ":" + dns_dict[cmd])


if __name__ == "__main__":
	main()