
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


route = star5_routing([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
for node in route:
    print(node)
