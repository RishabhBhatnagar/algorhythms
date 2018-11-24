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


print(naive("sajkdugfvkiausgfiagsfugsaiufasiasiasasasjugasiugaisu iasug ", 'as'))

