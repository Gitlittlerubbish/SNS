#! /bin/sh
rm -f logfile

for i in {0..59}
do	
	wget --append-output=logfile  -O /dev/null www.google.com
done;
echo $?;
echo "Finished";
