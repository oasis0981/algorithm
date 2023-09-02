

def solution(array):
    ans = 0
    str_list = [str(num) for num in array]
    for string in str_list:
        if "7" in string:
            ans += 1
    return ans

