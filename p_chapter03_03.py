# Chapter 03-03
# Special Method(magic mathod)
# 파이썬의 핵심 -> 시퀀스, 반복, 함수, 클래스
# 클래스안에 정의할 수 있는 특별한(built-in) 메소드

# 객체 => 파이썬의 데이터를 추상화
# 모든 객체 -> id, type -> value

# 일반적인 튜플
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt


l_leng1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)
print(l_leng1)



# named tuple 사용
# 네임드 튜플은 튜플인데 딕셔너리처럼 키와 밸류로 저장되는 형식


from collections import namedtuple

# 네임드 튜플 선언
Point = namedtuple('Point', 'x y')
pt3 = Point(1.0, 5.0)
pt4 = Point(2.5,1.5)

print(pt3[0], pt4.y)
l_leng2 = sqrt((pt3.x - pt4.x) ** 2 + (pt3[1] - pt4[1]) ** 2)
print(l_leng2)

# 네임드 튜플 선언 방법
Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')
Point4 = namedtuple('Point', 'x y x class', rename=True) #예약어를 사용하기 때문에 명명함

# Dict to Unpacking
# 언팩킹 시 튜플은 * 딕셔너리는 **
temp_dict = {'x': 75, 'y': 55}

# 객체생성
p1 = Point1(x=10, y=35)
p2 = Point2(20,40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)
p5 = Point3(**temp_dict) #딕셔너리를 언페킹 후 자료형 저장, 언팩킹 시 튜플은 * 딕셔너리는 **

print()

print(p1)
print(p2)
print(p3)
print(p4)

# named tuple method
temp = [52,38]

# _make() : 리스트를 기반으로 새로운 객체 생성
p4 = Point1._make(temp)
print(p4)

# _fields : 필드 네임 확인, 키 값 조회
print(p1._fields)

# _asdict() : orderDictionary 반환
print(p1._asdict())


# 실사용 실습
# 반 20명 , 4개의 반 , a, b, c, d반

Classes = namedtuple('Classes', ['rank', 'number'])

# 그룹 리스트
numbers = [str(n) for n in range(1,21)]
ranks = 'A B C D'.split()
#
# print(numbers)
# print(ranks)

# list comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers]

# print(students)


students2 = [Classes(rank, number)
     for rank in 'A B C D'.split()
        for number in [str(n)
                    for n in range(1,21)]]


# print(numbers)
# print(ranks)
print(123)
for s in students2:
    print(s)
