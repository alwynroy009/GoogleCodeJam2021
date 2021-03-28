
t = int(input())
tc = 1

def Reverse(lst):
    return [ele for ele in reversed(lst)]

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        j = a[i:n].index(min(a[i:n]))+1+i
        if j == len(a) and i==0:
            a = Reverse(a)
        elif j != len(a) and i!=0:
            if j-i != 1:
                a = a[:i] + Reverse(a[i:j]) + a[j:] 
        elif j == len(a) and i != 0:
            if j-i != 1:
                a = a[:i] + Reverse(a[i:])
        elif j != len(a) and i==0:
            a = Reverse(a[:j]) + a[j:]

        ans += j-(i+1)+1

    t -= 1
    print(f'Case #{tc}: {ans}')
    tc += 1

