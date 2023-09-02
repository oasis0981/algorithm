from string import ascii_lowercase

a_list = list(ascii_lowercase)

n = input()

for i in a_list:
    print(n.find(i), end=" ")
