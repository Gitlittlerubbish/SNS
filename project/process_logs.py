#! /usr/bin/python3

# This is the script of processing the logfiles in ./logs/
import os, fnmatch, csv


# process a single logfile, e.g. www.apple.com
def process_single_logfile(filename):
    
    print(f"Processing {filename}.")
    # get the domain name of the current logfile
    rt_dict = dict(domain=filename[15:], ip="", ip_bin="", throughput=0.0, unit="")

    # open the current logfile and do the following processes
    with open(filename, "r") as logfile:
        wget_times = 0
        sum = 0
        for line in logfile:

            # get the ip address of the current domain
            if line[:10] == "Connecting":
                try:
                    ip = line.split("|")[1].split("|")[0].strip()
                    rt_dict["ip"] = ip

                    # get the binary version of the current ip
                    ip_bin = ""
                    for x in ip.split('.'):
                        ip_bin += format(int(x), "08b")
                    rt_dict["ip_bin"] = ip_bin
                except IndexError as e:
                    print(f"{e}!!! Dropping {filename}.")


            # get speed of each wget and then calculate the throughput of this ip address
            if "- ‘/dev/null’ saved" in line:
                try:
                    wget_times = wget_times + 1
                    # speed format: xxx xb/s
                    speed = line.split("(")[1].split(")")[0]
                    sum = sum + float(speed.split(" ")[0])

                    unit = speed.split(" ")[1]
                except IndexError as e:
                    print(f"{e}!!! Dropping {filename}.")

        if wget_times != 0:
            # convert all the speed to Kb/s
            raw_throughput = sum / wget_times
            throughput = 0
            if unit[0] == 'G':
                throughput = raw_throughput * 1024 * 1024
            elif unit[0] == 'M':
                throughput = raw_throughput * 1024
            elif unit[0] == 'K':
                throughput = raw_throughput
                
            rt_dict["throughput"] = format(throughput, ".5f")
            rt_dict["unit"] = "Kb/s"
        else:
            rt_dict["throughput"] = 0
            
    return rt_dict

def main():

    # get all the logfile* in the logs directory
    log_list = fnmatch.filter(os.listdir('./logs'), 'logfile*')
    # print(log_list)

    # traverse the log_list and process the logfile
    with open('data.csv', mode='w') as csv_file:
        data_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        data_writer.writerow(['Domain', 'Ip', 'Ip_bin', 'Throughput', 'Unit'])

        # process the current logfile
        for filename in log_list:
            rt_dict = process_single_logfile("./logs/" + filename)
            if rt_dict["unit"] == "Kb/s":
                current_row_list = list(rt_dict.values())
                data_writer.writerow(current_row_list)

if __name__ == "__main__":
    main()
