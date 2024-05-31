from array import array
import big_o

def findSmallest(array):

    smallest = array[0]
    smallest_index = 0
    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
        print(i)

    return smallest_index

def selectionSort(array):
    newArray = []
    copiedArray = list(array)
    for i in range(len(copiedArray)):
        smallest = findSmallest(copiedArray)
        newArray.append(copiedArray.pop(smallest))
    return newArray


print(selectionSort([5,8,4,9]))
#positive_int_generator = lambda n: big_o.datagen.integers(n, 0, 10)
#best, others = big_o.big_o(selectionSort, positive_int_generator, n_repeats=1)
#print(best)
