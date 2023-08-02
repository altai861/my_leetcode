n = int(input(":"))

def climb(n):
    global ways
    ways = 0

    def recurse(cur):
        if cur == n:
            global ways
            ways += 1
        elif cur > n:
            return
        recurse(cur + 1)
        recurse(cur + 2)
    recurse(0)
    return ways

print(climb(n))