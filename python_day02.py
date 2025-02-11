# v1.2 prime number

def is_prime(num) -> bool:

numbers = Input("Input number : ").split()

n1 = int(numbers[0])
n2 = int(numbers[1])

if n1 > n2:
    n1, n2 = n2, n1

j = n1
while j <= n2:
    if is_prime(j):
        print(j, end=' ')
    j = j + 1