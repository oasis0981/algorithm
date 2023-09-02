words = list(input())
alphabets = 'ABC DEF GHI JKL MNO PQRS TUV WXYZ'
alphabets = alphabets.split()

sum = 0
for i in range(len(words)):
    for j in range(len(alphabets)):
        if words[i] in alphabets[j]:
            sum += j + 3

print(sum)
