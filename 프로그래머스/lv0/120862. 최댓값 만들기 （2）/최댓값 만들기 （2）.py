def solution(numbers):
    if len(numbers) == 2:
        return numbers[0]*numbers[1]
    
    positives = [n for n in numbers if n > 0]
    negatives = [n for n in numbers if n < 0]
    
    max_pos = 0
    max_neg = 0
    if len(positives) > 1:
        max_pos = sorted(positives)[-1] * sorted(positives)[-2]
    if len(negatives) > 1:
        max_neg = sorted(negatives)[-1] * sorted(negatives)[-2]
        
    return max(max_pos, max_neg)