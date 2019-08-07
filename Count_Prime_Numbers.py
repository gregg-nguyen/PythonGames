def count_primes(num):
    prime = [2]
    x = 3
    while x in range(3,num+1):
        x += 1
        for y in range(2,x):
            if x % y == 0:
                break
        else:
            prime.append(x)
    return len(prime)



