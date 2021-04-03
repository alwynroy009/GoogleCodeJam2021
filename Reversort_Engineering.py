
t = int(input())
tc = 1

while t>0:
    n, c = map(int, input().split())
    remaining = c - (n - 1) 
    l = list(range(1, n+1)) 
    if (c >= n-1 and c <= (n*(n+1)/2)-1):
        for i in range(n-2, -1, -1):  
            tot_work = n - i - 1  
            used = min(remaining, tot_work)
            remaining -= used 
            l[i:i+used+1] = reversed(l[i:i+used+1])
        ans = ' '.join(str(a) for a in l)
    else:
        ans = 'IMPOSSIBLE'
    print(f'Case #{tc}: {ans}')
    t -= 1
    tc += 1
