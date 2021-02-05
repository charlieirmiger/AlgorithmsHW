#Programming Assignment #2 - Charlie Irmiger - 9/11/2020

#bin counter has time complexity of O(n)
def bin_counter(n):
    count = 0
#    print("int form: "+str(n))
    n = int(n)
#    print("Binary form: "+str(bin(n)))
    n = n % 2**64
    bin_val = str(bin(n))
    for i in range(2, len(bin_val)):
        #print(bin_val[i])
        if bin_val[i] == '1':
            count += 1
    return count

#Time complexity = O(n) since one loop for length of n
def bit_invert(n):
    n = int(n) % 2**64
    n = bin(n)
#    print(n)
    arr = []
    for i in range(2, len(n)):
        if n[i] == '1':
            arr.append(0)
        else:
            arr.append(1)
    return arr

def valid_sudoku(arr):
    #There should be no non-zero duplicates in any row or column or 3x3
    #Got the code for inputing whole 2D arrays from python interview book
    #Error checking doesn't quite work, breaks instead of returning false
    
    if len(arr) != 9 and len(arr[0]) != 9:
        return False
    for i in range(9):  #each row and column
        temp_arr = []
        for j in range(9):
            temp_arr.append(arr[j][i])
        if not valid_chunk(temp_arr):
            return False
        if not valid_chunk(arr[i]):
            return False

    for x in range(0,9,3):
        for y in range(0,9,3):
            temp_arr2 = []
            for a in range(3):
                for b in range(3):
                    temp_arr2.append(arr[a+x][b+y])
            if not valid_chunk(temp_arr2):
                return False
    return True
        
#check_dupes takes a list of 9 ints and returns false if there are any non-zero duplicates 
def valid_chunk(chunk):
    temp_arr = []
    if len(chunk) != 9:
        return False
    else:
        for i in range (9):
            if chunk[i] not in temp_arr:
                if chunk[i] != 0:
                    temp_arr.append(chunk[i])
            else:
                return False
    #print(temp_arr)
    return True
                

value = input("Enter an int: ")
print("Number of ones in binary representation = " + str(bin_counter(value)))
value2 = input("Enter int to invert: ")
print(bit_invert(value2))
valid_row = [1, 2, 3, 4, 5, 6, 7, 8, 9]
valid_row2 = [1, 0, 3, 0, 5, 0, 7, 8, 9]
valid_row3 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
non_valid = [1, 1, 2, 3, 4, 5, 6, 7, 8]
non_valid2 = []
non_valid3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


print(input("Press enter to contine:"))

#print(valid_chunk(valid_row))
#print(valid_chunk(valid_row2))
#print(valid_chunk(non_valid))
#print(valid_chunk(non_valid2))
#print(valid_chunk(non_valid3))
#print(valid_chunk(valid_row3))
print("====== SUDOKUS ======")

sudoku1 = [[0, 5, 0, 0, 0, 8, 0, 4, 0],     #should be true
           [0, 4, 0, 3, 0, 0, 0, 7, 0],
           [0, 3, 1, 7, 2, 0, 8, 9, 0],
           [3, 0, 0, 0, 0, 0, 7, 8, 0],
           [0, 0, 5, 0, 0, 0, 1, 0, 0],
           [0, 6, 2, 0, 0, 0, 0, 0, 3],
           [0, 2, 6, 0, 4, 7, 9, 3, 0],
           [0, 8, 0, 0, 0, 6, 0, 2, 0],
           [0, 9, 0, 8, 0, 0, 0, 1, 0]]

sudoku2 = [[9, 9, 9, 9, 9, 9, 9, 9, 9],     #should be false
           [1, 2, 3, 4, 5, 6, 7, 8, 9],
           [1, 2, 3, 4, 5, 6, 7, 8, 9],
           [1, 2, 3, 4, 5, 6, 7, 8, 9],
           [1, 2, 3, 4, 5, 6, 7, 8, 9],
           [1, 2, 3, 4, 5, 6, 7, 8, 9],
           [1, 2, 3, 4, 5, 6, 7, 8, 9],
           [1, 2, 3, 4, 5, 6, 7, 8, 9],
           [1, 2, 3, 4, 5, 6, 7, 8, 9]]

sudoku3 = [[3, 5, 0, 0, 0, 8, 0, 4, 0],     #should be false, two 3s in col1
           [0, 4, 0, 3, 0, 0, 0, 7, 0],
           [0, 3, 1, 7, 2, 0, 8, 9, 0],
           [3, 0, 0, 0, 0, 0, 7, 8, 0],
           [0, 0, 5, 0, 0, 0, 1, 0, 0],
           [0, 6, 2, 0, 0, 0, 0, 0, 3],
           [0, 2, 6, 0, 4, 7, 9, 3, 0],
           [0, 8, 0, 0, 0, 6, 0, 2, 0],
           [0, 9, 0, 8, 0, 0, 0, 1, 0]]

sudoku4 = [[1, 5, 0, 0, 0, 8, 0, 4, 0],     #should be false, two 1s in grid 1
           [0, 4, 0, 3, 0, 0, 0, 7, 0],
           [0, 3, 1, 7, 2, 0, 8, 9, 0],
           [3, 0, 0, 0, 0, 0, 7, 8, 0],
           [0, 0, 5, 0, 0, 0, 1, 0, 0],
           [0, 6, 2, 0, 0, 0, 0, 0, 3],
           [0, 2, 6, 0, 4, 7, 9, 3, 0],
           [0, 8, 0, 0, 0, 6, 0, 2, 0],
           [0, 9, 0, 8, 0, 0, 0, 1, 0]]

sudoku5 = [[0, 0, 0, 0, 0, 0, 0, 0, 0],     #should be true, all zeros
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0]]

sudoku6 = [[0, 0, 0, 0, 0, 0, 0, 0, 0],     #should be true
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 1, 2, 3],
           [0, 0, 0, 0, 0, 0, 4, 5, 6],
           [0, 0, 0, 0, 0, 0, 7, 8, 9]]

sudoku7 = [[0, 0, 0, 0, 0, 0, 0, 0, 0],     #should be false
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 1, 2, 3],
           [0, 0, 0, 0, 0, 0, 4, 5, 2],
           [0, 0, 0, 0, 0, 0, 7, 8, 9]]




print(valid_sudoku(sudoku1))
print(valid_sudoku(sudoku2))
print(valid_sudoku(sudoku3))
print(valid_sudoku(sudoku4))
print(valid_sudoku(sudoku5))
print(valid_sudoku(sudoku6))
print(valid_sudoku(sudoku7))

print(input("Press enter to exit:"))
