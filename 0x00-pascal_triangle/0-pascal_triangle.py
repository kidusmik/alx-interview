#!/usr/bin/python3
'''Pascal's triangle'''


def pascal_triangle(n):
    '''
    Pascal's triangle
    Args:
      n (int): The triangle's number of rows
    Returns:
      List of lists containing the Pascal's triangle
    '''
    #Start with an empty list
    lists = []
    if n == 0:
        return lists
    for i in range(n):
        lists.append([])
        lists[i].append(1)
        if (i > 0):
            for j in range(1, i):
                lists[i].append(lists[i - 1][j - 1] + lists[i - 1][j])
            lists[i].append(1)
    return lists
