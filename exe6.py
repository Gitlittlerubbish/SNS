#! usr/bin/python3
import csv


def read_wireshark(file_name):
    rt_dict = {}
    with open(file_name) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        ids = []
        sources = []
        destinations = []
        protocols = []
        lengths = []
        infos = []

        for row in readCSV:
            identity = row[0]
            source = row[2]
            destination = row[3]
            protocol = row[4]
            length = row[5]
            info = row[6]

            ids.append(identity)
            sources.append(source)
            destinations.append(destination)
            protocols.append(protocol)
            lengths.append(length)
            infos.append(info)

        rt_dict["id"] = ids[1:]
        rt_dict["source"] = sources[1:]
        rt_dict["destination"] = destinations[1:]
        rt_dict["protocol"] = protocols[1:]
        rt_dict["length"] = lengths[1:]
        rt_dict["info"] = infos[1:]

        return rt_dict


def main():
    file_name = "ws.csv"
    rt_dict = read_wireshark(file_name)
    flow_dict = {}  # flow   >>> length

    for i in range(len(rt_dict["id"])):
        # for i in range(7):
        if rt_dict["protocol"][i] == "TCP":
            length = int(rt_dict["length"][i])  # length

            # port & ip
            info = rt_dict["info"][i]
            if info[0].isdigit():
                split_info = info.split(' ', 5)
                sport = split_info[0]
                dport = split_info[4]
            else:
                split_info = info.split(']')[1].split(' ', 6)
                sport = split_info[1]
                dport = split_info[5]

            sip = rt_dict["source"][i]
            dip = rt_dict["destination"][i]
            flow = sip + ":" + sport + " > " + dip + ":" + dport

            if flow in flow_dict:
                flow_dict[flow] += length
            else:
                flow_dict[flow] = length

    for flow, length in flow_dict.items():
        print("Flow:", flow, "\t\t\tLength", length)


if __name__ == "__main__":
    main()
