# 類別
'''
舉例: 汽車製造藍圖

class 類別名稱():
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

c1 = Car('Ford') # 實體化(建立物件)
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

# 封裝 (私用)
class Bank():
    def __init__(self, money):
        self.__money = money # 封裝屬性

    def __display(self): # 封裝方法
        print(f'當前存款為:{self.__money}')

    def show(self):
        self.__display()
'''
1. 封裝(私有)的屬性或方法是無法被繼承
2. 私有方法/屬性 只能在class內部應用
'''
b = Bank(20000)
# print(b.__money)
# b.__display()
b.show()

# 繼承
'''
class 類別名稱(繼承父類別名稱):
    類別屬性定義

    def 方法名稱():
        方法內容

1. 子類別可以擴充富類別的方法
2. 子類別可以覆寫覆類別的屬性/方法
3. 子類別可以呼叫覆類別的方法
'''
class Truck(Car):
    def __init__(self, name):
        self.name = '子類別'+ name

    def run(self):
        print(f'{self.name}很會跑!')

    def hello(self):
        print('Hi!')

    

t1 = Truck('Banze')
print(t1.name)
t1.run()
t1.hello()

'''
super(): 呼叫父類別屬性/方法
'''
class Sports(Car):
    def __init__(self, name):
        super().__init__(name)

    def talk(self):
        super().hello()

    

s = Sports('Porsche')
s.talk()

# 多重繼承
'''
1. 多型: 若子類別有覆寫方法，以新方法為主 -> 多型
2. 多重繼承下，子類別沒有定義方法 -> 以第一個繼承的方法為主
'''
class Father(): # 定義父類別
    def say(self):
        print('爸爸說話!')

class Mother(): # 定義父類別
    def say(self):
        print('媽媽說話!')

class Child(Father, Mother): # 定義子類別 (多重繼承)
    pass
    # def say(self):
    #     print('兒子說話!')

child = Child()
child.say()