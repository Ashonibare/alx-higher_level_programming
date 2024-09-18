def square_matrixsimple(matrix=[]):
    squared_matrix = []  # empty list to store the sqaured ints

    for row in matrix:  # loop through each row
        squred_row = []  # to store the squared values in rows

        for element in row:  # loops through each int in each row
            squared_row.append(element ** 2)  # square each int, add to list

        squared_matrix.append(squared_row)  # add the items to matrix

    return squared_matrix  # return the new matrix
