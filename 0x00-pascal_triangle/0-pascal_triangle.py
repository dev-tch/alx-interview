"""module with one function pascal_triangle """


def pascal_triangle(n):
    """ print pascal triangle """
    myList = []
    if n <= 0:
        return myList
    for i in range(0, n):
        row = [0] * (i + 1)
        row[0] = 1
        row[-1] = 1
        if i >= 2:
            for j in range(1, i):
                row[j] = myList[-1][j-1] + myList[-1][j]
        myList.append(row)
    return myList
