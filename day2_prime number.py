
def is_prime(num)-> bool:

    if num >=2 :
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
    else:
        return False
    return True

help(abs)
n = int(input("Input number : "))
if is_prime(n):
    n = float(input("Input number : "))
    sqrt_value = math.sqrt(n)
print(f"{n}의 제곱근은 {sqrt_value}입니다.")