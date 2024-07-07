def star(n, star_map):
    pass

if __name__ == "__main__":
    n = int(input())

    star_map = [[0]*(2*n-1) for _ in range(2*n-1)]
    
    star(n, star_map)
    