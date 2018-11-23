class ErrorCheck:
    """
      Assumptions : 
          first parameter of sorting function is array to be sorted.
      This class checks for error in the parameters 
      and returns sorted object of given type.
    """
    
    def __init__(self, sort_function):
        self.sort_function = sort_function
        
    def __call__(self, *params, **kwargs):
        array = params[0]
        array_type = type(array)
        
        if not isinstance(array, __import__("collections").Iterable):
            print("Expected an iterable, {} found".format(array_type))
            return None
        else:
            if array_type != type([]):
                params = (list(array), ) + params[1:]
            
            sorted_array = self.sort_function(*params, **kwargs)
            if array_type == type(""):
                return "".join(sorted_array)
            return array_type(sorted_array)


# bubble sort
@ErrorCheck
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(i, n):
            if array[j] < array[i]:
                array[j], array[i] = array[i], array[j]
    return array
# end bubble sort


# Merge sort
def __merge(a, b):
    if a and b:
        if a[0] < b[0]:
            return [a[0]] + __merge(a[1:], b)
        else:
            return [b[0]] + __merge(a, b[1:])
    return a + b

@ErrorCheck
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
# end Merge sort


# quick sort
def __partition(a, l, r):
    key = a[r]
    i = l - 1
    for j in range(l, r):   # upto r-1
        if a[j] < key:
            i += 1
            a[i], a[j] = a[j], a[i]
    i += 1
    a[i], a[r] = a[r], a[i]
    return i

@ErrorCheck
def quick_sort(array):
    def __quick_sort(array, l, r):
        if l < r:
            p = __partition(array, l, r)
            __quick_sort(array, l, p-1)
            __quick_sort(array, p+1, r)
            return array
    return __quick_sort(array, 0, len(array)-1)
# end quick sort


# insertion sort
@ErrorCheck
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array
# end insertion sort

# selection sort
@ErrorCheck
def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array
# end selection sort


