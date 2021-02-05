from random import *
#PA6 - Charlie Irmiger
#Linear hashing addressing assignment
#given number of buckets, split pointer, and level, insert 10000 random records 100 times
#calculate average number of records per bucket

def address(key, level, split):
    if key % 2**level < split:
        return key % 2**(level+1)
    else:
        return key % 2**level

def main():
    results = [[] for _ in range(150)]
    for run in range(50):
        buckets = 150
        level = 7
        split = 22
    
        hash_table = [0]*150
        
        for _ in range(10000):
            key = getrandbits(32)
            #print(x)
            add = address(key, level, split)
            
            hash_table[add] += 1

        for i in range(150):
            results[i].append(hash_table[i])
        
    for i in results:
        for j in i:
            print(j, end='\t')
        print()



main()
input("  ")

