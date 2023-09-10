def checkResult(words):
  newList = []

  for word in words:
    
    if word == '(' or word == '[':
      newList.append(word)
      continue

    if word == ')' or word == ']':
      if len(newList) == 0:
        return 'no'

    if word == ')':
      check = newList[-1]
      if (check != '('):
        return 'no'
      newList.pop()
      continue

    if word == ']':
      check = newList[-1]
      if (check != '['):
        return 'no'
      newList.pop()
      continue

  if len(newList) == 0:
    return 'yes'
  return 'no'


while True:
  words = input()
  if words == '.':
    break
  print(checkResult(words))
