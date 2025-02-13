# Assignment
# v3.6) 2중 데코레이터 적용, 성능측정 데코레이터, 디스크립션 데코레이터를 팩토리얼 함수에 적용하시오.

import time

from anaconda_project.internal.conda_api import result


@time_decorator
@description_decorator
def description(func)
    def wrapper(*arg)
        print(func.__name__)
        print(func.__doc__)
        r = func(*arg)
        return result * i
    return result


def time_decoration(func):
    def wrapper(*arg):
        s = time.time()
        r = func(*arg)
        e = time.time()
        print(f'실행시간 : {e -s}초')
        return r
    return wrapper

# @time_decorator
def factorial_repetition(n) -> int:
    result = 1
