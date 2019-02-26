def sieve(n):
    if n < 3:
        return False
    
    prime = []
    nums = [True for i in range(n+1)]
    p = 2

    while p**2 <= n:
        if nums[p] == True:
            for i in range(p * 2, n+1, p):
                nums[i] = False
        p += 1

    for j in range(n + 1):
        if nums[j] == True:
            prime.append(j)

    return prime

print(sieve(20))