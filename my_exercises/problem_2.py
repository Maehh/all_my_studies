import sys
def element_equal(list):
    element = list[0]
    for item in list:
        if element != item:
            return False
    return True
        
def minMaxSum_forequals(value):
    value.pop()
    val_count = 0
    for i in value:
        val_count += i
    return val_count

def miniMaxSum(arr):
    count = 0
    max_count = 0
    min_count = 10**99
    neglected_num = 0

    for i in arr:
        count = 0
        neglected_num = i

        if element_equal(arr):
           result = minMaxSum_forequals(arr)
           print(result, result)
           sys.exit()
            

        for i in arr:

            if (i < 1) or (i > 10**9):
                raise ValueError
            
            if i == neglected_num :
                continue
            count += i

        max_count = max(count, max_count)
        min_count = min(count, min_count)
            
    print(min_count, max_count)

miniMaxSum([1, 2, 3, 4, 5])