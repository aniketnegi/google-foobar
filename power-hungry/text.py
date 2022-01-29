# Question
'''
Write a function solution(xs) that takes a list of integers and print( the maximum product of some non-empty subset of those numbers. 
So for example, if an array contained panels with power output levels of [2, -3, 1, 0, -5], then the maximum product would be found by taking 
the subset: xs[0] = 2, xs[1] = -3, xs[4] = -5, giving the product 2*(-3)*(-5) = 30. So solution([2,-3,1,0,-5]) will be "30".
'''




def solution(xs):
    from collections import Counter
    count = Counter(xs)
    max_prod = 1

    if len(count) == 1:
        print(str(xs[0]**count[xs[0]]))
        return
    elif len(xs) == 2:
        print(str(max(xs)))
        return

    
    
    xs.sort()
    for i in xs:
        if i != 0:
            max_prod *= i
    
    if max_prod < 1:
        list_of_negatives = [x for x in xs if x < 0]
        max_prod //= max(list_of_negatives)
    

    print(str(max_prod))
    return

# Testing

test_list = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
solution(test_list)