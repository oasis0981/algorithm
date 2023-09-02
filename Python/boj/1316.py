# import sys
#
# def judge_group(word):
#     word_list = list(word)
#     set_list = list(set(word))
#     for char in set_list:
#         idx = []
#         for i in range(len(word_list)):
#             if char == word_list[i]:
#                 idx.append(i)
#         if len(idx) > 1 :
#             for j in range(0, len(idx)-1):
#                 if abs(idx[j] - idx[j+1]) > 1:
#                     return False
#     return True
#
#
# t = int(input())
# cnt = 0
# for i in range(t):
#     a = sys.stdin.readline().rstrip()
#     if judge_group(a) == True:
#         cnt += 1
# print(cnt)

n = int(input())
cnt = n
for i in range(n):
    word = input()
    for j in range(len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            cnt -= 1
            break
print(cnt)