for i in range(0, 10):
    for j in range(i + 1, 10):
        if i == 8 and j == 9:  # The last combination
            print("{}{}".format(i, j))
        else:
            print("{}{}".format(i, j), end=', ')
