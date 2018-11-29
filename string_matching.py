# start naive  
def naive(string, pattern):
    """
    Check against each contiguous look ahead subset of string 
    whether pattern is found
    """
    result = []
    m = len(string)
    n = len(pattern)
    for i in range(m-n+1):
        # string[i:i+n] is the subset.
        if string[i:i+n] == pattern:
            result.append(i)
    return result
# end naive


# kmp-algorithm
def kmp(string, pattern):
    def __prefix_function(s):
        # src:https://stackoverflow.com/questions/13792118/kmp-prefix-table
        π = [0]*len(s)         # pre-initialising pi with all zeros.
        j = 0
        for i in range(1, len(s)):
            while j>0 and s[j]!=s[i]:
                j = π[j-1]
            if s[j] == s[i]: j+= 1
            π[i] = j
        return π
    def __search(π, string, pattern):
        # src:http://hanslen.me/2017/02/06/KMP-Algorithm-explanation-and-python-code/
        size_p = len(pattern)
        size = len(string)
        p, s = 0, 0
        while p < size_p and s < size and size_p <= size:
            if(string[s] == pattern[p]):
                p += 1
                s += 1
            else:
                if p == 0:
                    s += 1
                else:
                    p = π[p-1]
        if p == size_p:
            yield s-size_p
            for i in __search(π, string[s:], pattern):
                if i != -1:
                    yield s+i
        else:
            yield -1

    π = __prefix_function(pattern)
    return list(__search(π, string, pattern))

