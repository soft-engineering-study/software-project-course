import big_o
def binary_search(array):
    target = 9999
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (high + low) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            high = mid - 1
        elif array[mid] < target:
            low = mid+1
    return -1

positive_int_generator = lambda n: big_o.datagen.integers(n, 0, 10000)
best, others = big_o.big_o(binary_search, positive_int_generator, n_repeats=100)
print(best)
