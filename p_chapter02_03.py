#chapter 02-02
# OOP 객체 지향 프로그래밍


class Car:
    """
    Car class
    Auther :Peter
    Date : 2022.04.08
    Description : Class, Static, Instance Method
    """

    #클래스 변수 (모든 인스턴스가 공유)
    price_per_raise = 1.0

    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):
        return 'str : {} {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

    # Instance Method
    # Self : 객체의 고유한 속성 값을 사용 (self가 들어가 있으면 Instance 변수, 메소드)
    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car detail information : {} {}'.format(self._company, self._details.get('price')))


    # Instance Method 안의 인스턴스 값 가져오기
    def get_price(self):
        return 'Before Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price'))

    # Instance Method 안의 인스턴스 값 가져오기
    def get_price_calc(self):
        return 'After Car Price -> company : {}, price : {}'.format(self._company, float(self._details.get('price')) * Car.price_per_raise)

    # Class Method
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            pass
            print('none')
        else:
            cls.price_per_raise = per
            print('success')

    #Static method
    @staticmethod
    def is_bmw(inst):
        if inst._company == "bmw":
            return 'OK, This car is {}'.format(inst._company)
        else:
            return 'OK, This car is {}'.format(inst._company)



car1 = Car('bmw', {'color':'white','horsepower':'200', 'price':'8000'})
car2 = Car('Ferrari', {'color':'black','horsepower':'300', 'price':'9000'})


#가격정보(직접 접근)
print(car1._details.get('price'))
print(car2._details.get('price'))


#가격정보(인상전)
print(car1.get_price())
print(car2.get_price())

#가격 인상
Car.price_per_raise = 1.4
print(car1.get_price_calc())
print(car2.get_price_calc())

Car.raise_price(1.6)
print(car1.get_price_calc())
print(car2.get_price_calc())


print(Car.is_bmw(car1))
