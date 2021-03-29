
t = int(input())
tc = 1

while t>0:
    n, c = map(int, input().split())
    remaining = c - (n - 1)  # 6 - (4-1) = 3
    l = list(range(1, n+1)) # [1,2,3,4]
    if (c >= n-1 and c <= (n*(n+1)/2)-1):
        for i in range(n-2, -1, -1):  #  [2, 1, 0]
            tot_work = n - i - 1  # 1, 2, 3; 
            used = min(remaining, tot_work) # min(3,1) ; min(2,2) ; min(0, 3)
            remaining -= used # 2; 0
            l[i:i+used+1] = reversed(l[i:i+used+1])
        ans = ' '.join(str(a) for a in l)
    else:
        ans = 'IMPOSSIBLE'
    print(f'Case #{tc}: {ans}')
    t -= 1
    tc += 1
