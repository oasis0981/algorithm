from itertools import permutations

def solution(spell, dic):
    words = list(map(list, (permutations(spell, len(spell)))))
    str_words = []
    
    for w in words: 
        str_w = ''.join(w)
        str_words.append(str_w)
    
    for d in dic:
        if d in str_words:
            return 1
        
    return 2