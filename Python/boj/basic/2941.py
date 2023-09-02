def Count(word):
    cnt = 0
    cro_words = ["c=", "c-", "dz=",  "d-", "lj", "nj", "s=", "z="]
    for i in cro_words:
        if i in word:
            cnt += word.count(i)
            word = word.replace(i, ' ')
    cnt += len([j for j in word if j != ' '])
    return cnt

a = input()
print(Count(a))