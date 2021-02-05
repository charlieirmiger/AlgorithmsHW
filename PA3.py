import time
#backtracking assignment using recursion
#bibd:
nr_blocks = 10      #b
pts_per_block = 3   #k
nr_elements = 6     #v
distinct = 2        #l
blks_with_point = 5 #r

def is_complete(blocks):                        #checks for any 0s
    for blk in range(nr_blocks):
        for i in range(pts_per_block):
            if blocks[blk][i] == 0:
                return False
    return True

def is_valid(blocks, num):
    for i in range(1, nr_elements+1):           #checks l
            #print(str(i)+" : "+str(j))
        count = 0
        for blk in blocks:
            if not i == num and i in blk and num in blk:
                count += 1
                    #print(count)
            if count > distinct:
                #print("Failed l")
                return False
    count = 0        
    for blk in blocks:
        if num in blk:
            count +=1
    if count > blks_with_point:
        return False
    
    return True

def find_first_free(blocks):
    for blk in blocks:
        for i in range(pts_per_block):
            if blk[i] == 0:
                return blk, i
            
def bibd(blocks):
    if is_complete(blocks):
        return blocks
    bl, i = find_first_free(blocks)
    #print(blocks)
    #print(str(i)+" : "+str(j))
    for num in range(max(bl)+1, nr_elements+1):     #starts at highest value possible
        bl[i] = num
        if is_valid(blocks, num):
            result = bibd(blocks)
            if is_complete(result):
                return result
        bl[i] = 0
    return blocks
    

blocks = [ [0 for i in range(pts_per_block)] for j in range(nr_blocks) ]    #generates empty bibd

#bibd_count = 0
total = time.time()
print("===MAIN BIBD===")
print(bibd(blocks))
#print(blocks)
print("Total time = " + str(time.time() - total) + " seconds")

print("===TESTS===")
bibd1 = [[1,2,3,4], [1,2,3,5], [1,2,6,7], [1,3,6,8], [1,4,5,6],     #good bibd
         [1,4,7,8], [1,5,7,8], [2,3,7,8], [2,4,5,7], [2,4,6,8],
         [2,5,6,8], [3,4,5,8], [3,4,6,7], [0,0,0,0]]

bibd2 = [[1,2,3,4], [1,2,3,5], [1,2,6,7], [1,3,6,8], [1,4,5,6],     #bad v
         [1,4,7,8], [1,5,7,8], [2,3,7,8], [2,4,5,7], [2,4,6,8],
         [2,5,6,8], [3,4,5,8], [3,4,6,7], [3,5,6,9]]

bibd3 = [[1,2,3,4], [1,2,3,5], [1,2,6,7], [1,3,6,8], [1,4,5,6],     #bad r
         [1,4,7,8], [1,5,7,8], [2,3,7,8], [2,4,5,7], [2,4,6,8],
         [2,5,6,8], [3,4,5,8], [3,4,6,7], [3,5,6,8]]

bibd4 = [[1,2,3,4], [1,2,3,5], [1,2,6,7], [1,3,6,8], [1,4,5,6],     #bad l
         [1,4,7,8], [1,5,7,8], [2,3,7,8], [2,4,5,7], [2,4,6,8],
         [2,5,6,8], [3,4,6,7], [3,4,6,7], [3,5,5,8]]

print(bibd(bibd1))
print(bibd(bibd2))
print(bibd(bibd3))
print(bibd(bibd4))

print(bibd(bibd1))


        
