def main():

    while True:    # 계속 반복
        n = int(input())
        a = 0
        b = 1
        lst = []

        if n == -1:    # n == -1 이면 끝
            break

        while a + 1 < n:    # a < n 이면 약수인 a == n 인 경우로 포함해서 lst에 넣어버림
            a += 1    # a 에 1씩 더하며 약수를 찾는 모습
            if n % a == 0:
                lst.append(a)

        if sum(lst) == n:    # 완전수를 찾음
            while lst[-2] != '+':    # 가장 뒷 번째 숫자 왼쪽에 + 를 추가하는 액션이 마지막이 되도록
                lst.insert(b,'+')
                b += 2    # 1 에 2씩 더해가며 홀수만 골라내기
            print(n, '=', end=" ")
            for i in lst:
                print(i, end=" ")
            print()
        else:    # 완전수가 아님..
            print(n, "is NOT perfect.")

if __name__ == '__main__':
    print(main())