# Chapter 04 - 01
# 시퀀스형
# 컨테이너 형태의 자료형 (container: 서로다른 자료형[list, tuple, dictionary, collections.deque]을 한번에 저장할 수 있는 저장 공간)
# 플랫(Flat : 단일 자료형([str, bytes, bytearray, array.array, memoryview])만 담을 수 있는 저장공간
# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)

# 지능형 리스트(comprehending Lists)
chars = '+_)(*&^%$#!'
code_list1 = []
for s in chars:
    #unicode list
    code_list1.append(ord(s))




# comprehending Lists
code_list2 = [ord(s) for s in chars]



# comprehending Lists + map + filter
#
code_list3 = [ord(s) for s in chars if ord(s) > 40]
code_list4 = list(filter(lambda x : x > 40, map(ord, chars)))


print([chr(s) for s in code_list1])
print([chr(s) for s in code_list2])
print([chr(s) for s in code_list3])
print([chr(s) for s in code_list4])


#Generator 생성 () : 한 번에 한 개의 항목을 생성 (메모리 유지 X)
# Array
import array

tuple_g = (ord(s) for s in chars)
array_g = array.array('I', (ord(s) for s in chars))


print(type(tuple_g))
print(tuple_g)
print(next(tuple_g))
print(next(tuple_g))

print(array_g)
print(array_g.tolist())

# 제너레이터 예제
print(('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,21)))

for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,21)):
    print(s)





