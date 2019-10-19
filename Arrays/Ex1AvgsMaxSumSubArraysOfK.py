# Exercise-1: For the given array and size K, find average of sub-arrays of size k

# Solution-1 : Time Complexity O(N^2)
def find_averages_of_subarrays(K, arr):
  result = []
  for i in range(len(arr)-K+1):
    _sum = 0.0 # find sum of next 'K' elements
    for j in range(i, i+K):
      _sum += arr[j]
    result.append(_sum/K)  # calculate average

  return result

# Solution-2 : Time Complexity O(N)
def find_averages_of_subarrays2(K, arr):
    result = []
    _sum = 0.0
    start = 0
    for end in range(len(arr)):
        # find sum of next 'K' elements
        _sum += arr[end]

        if end >= K - 1:
            result.append(_sum / K)  # calculate average
            _sum -= arr[start]
            start += 1

    return result

result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2, 3, 4, 6, -1, -2, 8])
print("Averages of subarrays of size K: " + str(result))


# Exercise-2: For the given array and size K, find sub-array having max sum of all sub-arrays
# Solution-2 : Time Complexity O(N)
def max_sub_array_of_size_k(K, arr):
    _sum = 0.0
    _maxsum = 0.0
    _maxsubarr = []
    start = 0
    count = 0

    for i in range(len(arr)):
        _sum += arr[i]
        count += 1
    if count == K:
        if _sum > _maxsum:
            _maxsubarr

        _sum -= arr[start]
        start += 1
        count = 0

    return _maxsum


print("Maximum of subarrays of size K=5: " + max_sub_array_of_size_k(5, [1, 3, 2, 6, -1, 4, 1, 8, 2, 3, 4, 6, -1, -2, 8])
print("Maximum of subarrays of size K=2: " + max_sub_array_of_size_k(2, [1, 3, 2, 6, 8]))
