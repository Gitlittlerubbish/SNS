#! usr/bin/python3
# __author__ == "Littlerubbish"

from math import inf

class Network:

    def __init__(self, net_nest_list):
        self.net_list = net_nest_list

    def description(self):
        return f"This network's nested list is {self.net_list}"

    # return the index of node of the minimum distance && not in the path_list
    def my_net_min(self, source_list, used_list):
        tmp_min = inf
        index = 0

        for i in range(len(source_list)):
            if i not in used_list:
                if source_list[i] < tmp_min:
                    tmp_min = source_list[i]
                    index = i

        return index


    def Dijkstra(self, source, destination):    #pass in source & destination number
        source_list = self.net_list[source]     # list of source to each node
        used_list = [source, ]      # a list of used nodes

        # route from src to all other nodes(list), each sub list only stores the last part of route, 
        # so line50 is needed
        route_nest_list = []
        for i in range(len(source_list)):
            route_nest_list.append([])

        # start of algorithm
        tmp_source_list = source_list
        while len(used_list) < len(source_list):
            next_node = self.my_net_min(tmp_source_list, used_list)   #get the index of the next node
            used_list.append(next_node)

            for i in range(len(source_list)):
                if i not in used_list:
                    if source_list[i] > source_list[next_node] + self.net_list[next_node][i]:
                        source_list[i] = source_list[next_node] + self.net_list[next_node][i] 
                        route_nest_list[i].append(next_node)
        # algorithm ends


        #add the entire routing list to the destination route
        route_list = route_nest_list[destination]
        tmp_list = route_list
        while tmp_list !=[]:
            route_list = route_nest_list[tmp_list[0]] + route_list 
            tmp_list = route_nest_list[tmp_list[0]]

        # return a dictionary as the result with two key-values:route(list) & distance(int)
        route_list.append(destination)
        route_list = [source, ] + route_list
        res_dict = {
            "route" : route_list,
            "distance" : source_list[destination]
        }
        return res_dict


def main():
    # A to F
    # my_net_list = [
    #     [0,   2,   5, 1,   inf, inf],
    #     [2,   0,   3, 2,   inf, inf],
    #     [5,   3,   0, 3,   1,     5],
    #     [1,   2,   3, 0,   1,   inf],
    #     [inf, inf, 1, 1,   0,     2],
    #     [inf, inf, 5, inf, 2,     0]
    # ]
    my_net_list = [
        [0, 5, inf, inf, inf, inf],
        [5, 0, 2, inf, inf, inf],
        [inf, 2, 0, inf, inf, 2],
        [inf, inf, inf, 0, 2, inf],
        [inf,inf, inf, 2, 0, 10],
        [inf, inf, 2, inf, 10, 0]
    ]

    # test from source to destination
    test_net = Network(my_net_list)
    source = 0
    destination = 5
    res_dict = test_net.Dijkstra(source, destination)      


    # ## test for my_net_min
    # print("Test net_min:")
    # print(test_net.my_net_min(my_net_list[0], [0,]))


    # print the routing result
    print("The routing path is: ", chr(source + 65), end='')
    for i in res_dict["route"][1:]:
        print(f"--->{chr(65 + i)}", end='')

    print('\n' + "Distance is: ", res_dict["distance"])
    # end of result print


if __name__ == "__main__":
    main()
