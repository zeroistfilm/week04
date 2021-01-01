# https://www.acmicpc.net/problem/2748

# 피보나치 수
# 전형적인 dp문제
# 딕셔너리에 계산된 값을 저장한다.
# 재밌는건 이전 2개의 값만 저장해도 괜찮다.

memo={}
def fibonacci(n):
    if n in memo:
        return memo[n]
    if n<=2:
        return 1
    else:
        f= fibonacci(n-1)+fibonacci(n-2)
        memo[n]=f
        return f
print(fibonacci(int(input())))