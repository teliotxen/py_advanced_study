# Chapter 05 - 01
# 일급함수 (First Class Functions)
# 파이썬 함수 특징
# 1. 런타임 초기화
# 2. 변수 할당 가능
# 3. 함수를 인수 전달 가능
# 4. 함수를 결과 반환

# 함수 객체

def factorial(n):
    '''Factorial Function -> n : int'''
    if n == 1:
        return 1
    return n * factorial(n-1)

class A:
    pass

print(factorial(5))
print(factorial.__doc__)

#함수만이 가진 메소드
print(set(sorted(dir(factorial)))-set(sorted((dir(A)))))
print(factorial.__name__)
print(factorial.__code__)

#변수 할당 가능
var_func = factorial

print(var_func)
print(var_func(10))
print(list(map(var_func, range(1,11))))

# 함수를 인수로 전달 및 함수로 결과를 반환할 수 있어야 함

from functools import reduce
from operator import add

print(sum(range(1,11)))
print(reduce(add, range(1,11)))

# 익명함수(lambda) 가급적 주석을 꼭 작성하세요
# 일반 함수 형태로 리팩토링을 권장함 
print(reduce(lambda x, t: x + t, range(1,11)))

# callable : 호출 연산자 -> 메소드 형태로 호출 가능한지 확인하는 함수
# 호출한다는 의미느 함수() 했을 때 결과값을 주는 것
print(callable(str), callable(A), callable(var_func), callable(factorial), callable(3.14))

# partial 사용법 !중요, 많이 사용함 : 인수 고정 -> 콜백 함수에 사용함
from operator import mul
from functools import partial
print(mul(10,10), 10*10)

# 인수 고정
five = partial(mul, 5)
# 함수를 인자에 고정하고, 그 함수를 변수에 할당함
print(five(10))
print(five(100))
six = partial(five,6)
print(six())
# print(six(5)) 오류 발생

print([five(i) for i in range(1,10)])
print(list(map(five,range(1,10))))


