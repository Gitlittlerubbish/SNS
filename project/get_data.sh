#! /bin/sh

# University College of London
# This is a script of SNS project's first step to get the <IP address, throughput> pair.
# It generates all the wget logfiles in the ./logs/ for process_logs.py to use.
#
# $Author$: Chen Xiao<uceeheh@ucl.ac.uk>
# $Date$: 18/01/2020

VERSION="0.0.2"
rm -f logfile*

cat chenxiao.icon
echo "|        \033[33mFetching <IP, Throughput> Script V$VERSION\033[0m       |"
echo "|           $ \033[34mChen Xiao \033[0m <uceeheh@ucl.ac.uk> $         |"
echo "\n\nTHIS MAY TAKE A WHILE, PLEASE BE PATIENT WHILE THE SCRIPT IS RUNNING..."

input="./domains.txt"

errflag=0
while IFS= read -r line
do	
	errflag=0
	printf "%-20s" $line":"
	printf "["
	# 40 times of wget, considering the initial congestion window size is 10
	for idx in {0..39}
	do
		printf "▓"
		wget -4 --tries=1 --connect-timeout=3 --report-speed=bits --append-output=./logs/logfile"_$line"  -O /dev/null $line
		if [ $? != 0 ]
		then
			echo "\n\033[31m"$line" connection failed, go to the next domain.\033[0m"
			echo "$line" >> err_domains.txt
			errflag=1
			break
		fi
	done;

	if [ $errflag == 0 ]
	then
		echo "]"
	fi
done < "$input"

echo "\nFinished!";
