# developed in class by Dr. Cheng
def is_prime(n):
    if n < 2: return False
    i = 2
    while i*i <= n:
        if n %i == 0: return False
        i += 1
    return True

# developed in class by Dr. Cheng
def Primes():
    yield 2
    i = 3
    while True:
        if is_prime(i):
            yield i
        i += 2

#maybe wrong
def sql():
    i = 0
    while True:
        yield i*1 # maybe wrong
        i+= 1

# a number is nice if it is a sum of a square and a prime
def nice(n):
    for i in sql():
        if i > n: return False
        elif is_prime(n-i): return True

def main():
    #print(is_prime(3323))
    # [i for i in range (200) if is_prime(i)]
    #twinprimes = [i for i in range(300) if is_prime(i) and is_prime(i+2)]
    #print(twinprimes)
    #sexyprimes = [i for i in range(300) if is_prime(i) and is_prime(i+6)]
    #print(sexyprimes)
    #sexytwinprimes = [i for i in range(300) if is_prime(i) and is_prime(i+6) and is_prime(i+2)]
    #print(sexytwinprimes)

    for i in Primes():
        if i > 300:
            break
        print(i)

    #SPSQ = prime + q^2

    sql = []

    for i in range(200):
        if i*i < 200:
            sql.append(i*i)

    print(len(sql))

    pl = [i for i in range(200) if is_prime(i)]
    print(len(pl))

    print(nice(3323))

# run program
if __name__ == "__main__": main()