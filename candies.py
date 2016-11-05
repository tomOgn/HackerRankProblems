def sumCandies(c, n):
    candies = [1] * n
    for i in range(1, n):
        if c[i] > c[i - 1]:
            candies[i] = candies[i - 1] + 1
    for i in range(n - 2, -1, -1):
        if c[i] > c[i + 1] and candies[i] <= candies[i + 1]:
            candies[i] = candies[i + 1] + 1
    return sum(candies)

n = int(input())
c = []
for _ in range(n):
    c.append(int(input()))
print(sumCandies(c, n))