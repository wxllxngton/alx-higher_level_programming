#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_matrix = []
    for i in range(len(my_list)):
        new_matrix.append(my_list[i]) if i != search else new_matrix.append(
            replace
        )
    return new_matrix
