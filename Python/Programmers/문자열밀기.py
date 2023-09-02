def solution(A, B):
    if A == B:
        return 0
    pushed = []
    word = A
    for _ in range(len(word)-1):
        word_list = list(word)
        word_list.insert(0, word_list.pop())
        word = ''.join(word_list)
        pushed.append(word)
    if B in pushed : return 1
    else: return -1

print(solution("afsefiaef","fafsefiae"))
