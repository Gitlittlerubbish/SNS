#! usr/bin/python3
# __author__ = "Littlerubbish"

from math import inf
from exe7_1 import Network

class Tree(Network):

    def __init__(self, net_nest_list, root):
        super().__init__(net_nest_list)
        self.root = root
        
    def description(self):
        return f"This tree's nested list is {self.net_list}"

    def calc(self):
        num = len(self.net_list[self.root])

        depth = -inf
        for i in range(num):
            tmp_depth = self.Dijkstra(self.root, i)["distance"]
            if tmp_depth > depth:
                depth = tmp_depth

        return depth


def main():
    my_net_list = [
        [0,   2,   inf, 1,   inf, inf],
        [2,   0,   3, inf,   inf, inf],
        [inf,   3,   inf, inf,   inf,     inf],
        [1,   inf,   inf, 0,   1,   inf],
        [inf, inf, inf, 1,   0,     2],
        [inf, inf, inf, inf, 2,     0]
    ]
    root = 4

    my_tree = Tree(my_net_list, root)

    # print the tree's depth
    print("The depth of the tree is: ", my_tree.calc())


if __name__ == "__main__":
    main()
