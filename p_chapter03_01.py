# Chapter 03-02
# Special Method(magic mathod)
# 파이썬의 핵심 -> 시퀀스, 반복, 함수, 클래스
# 클래스안에 정의할 수 있는 특별한(built-in) 메소드

# print(int)
# print(float)
#
# print(dir(int))
# print(dir(float))

n = 10

# print(type(n))

# print(n.__add__(100))
# print(n.__doc__)

# print(n.__bool__(), bool(n))
print(n*100, n.__mul__(100))


print()
print()


# 클래스 예제 1
# 과일 종류 !!!! 파이썬 데이터 모델

class Fruit:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return 'Fruit Class Info : {} , {}'.format(self._name, self._price)

    def __add__(self, x):
        print('called __add__')
        return self._price + x._price

    def __sub__(self, x):
        print('called __sub__')
        return self._price - x._price

    def __le__(self, x):
        print('called __le__', '작거나 같다')
        if self._price <= x._price:
            return True
        else:
            return False

    def __ge__(self, x):
        print('called __ge__', '크거나 같다')
        if self._price >= x._price:
            return True
        else:
            return False

# 인스턴스 생성

s1 = Fruit('orange', 7000)
s2 = Fruit('banana', 3000)

# 매직 매소드
print(s1 <= s2)
print(s1 >= s2)
print(s2 - s1)
print(s1 + s2)
print(s1, s2)

