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
            if isinstance(array, list):
                params = (list(array), ) + params[1:]
            
            sorted_array = self.sort_function(*params, **kwargs)
            
            if isinstance(array, str):
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

@ErrorCheck
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

    for i in range(0,len(A)): 
        A[i] = output[i] 

    return A
  
@ErrorCheck
def radix_sort(array): 
    max_of_list = max(array) 

    mod = 1
    while max_of_list / mod > 0: 
        array = __counting_sort(array, mod) 
        mod *= 10
    return array
# end radix sort


# comb_sort
@ErrorCheck
def comb_sort(array):
    n = len(array)
    SHRINK_FACTOR = 1.3
    #initialize the gap to length of array
    gap = n

    swapped = True

    while gap > 1 or swapped:
        #finding next gap
        gap = int(float(gap) / SHRINK_FACTOR)

        swapped = False

        for i in range(0, n - gap):
            if array[i] > array[i + gap]:
                array[i], array[i + gap] = array[i + gap], array[i]
                swapped = True
    return array
# end comb sort


# pancake sort
@ErrorCheck
def pancake_sort(array):
    cur = len(array)

    while cur > 1:
        # find the index of the max element
        mi = array.index(max(array[:cur]))
        # reverse list from 0 to mi
        array = array[mi::-1] + array[mi + 1:]
        # reverse the whole list
        array = array[cur - 1::-1] + array[cur:]

        cur -= 1
    return array
# end pancake sort


# shell sort
@ErrorCheck
def shell_sort(array):
    length = len(array)
    #initalize gap to mid of the array
    gap = length // 2

    while gap > 0:
        for i in range(gap, length):
            temp = array[i]
            j = i

            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap

            array[j] = temp
        gap = gap // 2
    return array
# end shell sort


# bucket sort
@ErrorCheck
def bucket_sort(array):
    B = [list() for _ in range(10)]

    for i, x in enumerate(array):
        B[int(x * len(B))].append(x)

    output = []

    for buckets in B:
        output += insertion_sort(buckets)

    return output
# end bucket sort


# counting sort
@ErrorCheck
def counting_sort(array):
    
    #intitalize output final array
    output = [0] * 256

    count = [0] * 256

    #storing the count of each character
    for x in array:
        count[ord(str(x))] += 1

    for i in range(256):
        count[i] += count[i - 1]

    for i in range(len(array)):
        output[count[ord(str(array[i]))] - 1] = array[i]
        count[ord(str(array[i]))] -= 1

    for i in range(len(array)):
        array[i] = output[i]
    return array
# end counting sort


# tim sort
RUN = 32


def __merge_tim(A, p, q, r):
    la = A[p:q]
    ra = A[q:r]
    i = 0
    j = 0
    k = p
    for l in range(k, r):
        if j >= len(ra) or (i < len(la) and la[i] < ra[j]):
            A[l] = la[i]
            i = i + 1
        else:
            A[l] = ra[j]
            j = j + 1
    return A

def __insertion_sort(A, left, right):
    for i in range(left + 1, right + 1):
        key = A[i]
        # Insert A[j] into the sorted sequence A[1....j-1]
        j = i - 1

        while j >= left and A[j] > key:
            A[j + 1] = A[j]
            j -= 1

        A[j + 1] = key
    return A

@ErrorCheck
def tim_sort(array):
    for i in range(0, len(array), RUN):
        array = __insertion_sort(array, i, min((i + 31), (len(array) - 1)))

    for size in range(RUN, len(array)):
        for left in range(0, len(array)):
            mid = left + size - 1
            right = min((left + 2*size - 1), (len(array) - 1))
            array = __merge_tim(array, left, mid, right)
            left += 2*size
        size *= 2
    return array
# end tim sort

# tree sort
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def __insert(root, node):
    if root is None:
        root = node

    else:
        if root.data > node.data:
            if root.left is None:
                root.left = node
            else:
                __insert(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                __insert(root.right, node)
arr = []
def __in_order_traversal(root):
    
    if not root:
        return
    else:
        __in_order_traversal(root.left)
        arr.append(root.data)
        __in_order_traversal(root.right)
    return arr

@ErrorCheck
def tree_sort(array):
    root = Node(array[0])
    for i in range(1, len(array)):
        __insert(root, Node(array[i]))
    return __in_order_traversal(root)

# end tree sort



print(tree_sort("djsfgjh"))