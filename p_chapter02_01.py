#chapter 02-01
# OOP 객체 지향 프로그래밍

class Car:
    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):
        return 'str : {} {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)


car1 = Car('bmw', {'color':'white','horsepower':'200', 'price':'8000'})
car2 = Car('Ferrari', {'color':'black','horsepower':'300', 'price':'9000'})
car3 = Car('Benz', {'color':'brown','horsepower':'400', 'price':'10000'})

car_list = [car1, car2, car3]

for item in car_list:
    print(repr(item))