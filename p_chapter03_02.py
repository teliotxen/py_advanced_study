# Chapter 03-02
# Special Method(magic mathod)
# 파이썬의 핵심 -> 시퀀스, 반복, 함수, 클래스
# 클래스안에 정의할 수 있는 특별한(built-in) 메소드

# 클래스 예제 2번
# 백터(x,y) (5,2) + (4,3) = (9,5)

class Vector(object):
    def __init__(self, *args):
        '''
        Create a vector , example : v = Vector(5,10)
        '''
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def __repr__(self):
        '''Return the vector information.'''
        return 'Vector(%r, %r)' %(self._x, self._y)

    def __add__(self, other):
        '''
        Return the vector add
        '''
        return Vector(self._x + other._x, self._y+ other._y)

    def __mul__(self, other):
        return Vector(self._x * other._x, self._y* other._y)

    def __bool__(self):
        # print("It's False")
        return bool(max(self._x, self._y))

print(Vector.__init__.__doc__)

v = Vector()
print(v._y, v._x)


# vector 인스턴스 생성
v1 = Vector(5,7)
v2 = Vector(23,35)
v3 = Vector()


# 매직 매소드 출력
print(v1.__add__(v3))
# print(v3.__bool__())
print(v1, v2, v3)

if bool(v1):
    print('zero')