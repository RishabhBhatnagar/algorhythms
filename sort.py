def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(i, n):
            if array[j] < array[i]:
                array[j], array[i] = array[i], array[j]
    return array

def __merge(a, b):
    if a and b:
        if a[0] > b[0]:
            return [a[0]] + __merge(a[1:], b)
    return a + b

def merge_sort(array):
    """
        Returns a sorted array.
        Does not modify the original array.
    """
    if len(array) <= 1 : return array
    half = len(array) // 2
    left = merge_sort(array[:half])
    right = merge_sort(array[half:])
    return __merge(left, right)

if __name__ == "__main__":
    a = [1, 3, 2, 3]
    b = list("iokszueg")
    print(bubble_sort(a))
    
