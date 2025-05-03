import sys

def twopointer(arr, target):
    arr.sort()
    cnt = 0
    l, r = 0, len(arr) - 1
    while l < r:
        s = arr[l] + arr[r]
        if s == target:
            cnt += 1
            l += 1
            r -= 1
        elif s < target:
            l += 1
        else:
            r -= 1
    return cnt

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    arr = list(map(int, input().split()))
    x = int(input())
    print(twopointer(arr, x))
