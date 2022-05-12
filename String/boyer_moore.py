def boyer_moore_match(T, P):
    n = len(T)
    m = len(P)

    last = {}

    for i in range(m):
        last[P[i]] = i

    i = m - 1
    j = m - 1
    
    while i < n:
        if T[i] == P[j]:
            if j == 0:
                return i
            else:
                i -= 1
                j -= 1
        else:
            l = last.get(T[i], -1)
            i = i + m - min(j, 1 + l)
            j = m - 1

    return -1

print(boyer_moore_match("test pattern", "tern"))