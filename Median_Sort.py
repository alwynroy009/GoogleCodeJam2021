t, n, _ = [int(a) for a in input().split()]

def get_place_index(lst, the_num):
    i, j = len(lst)*1//3, len(lst)*2//3
    while True:
        print(lst[i], the_num, lst[j], flush=True)
        m = int(input())
        if m == the_num:                            # 0.......1/3......[X]......2/3........3/3
            if j-i == 1:
                return j
            else:
                i, j = i+(j-i)*1//3 , i+(j-i)*2//3
        elif m == lst[i]:                           # 0.......[X]......1/3......2/3........3/3
            if i == 0:
                return 0
            elif j-i == 1:
                i,j = i-1,i
            else:
                i, j = i-(j-i)*2//3 , i-(j-i)*1//3
        else:                                       # 0.......1/3......2/3......[X]........3/3
            if j == len(lst)-1:
                return len(lst)
            elif j-i == 1:
                i,j = j,j+1
            else:
                i, j = j+(j-i)*1//3 , j+(j-i)*2//3
        if i == j:
            j += 1

while t>0:
    print(1, 2, 3, flush=True)
    l = int(input())
    if l == 1:
        lst = [2, 1, 3]
    elif l == 2:
        lst = [1, 2, 3]
    else:
        lst = [1, 3, 2]
    while len(lst) < n:
        next_i = len(lst) + 1
        place_index = get_place_index(lst, next_i)
        lst.insert(place_index, next_i)
        

    print(' '.join(str(a) for a in lst), flush=True)
    ans = int(input())
    if ans == 1:
        pass # success
    if ans == -1:
        sys.exit()

    t-=1
