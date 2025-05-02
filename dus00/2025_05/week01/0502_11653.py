def prime_factorization(n):
    i = 2
    while n > 1:
        if n % i == 0:
            print(i)
            n //= i
        else:
            i += 1

if __name__ == "__main__":
    num = int(input())
    prime_factorization(num)
