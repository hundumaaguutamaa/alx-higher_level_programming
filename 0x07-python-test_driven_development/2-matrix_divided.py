#!/usr/bin/python3

	""" matrix_divided matrix to divide elements by number.

	"""
def matrix_divided(matrix, div):
	"""Returns a new matrix
	Args:
	matrix: list of atrix in integer or float.
	
	""" 
   
    matrix_list = []
    error = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or matrix == [[]] or matrix is None:
        raise TypeError(error)

    
    if isinstance(div, (int, float, type(None))):
        pass


    else:
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    if matrix[0]:
        length = len(matrix[0])

    else:
        raise TypeError(error)
    
    for x in range(len(matrix)):
        if len(matrix[x]) is not length:
            raise TypeError("Each row of the matrix must have the same size")
        
        matrix_list.append([])
        for n in matrix[x]:

            if type(n) is int or type(n) is float:
                matrix_list[x].append(round(n / div, 2))

            else:
                raise TypeError(error)
            
    return matrix_list
