
def star5_routing(source, destination):

    # initialise path and current node
    path = [source]
    current_node = source
    node_length = len(current_node)

    # keep routing until the destination is reached
    while current_node != destination:

        # check what digit must be swapped
        for index in range(0, node_length):

            if index == 0:

                if current_node[index] != destination[index]:

                    # get digit and find its index in destination
                    digit = current_node[index]
                    destination_digit_index = destination.index(digit)

                    current_node[index], current_node[destination_digit_index] =\
                        current_node[destination_digit_index], current_node[index]
                    
                    break

        print(current_node)
        path.append(current_node)

    return path

star5_routing([1, 2, 3, 4], [4, 3, 2, 1])
