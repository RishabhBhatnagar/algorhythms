class ErrorCheck:
    """
      Assumptions : 
          first parameter of sorting function is array to be sorted.
    """
    
    def __init__(self, sort_function):
        self.sort_function = sort_function
        
    def __call__(self, *params, **kwargs):
        if not isinstance(params[0], __import__("collections").Iterable):
            print("Expected an iterable, {} found".format(type(params[0])))
            return None
        else:
            return self.sort_function(*params, **kwargs)

@ErrorCheck
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

if __name__ == "__main__":
    a = [1, 3, 2, 3]
    b = list("iokszueg")
    print(bubble_sort(a))
    
