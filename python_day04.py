# Assignment
# v3.6) 2중 데코레이터 적용, 성능측정 데코레이터, 디스크립션 데코레이터를 팩토리얼 함수에 적용하시오.

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f'Function Name : {func.__name__}')
        print(f'Function Arguments : {args}')
        print(f'Function Keywards Arguments : {kwargs}')
        result = func(*args, **kwargs)
        return result
    return wrapper

def greet(name, greeting="안녕하세요", age=None):
    return f"{greeting}, {name}"if age else f"{greeting}, {name}"

print(greet("인하"))
print(greet(name:"인상", greeting: "안녕"))
print(greet(name:"James", greeting:"Hello"))
print(greet(name:"Gonzales", greeting="Hola"))
print(greet(name:"Nakamura", greeting="Gonizziwa"))