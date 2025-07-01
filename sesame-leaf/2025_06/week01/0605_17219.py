import sys

def main():
    input = lambda: sys.stdin.readline().rstrip()
    
    url_num, search_num = map(int, input().split())
    
    site_pws = dict()
    for _ in range(url_num):
        data = input().split()
        site_pws[data[0]] = data[1]
    
    pws = list()
    for _ in range(search_num):
        pws.append(site_pws[input()])
        
    print("\n".join(pws))

if __name__ == "__main__":
    main()
    