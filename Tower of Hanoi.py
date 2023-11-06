import time

# n = number of discs
# moving from rod i to rod j
def towerOfHanoi(n, i, j):
    # piles = [0, 1, 2]
    if (i == 0 and j == 1) or (i == 1 and j == 0):
        a = 2
    if (i == 1 and j == 2) or (i == 2 and j == 1):
        a = 0
    if (i == 0 and j == 2) or (i == 2 and j == 0):
        a = 1

    if n == 1:
        return [i, j]
    return towerOfHanoi(n - 1, i, a) + [i, j] + towerOfHanoi(n - 1, a, j)


start = time.perf_counter()
array = towerOfHanoi(3, 0, 1)
end = time.perf_counter()
result = []
numberOfMoves = 0

for i in range(0, len(array)):
    if i % 2 != 0:
        temp = [array[i - 1], array[i]]
        result.append(temp)
        numberOfMoves += 1

print(result)
print(numberOfMoves)
print(end - start)

