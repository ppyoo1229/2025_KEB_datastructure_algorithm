from sympy import factorial


def = nCr(n,r) -> int:

numerator = factorial(n)
denominator = factorial(n-r) * factorial(r)
return numerator / denominator

if __name__=="__main__":
    n = int(input("Input n : "))
    r = int(input("Input r : "))
    print(f"{n}C{n} = {nCr(n, r)}")