#sodoku backtracking assignment using recursion
def valid_so_far(matrix, config):
    #Checks; (1. No two numbers next to each other (2. each area has no repeats and < n
    for col in range(6):
        for row in range(6):                                                    #checks every square in matrix
            for i in range(-1, 2):
                for j in range(-1, 2):                                          #checks 3x3 around each square  
                    if col+i >= 0 and col+i < 6 and row+j >=0 and row+j < 6:    #not outside of matrix
                        if not (i == 0 and j == 0):                             #doesnt comapre space to itself
                            if matrix[col+i][row+j] == matrix[col][row] and matrix[col][row] != 0:
                                #print(str(col+i)+" : "+str(row+j))
                                #print(matrix[col][row])
                                #print(matrix[col+i][row+j])
                                return False
    
    for color in range(len(config)):
        array = []
        for square in config[color]:
            if matrix[square[0]][square[1]] != 0:
                if matrix[square[0]][square[1]] in array or matrix[square[0]][square[1]] > len(config[color]):
                    return False
                else:
                    array.append(matrix[square[0]][square[1]])
        #print(array)
    return True

def done(matrix):
    #Checks no zero cells left
    for i in matrix:
        if 0 in i:
            return False
    return True

def find_empty(matrix):
    #Returns coords of first cell with 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                return i,j

def backtrack(matrix, config):
    #print(matrix)
    if done(matrix):
        return matrix
    x, y = find_empty(matrix)
    for i in range(1, len(config)+1):
        matrix[x][y] = i
        if valid_so_far(matrix, config):
            result = backtrack(matrix, config)
            if done(result):
                #print("hello?")
                return result
        matrix[x][y] = 0
    return matrix
            

configuration = [{(0,0), (1,0), (0,1), (2,0)},
                 {(2,1), (3,1), (3,0), (4,0), (5,0)},
                 {(0,2), (1,1), (1,2), (1,3), (2,2)},
                 {(4,1), (4,2)},
                 {(5,1), (5,2), (5,3), (4,4), (5,4)},
                 {(3,2), (2,3), (3,3), (4,3), (3,4)},
                 {(0,3), (0,4), (0,5), (1,4), (2,4)},
                 {(1,5), (2,5), (3,5), (4,5), (5,5)}]

di = 6
dj = 6
matrix = [[0 for j in range(dj)] for i in range(di)]
matrix_test = [[1 for j in range(dj)] for i in range(di)]
matrix[0][0]=4
matrix[4][0]=5
matrix[2][2]=4
matrix[3][3]=2
matrix[4][3]=3
matrix[4][4]=5
matrix[2][5]=1

#matrix[4][1]=1
#matrix[4][2]=1 

#print(matrix)
#print(done(matrix_test))
#print(find_empty(matrix))
#print(valid_so_far(matrix, configuration))
print("Original Matrix:")
print(matrix)
final = backtrack(matrix, configuration)

print("Solved Matrix:")
print(final)
print(input("any key to exit:"))
