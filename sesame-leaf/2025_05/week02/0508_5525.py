import sys

if __name__ == "__main__":
    
    input = lambda: sys.stdin.readline().rstrip()
    
    N = int(input())
    M = int(input())
    S = input()
    
    S_N_count = 0
    
    start_idx = 0
    end_idx = 0
    while start_idx < len(S):
        
        if S[start_idx] == "O":
            start_idx += 1
            end_idx += 1
        elif S[start_idx] == "I" and S[end_idx+1:end_idx+3] == "OI":
            end_idx += 2
        elif S[start_idx] == "I" and S[end_idx+1:end_idx+3] != "OI":
            S_N_count = S_N_count + (((end_idx-start_idx)//2) - N + 1) if ((end_idx-start_idx)//2) - N >= 0 else S_N_count
            
            start_idx = end_idx + 1
            end_idx = start_idx
    
    print(S_N_count)
    