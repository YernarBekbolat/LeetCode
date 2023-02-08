def maxProfit(prices):
    l = 1
    r = len(prices) - 1
    mini = maxi = 0 

    while l <= r:
        if prices[l] - mini > maxi:
            maxi = prices[l] - mini

        if prices[l] < mini:
            mini = prices[l]

        l += 1

    return maxi