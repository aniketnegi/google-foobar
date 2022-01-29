'''
The latest gossip in the henchman breakroom is that "LAMBCHOP" stands for "Lambda's Anti-Matter Biofuel Collision Hadron Oxidating Potentiator".
You're pretty sure it runs on diesel, not biofuel, but you can at least give the commander credit for trying.
'''
'''
for i in xs:
        if i in [1, 0]:
            print(max_product)
            return
        else:
            max_product *= i
    print(max_product)
'''
'''def solution(xs: list):  # sourcery skip: remove-str-from-print
    import math

    xs = sorted([int(math.fabs(x)) for x in xs])[::-1]
    max_product = xs[0] if len(xs) == 1 else list(filter(lambda x: x != 0, xs)) # [0,0,0,0,0,0,0], [1,1,1,1,1,1,1]
    
    print((max_product))

solution([-1,0,2,2,3,0,-2,3,-3,0,0,0,1])


def solution(xs: list):
    import math
    sorted_list = sorted([int(math.fabs(x)) for x in xs], reverse=True)
    max_product = sorted_list[0]
    for i in range(1, len(sorted_list)-1):
        if sorted_list[i] != 0:
            max_product *= sorted_list[i]
    print(str(max_product))

listx = [0,-1]
solution(listx)
'''

# Possible Cases:
# 1. All positive: [1,2,3,4,5,6,7,8,9]
# 2. All negative: [-1,-2,-3,-4,-5,-6,-7,-8,-9]
# 3. Mixed: [1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9]
# 4. Zero: [0,0,0,0,0,0,0,0,0]
# 5. One: [1,0,0,0,0,0,0,0,0]
# 7. Mixed_with_zero: [1,2,3,4,5,6,7,8,9,0,0,0,0,0,0,0,0,0]
# 8. One_Zero: [0]
# 9. Zero_One: [1,0]
# 10. Minus-One_Zero: [-1,0]
# 11. Negative_Zero: [-0]
# 12. Minus_One_Minus_One: [-1,-1]
# 13. Minus_One: [-1]

'''
Write a function solution(xs) that takes a list of integers and returns the maximum product of some non-empty subset of those numbers. 
So for example, if an array contained panels with power output levels of [2, -3, 1, 0, -5], then the maximum product would be found by taking 
the subset: xs[0] = 2, xs[1] = -3, xs[4] = -5, giving the product 2*(-3)*(-5) = 30. So solution([2,-3,1,0,-5]) will be "30".
'''
# Using Dictionaries

'''
def solution(xs: list):
    from collections import Counter

    count = Counter(xs)
    
    if len(count) == 1:
        return xs[0]
    
    xs.sort()
    
    max_product = 1
    no_of_negatives = 0

    # Count the number of negatives
    for key, value in count.items():
        if key < 0:
            no_of_negatives += value

    for key, value in count.items():
        if key > 0:
            max_product *= (key**value) 
    else:
        if 
    if max_product == 1:
        
    
    return max_product

list = [-1,-2,-3,-4,-5,-6,-7,-8,-9]
print(solution(list))
'''