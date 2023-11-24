def plusMinus(arr):
    pos = 0
    neg = 0
    zeros = 0
    
    if 0 > len(arr) > 100:
        raise ValueError
    
    for i in arr :

        if -100 > i > 100:
            raise ValueError
        
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zeros += 1

    print(f'{pos / len(arr):.6f} \n {neg / len(arr):.6f} \n {zeros / len(arr):.6f}')

plusMinus([-4, 3, -9, 0, 4, 1])