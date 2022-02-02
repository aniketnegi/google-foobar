# Question
'''
Write a function solution(M, F) where M and F are the number of Mach and Facula bombs needed. Return the fewest number of generations (as a string) that need to pass before 
you'll have the exact number of bombs necessary to destroy the LAMBCHOP, or the string "impossible" if this can't be done!
'''
def solution(x, y):
    M, F = max(int(x), int(y)), min(int(x), int(y))
    result = 0
    while F > 0:
        result += M // F
        M, F = F, M % F
    if M != 1:
        return "impossible"
    return str(result - 1)

         

# Test
x, y = '7', '4'
print(solution(x, y))