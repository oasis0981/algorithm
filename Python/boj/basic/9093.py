# t = int(input())
#
# def change_word(word):
#     word_list = list(word)
#     if len(word_list) == 1:
#         return word
#     for i in range(len(word_list)//2):
#         word_list[i], word_list[len(word_list)-(i+1)] = word_list[len(word_list)-(i+1)], word_list[i]
#     return ''.join(word_list)
#
#
# for _ in range(t):
#     sentence = input().split()
#     for i in range(len(sentence)):
#         sentence[i] = change_word(sentence[i])
#     print(' '.join(sentence))

# t = int(input())
#
# for _ in range(t):
#     sentence = input().split()
#     for word in sentence:
#         print(word[::-1], end = " ")
#     print()

l = [("abc"), ("cd")]
def change_to_string(combi):
    for i in range(len(combi)):
        combi[i] = ''.join(combi[i])
    return combi
print(change_to_string(l))