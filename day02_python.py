# v1.1) for -> while
# v1.2) while 구문으로 구간 소수를 출력하는 프로그램 작성
# v1.3) ** 대신 pow 함수

# v1.1) for -> while
import math

def is_prime(num) -> bool:
    if num < 2:
        return False

    i = 2
    while i <= int(num ** 0.5):  # while 문 사용
        if num % i == 0:
            return False
        i += 1

    return True

n = float(input("Input number : "))

# 소수인지 판별 후 제곱근 출력
sqrt_value = math.sqrt(n)
print(f"{n}의 제곱근은 {sqrt_value}입니다.")

