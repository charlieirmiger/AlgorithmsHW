nr_blocks = 10
pts_per_block = 3
nr_elements = 6 
distinct = 2
blks_with_point = 5



def is_complete(blocks):
    for blk in range(nr_blocks):
        for i in range(pts_per_block):
            if blocks[blk][i] == 0:
                return False
    return True

def is_valid(blocks): 
    for blk in range(nr_blocks):
        for i in range(pts_per_block):
            for j in range(i+1, pts_per_block):
                if blocks[blk][i] == 0:
                    continue
                if blocks[blk][i] == blocks[blk][j]:
                    print("FAIL duplicates")
                    return False
                    #duplicate in block
        print("PASS duplicates")
    for point in range(1, nr_elements+1):
        point_count = 0
        for blk in range(nr_blocks):
            for i in range(pts_per_block):
                if blocks[blk][i] == point:
                    point_count = point_count+1
                    if point_count > blks_with_point:
                        print("FAIL num of blocks")
                        return False
                        #too many blocks with point
        print("PASS num of blocks")
    for point1 in range(1, nr_elements+1):
        for point2 in range(point1+1, nr_elements+1):
            pair_count = 0
            for blk in range(nr_blocks):
                for i in range(pts_per_block):
                    for j in range(i+1, pts_per_block):
                        if blocks[blk][i] == point1 and blocks[blk][j] == point2:
                            pair_count = pair_count+1
                        if blocks[blk][i] == point2 and blocks[blk][j] == point1:
                            pair_count = pair_count+1
                        if pair_count > distinct:
                            print("FAIL pairs")
                            return False
                            #too many pairs
        print("PASS pairs")
    return True


def find_first_empty(blocks):
    for blk in range(nr_blocks):
        for i in range(pts_per_block):
            if blocks[blk][i] == 0:
                return blk, i


def bibd(blocks):
    if is_complete(blocks):
        return blocks
    blk, i = find_first_empty(blocks)
    for num in range(1,nr_elements+1):
        blocks[blk][i] = num
        if is_valid(blocks):
            result = bibd(blocks)
            if is_complete(result):
                return result
        blocks[blk][i] = 0
    return blocks

blocks = [ pts_per_block*[0] for _ in range(nr_blocks) ]

print(blocks)
print(bibd(blocks))
