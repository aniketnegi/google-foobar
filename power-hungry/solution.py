# Question
'''
Write a function solution(xs) that takes a list of integers and print( the maximum product of some non-empty subset of those numbers. 
So for example, if an array contained panels with power output levels of [2, -3, 1, 0, -5], then the maximum product would be found by taking 
the subset: xs[0] = 2, xs[1] = -3, xs[4] = -5, giving the product 2*(-3)*(-5) = 30. So solution([2,-3,1,0,-5]) will be "30".
'''
def solution(xs):
    from collections import Counter
    count = Counter(xs)
    max_output = 1

    for number in xs:
        if number != 0: max_output *= number

    if max_output < 0:
        if max(xs) != 0 and len(xs) > 1:
            negatives = [x for x in xs if x < 0]
            max_output //= max(negatives)
        elif len(count) == 2:
            max_output = 0
    
    if len(count) == 1:
        max_output = xs[0]**len(xs)
        if max_output < 0 and len(xs) > 1:
            max_output //= xs[0]

    return str(max_output)
