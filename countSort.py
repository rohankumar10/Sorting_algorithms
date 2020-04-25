def countSort(array):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):    # O(max)
        count[array[i]] += 1

    for i in range(1, 10):      # O(size)
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:               # O(max)
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    for i in range(0, size):    # O(size)
        array[i] = output[i]


data = [4, 2, 2, 8, 3, 3, 1]
countSort(data)
print("Sorted Array in Ascending Order: ")
print(data)
print("Worst Case Complexity:- O(max+size)")
print("Average Case Complexity:- O(max+size)")
print("Best Case Complexity:- O(max+size)")
