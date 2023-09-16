import math

def solution(numbers, k):
    result = 0
    cycle = len(numbers) // 2
    
    if k > cycle:
        numbers += numbers * math.ceil(k / cycle)
        
    for i in range(k):
        result = numbers[i*2]
        
    return result
