n = int(input("n: "))

def climbingStairs(n):
    global result
    result = 0
    def recursive(current_climbed_stairs):
        if current_climbed_stairs == n:
            global result
            result += 1
            return
        elif current_climbed_stairs > n:
            return
    
        recursive(current_climbed_stairs + 1)
        recursive(current_climbed_stairs + 2)
    
    recursive(0)
    return result

def climbing_stairs_efficient(n):
    if n <= 2:
        return n
    dp = [i + 1 for i in range(n)]
    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[-1]


print(climbing_stairs_efficient(n))

