# Method to count inversions (Not used in the problem solution though)
def get_inv_count(ar, n):
    inv_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if ar[i] > ar[j]:
                inv_count += 1
    return inv_count

print()

# Minimum swaps to sort the array of consective-unquie elements by detecting a cycle
def minimum_swaps(arr):
    swaps = 0
    n = len(arr)
    arr_dict = {}
    checked = [False] * n
    for i, item in enumerate(arr):
        arr_dict[item - 1] = i

    for key, val in arr_dict.items():
        if checked[key] or key == val:
            continue

        c_cycles = 0
        value = key

        while not checked[value]:
            checked[value] = True
            value = arr_dict[value]
            c_cycles += 1

        swaps += c_cycles - 1

    return swaps


# Minimum swaps to sort the array of consective-unquie elements in descending order by detecting a cycle
def minimum_swaps_desc(arr):
    swaps = 0
    n = len(arr)
    arr_dict = {}
    checked = [False] * n
    for i, item in enumerate(arr):
        arr_dict[item - 1] = n-i-1

    for key, val in arr_dict.items():
        if checked[key]:
            continue

        c_cycles = 0
        value = key

        while not checked[value]:
            checked[value] = True
            value = arr_dict[value]
            c_cycles += 1

        swaps += c_cycles - 1

    return swaps

# values = "2 31 1 38 29 5 44 6 12 18 39 9 48 49 13 11 7 27 14 33 50 21 46 23 15 26 8 47 40 3 32 22 34 " \
#          "42 16 41 24 10 4 28 36 30 37 35 20 17 45 43 25 19"

# values = "8 45 35 84 79 12 74 92 81 82 61 32 36 1 65 44 89 40 28 20 97 90 22 87 48 26 56 18 49 71 23 " \
#          "34 59 54 14 16 19 76 83 95 31 30 69 7 9 60 66 25 52 5 37 27 63 80 24 42 3 50 6 11 64 10 96 47 38 " \
#          "57 2 88 100 4 78 85 21 29 75 94 43 77 33 86 98 68 73 72 13 91 70 41 17 15 67 93 62 39 53 51 55 58 99 46"

values = "7 6 5 4 3 2 1"
values = "1 2 3 4"
arr1 = list(map(int, values.rstrip().split()))
print(minimum_swaps(arr1))

print(minimum_swaps_desc(arr1))
