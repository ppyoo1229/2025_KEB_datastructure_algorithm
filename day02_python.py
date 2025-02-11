# 1) for -> while
# 2) while 구문으로 구간 소수를 출력하는 프로그램 작성
#

# 1) for -> while
# import math, sqrt 내장함수 사용 x
def is_prime(num) -> bool:
    if num < 2:
        return False

    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1

    return True

def sqrt_custom(n, precision=0.00001):
    """뉴턴-랩슨 방법을 사용한 제곱근 근사 계산"""
    approx = n  # 초기 추정값 (입력값)
    while True:
        better_approx = 0.5 * (approx + n / approx)  # 뉴턴-랩슨 공식 적용
        if abs(better_approx - approx) < precision:  # 수렴하면 종료
            return better_approx
        approx = better_approx  # 업데이트

n = int(input("Input number : "))
if is_prime(n):
    n = float(input("Input number : "))
    sqrt_value = sqrt_custom(n)  # 직접 만든 제곱근 함수 사용
    print(f"{n}의 제곱근은 {sqrt_value:.5f}입니다.")
