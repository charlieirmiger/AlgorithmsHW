#determines max subarray in given array
class Subarray(object):
    def maxsub(self, arr):
        first_max = 0
        second_max = 0
        for i in range(len(arr)):
            first_max = first_max + arr[i]
            if second_max < 0:
                second_max = 0
            if first_max < second_max:
                first_max = second_max
        return first_max

    def final(self, arr, target):
        value1 = 0
        value2 = 0
        for i in range(len(arr)):
            value1 = value1 + arr[i]
            if value1 > target:
                return value2
            else:
                value2 = value1
        return value2

obj = Subarray()
arr1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(obj.maxsub(arr1))

arr2 = [1,3,5,1,6,1]
print(obj.final(arr2, 11))
