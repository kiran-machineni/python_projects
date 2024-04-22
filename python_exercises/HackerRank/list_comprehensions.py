# https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true

def list_comprehensions():
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    all_permutations = []
    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                all_permutations.append([i, j, k])
    print(list(filter(lambda l: sum(l) != n, all_permutations)))

# Sample Input:(x,y,z,n)
# 1
# 1
# 1
# 2

# Sample Output
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
