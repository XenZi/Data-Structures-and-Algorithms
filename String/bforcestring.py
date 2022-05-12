def brute_force(T, P):
    n = len(T)
    m = len(P)

    for i in range(n-m+1):
        j = 0
        while j < m and T[i+j] == P[j]:
            j+=1
            if j == m:
                return i
    return -1


print(brute_force('test pattern', 'tern'))

