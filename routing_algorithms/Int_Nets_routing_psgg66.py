import numpy as np
from itertools import permutations

# takes source and destination nodes and returns list of nodes
# and ending with the destination detailing the route provided
def star5_routing(source, destination):

    # initialise route and current node
    route = [source]
    current_node = source.copy()
    node_length = len(current_node)

    # keep routing until the destination is reached
    while current_node != destination:

        # check what digit must be swapped
        for index in range(0, node_length):

            if index == 0:

                # not equal means they should be swapped
                if current_node[index] != destination[index]:

                    # get digit and find its index in destination
                    digit = current_node[index]
                    destination_digit_index = destination.index(digit)

                    # swap
                    current_node[index], current_node[destination_digit_index] =\
                        current_node[destination_digit_index], current_node[index]

                    break

            # not equal means they should be swapped
            if current_node[index] != destination[index]:

                current_node[0], current_node[index] = current_node[index], current_node[0]
                break

        route.append(current_node.copy())

    return route


# simulates the all-to-all traffic pattern to determine cumulative channel loads
def simulate_traffic():

    # generate the nodes of S5 and initialise channel loads matrix
    nodes = list(permutations([i for i in range(1, 6)]))
    nodes = [list(node) for node in nodes]
    channel_loads_matrix = np.zeros((120, 120))

    



simulate_traffic()

"""
route = star5_routing([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
for node in route:
    print(node)
"""
