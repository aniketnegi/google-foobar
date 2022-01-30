# Question
'''
Given a list of elevator versions represented as strings, write a function solution(l) that returns the same list sorted in ascending order by major, minor, and revision number 
so that you can identify the current elevator version.
'''


def solution(l):
    # return sorted(l, key=lambda x: (int(x.split('.')[0]), int(x.split('.')[1]), int(x.split('.')[2])))
    return sorted(l, key=lambda x: [int(i) for i in x.split('.')])
        

# Test
test_list = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
print(
      solution(test_list)
     )