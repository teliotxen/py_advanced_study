# Chapter 04 - 03
# 시퀀스형
# 컨테이너 형태의 자료형 (container: 서로다른 자료형[list, tuple, dictionary, collections.deque]을 한번에 저장할 수 있는 저장 공간)
# 플랫(Flat : 단일 자료형([str, bytes, bytearray, array.array, memoryview])만 담을 수 있는 저장공간
# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)

# 해시테이블
# Key에 Value를 저장하는 구조 __dir__
# 파이썬 dict 해쉬 테이블 예,
# 키 값의 연산 결과에 따라 직접 접근이 가능한 구조
# key 값을 해싱 함수 -> 해쉬 주소 -> key 에 대한 value의 위치를 알 수 있다.

# DICT 구조 - 파이썬 엔진은 기본적으로 테이블 앤진으로 이루어져 있다.
# print(__builtins__.__dict__)

# hash 값을 확인할 수 있다는 것은 고유한 값이라는 것이다. 즉 immutable 이어야 한댜

t1 = (10,20,(30,40,50))
t2 = (10,20,[30,40,50]) #리스트는 mutable 이라 hash 값을 사용할 수 없음

print(hash(t1))
# print(hash(t2)) 오류 발생


# Dict setdefault 예제 - 검색 분석을 사용할 때 속도가 빨라짐 (reference 권장사항)
source = (('k1','val1'),
            ('k1','val2'),
            ('k2','val3'),
            ('k2','val4'),
            ('k2','val5'),
          )

new_dict1 = {}

new_dict2 = {}

# not Using setDefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]
print(new_dict1)

# Using setDefault
for k, v in source:
    new_dict2.setdefault(k,[]).append(v)
print(new_dict2)


# 중복되면서 삭제된다.
new_dict3 = {k: v for k, v in source}
print(new_dict3)