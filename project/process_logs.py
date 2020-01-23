#! /usr/bin/python3

# This is the script of processing the logfiles in ./logs/
import os, fnmatch, csv


# process a single logfile, e.g. www.apple.com
def process_single_logfile(filename):
    
    # get the domain name of the current logfile
    rt_dict = dict(domain=filename[15:], ip="", throughput=0.0)

    # open the current logfile and do the following processes
    with open(filename, "r") as logfile:
        wget_times = 0
        sum = 0
        for line in logfile:

            # get the ip address of the current domain
            if line[:10] == "Connecting":
                rt_dict["ip"] = line.split("|")[1].split("|")[0].strip()

            # get speed of each wget and then calculate the throughput of this ip address
            if "- ‘/dev/null’ saved" in line:
                wget_times = wget_times + 1
                # speed format: xxx xb/s
                speed = line.split("(")[1].split(")")[0]
                sum = sum + float(speed.split(" ")[0])

        if wget_times != 0:
            rt_dict["throughput"] = format(sum / wget_times, ".5f")
        else:
            rt_dict["throughput"] = 0
            
    return rt_dict

def main():

    # get all the logfile* in the logs directory
    log_list = fnmatch.filter(os.listdir('./logs'), 'logfile*')
    print(log_list)

    # traverse the log_list and process the logfile
    with open('data.csv', mode='w') as csv_file:
        data_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        data_writer.writerow(['Domain', 'Ip', 'Throughput'])

        # process the current logfile
        for filename in log_list:
            rt_dict = process_single_logfile("./logs/" + filename)
            current_row_list = list(rt_dict.values())
            data_writer.writerow(current_row_list)

if __name__ == "__main__":
    main()
