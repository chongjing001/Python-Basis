

prices = [1, 2, 3, 4, 5]
max_liyi = 0
for i in range(len(prices) - 1):
    if prices[i + 1] > prices[i]:
        max_liyi += prices[i + 1] - prices[i]
print(max_liyi)







