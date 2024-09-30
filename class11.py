# 類別
'''
舉例: 汽車製造藍圖

class 類別名稱(繼承父類別名稱):
    類別屬性定義

    def 方法名稱():
        方法內容
'''

class Car(): # ()可省略 or (Object) 都可以
    # name = 'Ford'
    def __init__(self, name='BMW'): # 初始化類別(建構式)
        self.name = name

    def hello(self):
        print('Hello')

c1 = Car('Ford') # 實體化
c2 = Car()


print(c1.name)
print(c2.name)
c1.hello()

class Rectangle():
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def Area(self):
        return self.width * self.height
    
r = Rectangle(10, 20)
print(f'面積為{r.Area()}')

# 繼承
class Truck(Car):
    pass

t = Truck()
print(t.name)

# 封裝 (私用)
class Bank():
    def __init__(self, money):
        self.__money = money # 封裝屬性

    def show(self):
        print(f'當前存款為:{self.__money}')

    def __display(self): # 封裝方法
        print(f'當前存款為:{self.__money}')
'''
封裝(私有)的屬性或方法是無法被繼承
'''
b = Bank(20000)
# print(b.__money)
b.show()
# b.__display()

