def main():
    t = int(input())
    tc = 1
    while t>0:
        x, y, str1 = input().split()
        x, y = int(x), int(y)
        
        n = len(str1)
        ds = [[1e5, 1e5] for _ in range(n)]
        
        if str1[0] != 'C': #J or ?
            ds[0][1] = 0
        if str1[0] != 'J': #C or ?
            ds[0][0] = 0
            
        for i in range(1,n):
            if str1[i] != 'C':  # J or ?
                ds[i][1] = min(ds[i][1], ds[i-1][1], ds[i-1][0]+x)
            if str1[i] != 'J':  # C or ?
                ds[i][0] = min(ds[i][0], ds[i-1][0], ds[i-1][1]+y)
        
        ans = min(ds[n-1][0], ds[n-1][1])
        
        # ans = str1.replace('?','').count('CJ')*x + str1.replace('?','').count('JC')*y
        print(f'Case #{tc}: {ans}')
        t -= 1
        tc += 1
        
main()
