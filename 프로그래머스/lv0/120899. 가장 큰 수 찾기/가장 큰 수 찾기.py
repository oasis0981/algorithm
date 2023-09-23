def solution(array):
    max_num = max(array)
    enum_list = [(idx, num) for (idx, num) in enumerate(array)]
    for idx, num in enum_list:
        if num == max_num:
            return [num, idx]
    