from itertools import permutations

# ============================ STAR GRAPH ROUTING ============================

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

        route.append(current_node.copy())  # append the new node to the route

    return route


# simulates the all-to-all traffic pattern to determine cumulative channel loads
def simulate_traffic():

    # generate the nodes of S5 and initialise channel loads matrix
    nodes = list(permutations([i for i in range(1, 6)]))
    nodes = [list(node) for node in nodes]
    channel_loads_matrix = [[0 for x in range(120)] for y in range(120)] 

    # all-to-all traffic pattern
    for source in nodes:
        for destination in nodes:

            # retrieve indices
            source_index = nodes.index(source)
            destination_index = nodes.index(destination)

            # same source and destination means channel load is zero; remain unchanged
            if source != destination:

                # compute the route b/w source and destination + get pairs of nodes from route
                route = star5_routing(source, destination)
                channels = list(zip(route, route[1:]))

                # update channel loads
                for channel in channels:

                    # retrieve nodes
                    node1, node2 = channel[0], channel[1]
                    node1_index, node2_index = nodes.index(node1), nodes.index(node2)

                    # update values
                    channel_loads_matrix[node1_index][node2_index] += 1

    # printing the loads
    for i in range(0, len(channel_loads_matrix)):
        for channel in range(0, len(channel_loads_matrix)):
            if channel_loads_matrix[i][channel] > 0:
                print("Load on channel from", nodes[i], "to", nodes[channel],\
                    "is", channel_loads_matrix[i][channel])


#simulate_traffic()

#route = star5_routing([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
#for node in route:
#    print(node)


# ============================ DIMENSION ORDER ROUTING ============================

def hypercube_routing(n, source, target):

    # initialise route and current node
    route = [source]
    current_node = source.copy()
    dimension = n - 1

    # keep routing until the target node is reached
    while current_node != target:

        # if bits are equal move to next dimension
        if current_node[dimension] != target[dimension]:

            # flip the bit and update route
            current_node[dimension] = 1 - current_node[dimension]
            route.append(current_node.copy())

        # update dimension
        dimension -= 1

    return route


route = hypercube_routing(8, [1, 0, 0, 1, 1, 0, 1, 0], [0, 1, 1, 0, 0, 0, 0, 1])
for node in route:
    print(node)
