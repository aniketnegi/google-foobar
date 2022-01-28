'''
The latest gossip in the henchman breakroom is that "LAMBCHOP" stands for "Lambda's Anti-Matter Biofuel Collision Hadron Oxidating Potentiator".
You're pretty sure it runs on diesel, not biofuel, but you can at least give the commander credit for trying.
'''


def solution(xs: list):
    import math
    max_product = 1
    xs = sorted([int(math.fabs(x)) for x in xs])[::-1]
    for i in xs:
        if i in [1, 0]:
            print(str(max_product))
            return
        else:
            max_product *= i
    print(str(max_product))

solution([0])