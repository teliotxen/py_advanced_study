#chapter 02-02
# OOP 객체 지향 프로그래밍

class Car:
    """
    Car class
    Auther :Peter
    Date : 2022.04.07
    """

    #클래스 변수 (모든 인스턴스가 공유한다.
    car_count = 0

    def __init__(self, company, details):
        self._company = company
        self._details = details
        Car.car_count += 1

    def __str__(self):
        return 'str : {} {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car detail information : {} {}'.format(self._company, self._details.get('price')))

    def __del__(self):
        Car.car_count -= 1

car1 = Car('bmw', {'color':'white','horsepower':'200', 'price':'8000'})
car2 = Car('Ferrari', {'color':'black','horsepower':'300', 'price':'9000'})
car3 = Car('Benz', {'color':'brown','horsepower':'400', 'price':'10000'})

car_list = [car1, car2, car3]



# print(car1._company == car2._company)
# print(car1 is car2)

# dir & __dict__

# print(dir(car1))
# print(car1.__dict__)



# print(car1.__doc__)
#""" 내용 """

# car1.detail_info()
# print(car1.__class__)
Car.detail_info(car2)

# 인스턴스 네임스페이스에 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 --> 상위(클래스 변수, 부모클래스 변수))
# 클래스 변수를 호출할 때는 클래스 이름으로 인스턴스 변수를 접근할 때는 클래스 인스턴스 이름으로 단 둘 다 동일한 이름이라면 인스턴스 변수 먼저 / 없으면 클래스 변수로 확인한다. 