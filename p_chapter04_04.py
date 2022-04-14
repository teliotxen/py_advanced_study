# Chapter 04 - 04
# 시퀀스형
# 해시테이블
# hashtable -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> Key 중복허용 X, Set -> 중복허용 X
# Dict 및 Set 심화

# immutable Dict
from types import MappingProxyType

d = {'key1': 'value1'}

# Read Only

d_frozen = MappingProxyType(d)

print(d, id(d))
print(d_frozen, id(d_frozen))


# 수정 가능
d['key2'] = 'value2'
print(d)

# 수정 불가능
# d_frozen['key2'] = 'value2'
# print(d_frozen)


# Set
s1 = {'apple', 'Orange', 'Apple', 'Orange', 'Kiwi'}
s2 = set(['apple', 'Orange', 'Apple', 'Orange', 'Kiwi'])
s3 = {3}
# s4 = {} 딕셔너리로 선언된다
s4 = set()
s5 = frozenset({'apple', 'Orange', 'Apple', 'Orange', 'Kiwi'})

s1.add('melon')
# print(s1)
# print(s2)

# 추가 불가 - forzenset
# s5.add('melon')


# print(s1, type(s1))
# print(s2, type(s2))
# print(s3, type(s3))
# print(s4, type(s4))
# print(s5, type(s5))

# 선언 최적화
# 파이썬은 바이트코드를 실행하고 파이썬 인터프리터가 바이트 코드를 내부적으로 실행함
# dis 는 코드가 실행될 때 프로세스를 보여준다.

from dis import dis

print('-------')
print(dis('{10}'))
print('-------')
print(dis('set([10])'))


# 지능형 집합(Comprehending Set)
from unicodedata import name
print({name(chr(i), '') for i in range(0,256)})
