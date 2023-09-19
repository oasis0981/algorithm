def solution(n):
    answer = []
    for i in range(2, n+1):
        if n % i == 0 and isPrime(i):
            answer.append(i)
    return answer


def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True