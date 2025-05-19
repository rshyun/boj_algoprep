def main():
    A = int(input())
    B = int(input())
    
    val1 = A * (B % 10)
    val2 = A * ((B % 100) - (B % 10)) // 10
    val3 = A * ((B % 1000) - (B % 100)) // 100
    val4 = val1 + val2*10 + val3*100
    print(f"{val1}\n{val2}\n{val3}\n{val4}")

if __name__ == "__main__":
    main()
    