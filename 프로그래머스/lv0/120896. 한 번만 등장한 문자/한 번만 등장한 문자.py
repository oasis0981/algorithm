def solution(s):
    s_list = list(s)
    s_set = set(s_list)
    result = []
    for word in s_set:
        if s_list.count(word) == 1:
            result.append(word)
    return ('').join(sorted(result))