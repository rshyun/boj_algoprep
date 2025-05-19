import math

def gcd(a, b):
    T = int(input())

    for _ in range(T):
        a, b = map(int, input().split())
        lcm = a * b // math.gcd(a, b)
        print(lcm)

if __name__ == "__main__":
    gcd(1, 1)
