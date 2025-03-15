from egzP8atesty import runtests 

def reklamy ( T, S, o ):
    n = len(T)
    new_t = [0 for i in range(2 * n)]
    high_on_beg = [0 for i in range(n)]
    for i in range(n):
        new_t[2 * i] = [T[i][0], i, False, i]
        new_t[2 * i + 1] = [T[i][1], i, True, S[i]]
    new_t.sort(key=lambda x: x[0])
    curr_high = 0
    highest = 0
    for end, i_on_beg, is_end, cost in new_t:
        if is_end:
            curr_high = max(curr_high, cost)
            highest = max(highest, high_on_beg[i_on_beg] + cost)
        else:
            high_on_beg[i_on_beg] = curr_high
    return highest

runtests ( reklamy, all_tests=True )