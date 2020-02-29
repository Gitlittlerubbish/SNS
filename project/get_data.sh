#! /bin/bash

# University College of London
# This is a script of SNS project's first step to get the <IP address, throughput> pair.
# It generates all the wget logfiles in the ./logs/ for process_logs.py to use.
#
# $Author$: Chen Xiao<uceeheh@ucl.ac.uk>
# $Date$: 18/01/2020

VERSION="0.0.3"
rm -f logfile*

cat chenxiao.icon
echo -e "|        \033[33mFetching <IP, Throughput> Script V$VERSION\033[0m       |"
echo -e "|           $ \033[34mChen Xiao \033[0m <uceeheh@ucl.ac.uk> $         |"
echo -e "\n\nTHIS MAY TAKE A WHILE, PLEASE BE PATIENT WHILE THE SCRIPT IS RUNNING..."

input="./pdfurlfinal.txt"

errflag=0
while IFS= read -r line
do	
	errflag=0

	#added
	temp=${line#*//}
	domain=${temp%%/*}

	printf "Processing "$temp"\n"

	# Considering TCP slow start, all wget items are pdfs
	wget -4 --tries=1 --timeout=3 --report-speed=bits --append-output=./logs/logfile"_$domain" -O /dev/null $temp
	if [ $? != 0 ]
	then
		echo -e "\033[31m"$temp" connection failed, go to the next domain.\033[0m"
		rm -f ./logs/logfile"_$domain"
		echo "$line" >> err_domains.txt
	fi

done < "$input"

echo "\nFinished!";
