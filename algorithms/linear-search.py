from array import array
import big_o


def linear_search(array):
    target = 9999
    for i in range(len(array)):
        if array[i] == target:
            return True

    return False

positive_int_generator = lambda n: big_o.datagen.integers(n, 0, 10000)
best, others = big_o.big_o(linear_search, positive_int_generator, n_repeats=100)
print(best)