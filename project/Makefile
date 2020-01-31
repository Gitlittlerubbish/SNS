all:
	./get_data.sh
	python3 process_logs.py

process:
	python3 process_logs.py

rmdata:
	rm -f data.csv
clean:
	rm -f ./logs/log* err_domains.txt
