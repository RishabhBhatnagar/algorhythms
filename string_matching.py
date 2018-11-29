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


# finite automata
NO_OF_CHARS = 256

def __getNextState(pat, M, state, x):

	if state < M and x == ord(pat[state]): 
		return state + 1 # if character is same as next then increment state

	i=0
	# ns stores the result which is next state 
  
    # ns finally contains the longest prefix  
    # which is also suffix in "P[0..state-1]" 
  
    # Start from the largest possible value and  
    # stop when you find a prefix which is also suffix
	for ns in range(state, 0, -1): 
		if ord(pat[ns - 1]) == x: 
			while(i < ns-1): 
				if pat[i] != pat[state - ns + 1 + i]: 
					break
				i += 1
			if i == ns - 1: 
				return ns 
	return 0

def __computeTF(P, M):
	TF = [[0 for i in range(NO_OF_CHARS)] for _ in range(M+1)] 

	for state in range(M+1): 
		for x in range(NO_OF_CHARS): 
			z = __getNextState(P, M, state, x) 
			TF[state][x] = z 

	return TF 

def finite_automata(T, P):
	indexes = []
	M = len(P) 
	N = len(T) 
	TF = __computeTF(P, M)	 
 
	state=0
	for i in range(N): 
		state = TF[state][ord(T[i])] 
		if state == M: 
			indexes.append(i - M + 1)
	return indexes
# finite automata end


print(finite_automata("sajkdugfvkiausgfiagsfugsaiufasiasiasasasjugasiugaisuiasug ", 'as'))
