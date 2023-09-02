# import sys
# from string import ascii_uppercase
# word = sys.stdin.readline().rstrip().upper()
#
# dic = {}
# for letter in ascii_uppercase:
#     dic[letter] = word.count(letter)
#
# l = sorted(list(dic.values()), reverse=True)
#
# if l[0] == l[1]:
#     print("?")
# else:
#     print(max(dic, key=dic.get))

a = input().upper()
word = list(set(a))

cnt = []
for i in word:
    cnt.append(a.count(i))

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(word[cnt.index(max(cnt))])