
def star5_routing(source, destination):

    path = [source]
    current_node = source

    while current_node != destination:

        if current_node[0] != destination[0]:
            break

        # path.append(next_node)

    return path

star5_routing([1, 2, 3, 4], [4, 3, 2, 1])
