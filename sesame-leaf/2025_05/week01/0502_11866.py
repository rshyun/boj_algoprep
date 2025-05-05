
if __name__ == "__main__":
    N, K = map(int, input().split())

    seat_list = [i for i in range(1, N+1)]
    Josephus_series = []

    pointer = 0
    while len(seat_list) != 0:
        pointer = (pointer + K - 1) % len(seat_list)
        Josephus_series.append(seat_list.pop(pointer))

    print("<" + ", ".join(map(str, Josephus_series)) +">")
