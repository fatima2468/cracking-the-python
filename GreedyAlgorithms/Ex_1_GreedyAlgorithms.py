# Ugly solution will time out for very large inputs
def max_min_ugly_sol(k, arr):
    arr.sort()
    temp_arr = []
    kCount = 0
    min_unfairness = 10**9
    for i in range(len(arr)):
        if kCount < k:
            temp_arr.insert(kCount, arr[i])
            kCount += 1
        else:
            unfairness = max(temp_arr) - min(temp_arr)
            if unfairness < min_unfairness:
                min_unfairness = unfairness

            temp_arr = temp_arr[1:]
            print(arr[i])
            temp_arr += [arr[i]]

    unfairness = max(temp_arr) - min(temp_arr)
    if unfairness < min_unfairness:
        min_unfairness = unfairness

    return min_unfairness


def max_min_nice_sol(k, arr):
    arr_s = sorted(arr)
    min_unfairness = 10**9
    for i in range(len(arr) - k + 1):
        sub_arr_min = arr_s[i]
        sub_arr_max = arr_s[i+k-1]
        min_unfairness = min(sub_arr_max - sub_arr_min, min_unfairness)
    return min_unfairness

print(max_min_ugly_sol(4, [1, 2, 3, 4, 10, 20, 30, 40, 100, 200]))
print(max_min_nice_sol(4, [1, 2, 3, 4, 10, 20, 30, 40, 100, 200]))


