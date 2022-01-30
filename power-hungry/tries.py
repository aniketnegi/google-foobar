# Question
'''
Write a function solution(xs) that takes a list of integers and print( the maximum product of some non-empty subset of those numbers. 
So for example, if an array contained panels with power output levels of [2, -3, 1, 0, -5], then the maximum product would be found by taking 
the subset: xs[0] = 2, xs[1] = -3, xs[4] = -5, giving the product 2*(-3)*(-5) = 30. So solution([2,-3,1,0,-5]) will be "30".
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

# ======================================================================================================================

'''
def solution(xs: list):  # sourcery skip: remove-str-from-print
    import math

    xs = sorted([int(math.fabs(x)) for x in xs])[::-1]
    max_product = xs[0] if len(xs) == 1 else list(filter(lambda x: x != 0, xs)) # [0,0,0,0,0,0,0], [1,1,1,1,1,1,1]
    
    print((max_product))

solution([-1,0,2,2,3,0,-2,3,-3,0,0,0,1])

'''

# ======================================================================================================================

'''
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

# ======================================================================================================================

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

# ======================================================================================================================

'''
def solution(xs):
    from collections import Counter
    import math
    
    count = Counter(xs)
    max_prod = 1
    list_of_negatives = [x for x in xs if x < 0]
    xs.sort()
    
    if len(count) == 1:
        
        max_prod = ((xs[0]**count[math.fabs(xs[0])]))
        
        if max_prod < 0:
            max_prod //= xs[0]
        print(str(max_prod*(-1)))
        return
    
    elif len(count) == 2:
        for i in xs:
            if i != 0:
                max_prod *= i

        if xs[-1] == 0 and max_prod<0:
            max_prod = 0
        print(str(max_prod))
        return

    
    for i in xs:
        if i != 0:
            max_prod *= i
    

    
    if max_prod < 1:
        max_prod //= max(list_of_negatives)
    

    print(str(max_prod))
    return
'''

# ======================================================================================================================

'''
def solution(xs):
    # handle simple edge cases
    if len(xs) == 0:
        return str(0)
    if len(xs) == 1:
        return str(xs[0])

    # split input into positive/negative lists
    positive_numbers = []
    negative_numbers = []
    for n in xs:
        if n > 0: positive_numbers.append(n)
        elif n < 0: negative_numbers.append(n)

    # cache list counts
    positive_count = len(positive_numbers)
    negative_count = len(negative_numbers)

    # handle single negative panel edge case
    if negative_count == 1 and positive_count == 0:
        return str(0)

    # handle all zeros edge case
    if negative_count == 0 and positive_count == 0:
        return str(0)

    # calculate positive power output
    power_output = 1L
    for n in positive_numbers:
        power_output *= n

    # remove "largest" negative panel in odd arrangements
    if negative_count % 2 == 1:
        negative_numbers.remove(max(negative_numbers))

    # calculate negative power output
    for n in negative_numbers:
        power_output *= n

    return str(power_output)
'''

# ======================================================================================================================

# Final Solution
def solution(xs):
    from collections import Counter
    import math
    count = Counter(xs)
    max_output = 1
    negatives = [x for x in xs if x < 0]

    for number in xs:
        if number != 0: max_output *= number

    if max_output < 0:
        if max(xs) != 0 and len(xs) > 1:
            max_output //= max(negatives)
        elif len(count) == 2:
            max_output = 0
    
    if len(count) == 1:
        max_output = xs[0]**len(xs)
        if max_output < 0 and len(xs) > 1:
            max_output //= xs[0]

    return str(max_output)

# Test
for i in [[-1],[2, 0, 2, 2, 0], [-2, -3, 4, -5], [0, 0, 0, -43], [0, 0], [0, 0, 4], [1000, -1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]]:
    print(i, ' -> ', solution(i))