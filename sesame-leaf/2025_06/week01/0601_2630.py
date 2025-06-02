import sys

def same_color_cnt(paper_is_blue:list[list[bool]]) -> tuple[int, int]:
    
    # (start_coord, edge_len)
    stack = [(0, 0, len(paper_is_blue))]
    white_paper_cnt = 0
    blue_paper_cnt = 0
    
    while stack:
        x, y, edge_len = stack.pop()
        
        # decide that all paper is blue or white
        all_blue = True
        all_white = True
        for i in range(y, y+edge_len):
            
            if (not all_blue) and (not all_white):
                break
            
            for j in range(x, x+edge_len):
                if (not all_blue) and (not all_white):
                    break
                
                all_blue = all_blue and paper_is_blue[i][j]
                all_white = all_white and (not paper_is_blue[i][j])
        
        if all_blue:
            blue_paper_cnt += 1
            continue
        
        elif all_white:
            white_paper_cnt += 1
            continue
        
        stack.append((x, y, edge_len//2))
        stack.append((x+(edge_len//2), y, edge_len//2))
        stack.append((x, y+(edge_len//2), edge_len//2))
        stack.append((x+(edge_len//2), y+(edge_len//2), edge_len//2))
    
    return (white_paper_cnt, blue_paper_cnt)

def main() -> None:
    input = lambda: sys.stdin.readline().rstrip()
    
    N = int(input())
    
    # blue : True, white : False
    paper = [[True if x == "1" else False for x in input().split()] for _ in range(N)]
    white, blue = same_color_cnt(paper)
    
    print(white)
    print(blue)

if __name__ == "__main__":
    main()
    