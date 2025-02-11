# v1.1) for -> while
# v1.2) while 구문으로 구간 소수를 출력하는 프로그램 작성
# v1.3) ** 대신 pow 함수

# v1.1) for -> while
# import math
#
# def is_prime(num) -> bool:
#     if num < 2:
#         return False
#
#     i = 2
#     while i <= int(num ** 0.5):
#         if num % i == 0:
#             return False
#         i += 1
#
#     return True
#
# n = float(input("Input number : "))
#
# sqrt_value = math.sqrt(n)
# print(f"{n}의 제곱근은 {sqrt_value}입니다.")


# v1.2) while 구문으로 구간 소수를 출력하는 프로그램 작성
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

start, end = map(int, input("숫자 두 개 입력: ").split())

# 시작 숫자가 끝 숫자보다 크면 교체
if start > end:
    start, end = end, start

print(f"{start}부터 {end}까지의 소수:")
num = start
while num <= end:
    if is_prime(num):  # 소수 판별 함수 호출
        print(num, end=" ")
    num += 1  # 다음 숫자로 이동



