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
def __merge(A, B):
    if A and B:
        if A[0] < B[0]:
            return [A[0]] + __merge(A[1:], B)
        else:
            return [B[0]] + __merge(A, B[1:])
    return A + B

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
def __partition(A, l, r):
    key = A[r]
    i = l - 1
    for j in range(l, r):   # upto r-1
        if A[j] < key:
            i += 1
            A[i], A[j] = A[j], A[i]
    i += 1
    A[i], A[r] = A[r], A[i]
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

# heap sort
def __build_max_heap(A):
    heap_size = len(A)
    for i in range(int(len(A)/2), -1, -1):
        __max_heapify(A, i, heap_size)
    return heap_size

def __max_heapify(A, i, heap_size):
    l = 2 * i + 1
    r = 2 * i + 2

    if l < heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r < heap_size and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        __max_heapify(A, largest, heap_size)
    return A

def heap_sort(array):
    heap_size = __build_max_heap(array)

    for i in range(len(array)-1, -1, -1):
        array[0], array[i] = array[i], array[0]
        heap_size -= 1
        array = __max_heapify(array, 0, heap_size)
    return array
# end heap sort


#radix sort
def __counting_sort(A, mod): 
  
    n = len(A) 

    output = [0] * n
  
    count = [0] * 10
  
    
    for i in range(0, n): 
        index = A[i] // mod 
        count[index % 10] += 1
  
    for i in range(1,10): 
        count[i] += count[i-1] 
  
    i = n-1
    while i>=0: 
        index = A[i] // mod 
        output[ count[index % 10] - 1] = A[i] 
        count[index % 10] -= 1
        i -= 1
  
    i = 0
    for i in range(0,len(A)): 
        A[i] = output[i] 

    return A

  

def radix_sort(array): 
    max_of_list = max(array) 

    mod = 1
    while max_of_list / mod > 0: 
        array = __counting_sort(array, mod) 
        mod *= 10
    return array
# end radix sort


