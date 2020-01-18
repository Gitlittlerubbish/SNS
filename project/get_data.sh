#! /bin/sh

# University College of London
# This is a script of SNS to get the <IP address, throughput> pair.
#
# $Author$: Chen Xiao<uceeheh@ucl.ac.uk>
# $Date$: 18/01/2020

rm -f logfile

cat chenxiao.icon
echo "|        \033[31mFetching <IP, Throughput> Script v0.0.1\033[0m       |"
echo "|           $ \033[34mChen Xiao \033[0m <uceeheh@ucl.ac.uk> $         |"
echo "\n\nTHIS MAY TAKE A WHILE, PLEASE BE PATIENT WHILE THE SCRIPT IS RUNNING..."

printf "["
for i in {0..59}
do	
	printf "▓"
	wget --append-output=logfile  -O /dev/null www.google.com
done;
#echo $?;

echo "]\nFinished!";
