def solution(array, n):
    currentMin=101
    currentGap=100
    for number in array:
        if abs(number-n) == currentGap:
            if number < currentMin:
                currentMin = number
                continue
        if abs(number-n) < currentGap:
            currentMin = number
            currentGap = abs(number-n)
            
    return currentMin