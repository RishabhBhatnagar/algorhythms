def return_list(match_function):
    def return_list(*args, **kwargs):
        return list(
                   match_function(*args, **kwargs)
               )
    return return_list

# start naive  


@return_list
def naive(string, pattern):
    """
    Check against each contiguous look ahead subset of string 
    whether pattern is found
    """
    m = len(string)
    n = len(pattern)
    for i in range(m-n+1):
        # string[i:i+n] is the subset.
        print(string[i:i+n], pattern)
        if string[i:i+n] == pattern:
            yield i
# end naive


# kmp-algorithm
class KMP:
    def __hash(self, prev_char, next_char):
        """
          removes the hash of prev_char and adds hash of next_char
        """
            
    def __call__(self, string, pattern):
        self.prev_hash = None
        
# kmp-algorithm end


# rabin - karp algorithm
d = 256

@return_list
def rabin_karp_matcher(txt, pat): 
    M = len(pat) 
    N = len(txt) 
    j = 0
    p = 0 ; q = 101 
    t = 0    
    h = (d**(M-1)) % q
    indexes = []
    
    for i in range(M): 
        p = (d*p + ord(pat[i])) % q 
        t = (d*t + ord(txt[i])) % q 

    for i in range(N-M+1):
        if p == t: 
            for j in range(M): 
                if txt[i + j] != pat[j]: 
                    break
  
            j += 1
 
            if j == M: 
                indexes.append(i)

        if i < N-M: 
            t = (d*(t - ord(txt[i])*h) + ord(txt[i + M]))%q 

            if t < 0: 
                t += q 
    return indexes

# rabin - karp algorithm end


print(rabin_karp_matcher("sajkdugfvkiausgfiagsfugsaiufasiasiasasasjugasiugaisuiasug ", 'as'))
