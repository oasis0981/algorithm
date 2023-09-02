'''

알파벳 대문자와 숫자 0~9로만 구성된 문자열이 입력으로 주어짐
모든 알파벳을 오름차순 정렬 출력한 뒤에, 모든 숫자를 더한 값을 이어서 출력

'''

words = input()

alphabets = []
cnt = 0
for i in words:
    if i.isalpha():
        alphabets.append(i)
    else:
        cnt += int(i)

alphabets.sort()

if cnt != 0:
    alphabets.append(str(cnt))

print(''.join(alphabets))