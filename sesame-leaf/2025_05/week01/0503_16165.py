import sys

if __name__ == "__main__":
    input = lambda : sys.stdin.readline().rstrip()

    N, M = map(int, input().split())

    group_name_dict = {}
    group_member_dict = {}
    for _ in range(N):
        
        group_name = input()
        group_population = int(input())
        group_name_dict[group_name] = [input() for _ in range(group_population)]
        for x in group_name_dict[group_name]:
            group_member_dict[x] = group_name

    for _ in range(M):
        problem_name = input()
        problem_type = input()
        
        if problem_type == "0":
            print("\n".join(sorted([x for x in group_name_dict[problem_name]])))
        else:
            print(group_member_dict[problem_name])
