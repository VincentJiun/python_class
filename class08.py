# 華氏 = 攝氏*(9/5)+32

# degree_c = float(input('請輸入攝氏度:'))
def degree(c):
    y = c*(9/5)+32
    return y

# degree_w = degree(degree_c)
# print(f'華氏度數為:{degree_w}度')

# BMI 計算機
# BMI = 體重(kg)/身高(m)**2

my_h = 178.5 # (cm)
my_w = 75

def bmi(height, weight):
    h = height/100
    return weight/h**2

my_bmi = bmi(my_h, my_w)
print(f'我的BMI是:{my_bmi}')

# 成績判斷

def grad(score):
    if score < 60:
        print('不及格')
    elif score >=60 and score<90:
        print('及格')
    else:
        print('太棒了')

grad(90)
print(grad(90))

# 奇偶判斷

def odd(n):
    if n%2 == 0:
        return '偶數'
    else:
        return '奇數'
    
print(odd(10))

# 定義、判斷是 結合
def getBMI(weight, height):
    h = height/100
    bmi = weight/h**2
    msg = ''

    if bmi <= 18.5:
        msg = f'{bmi}:太瘦了，多吃一點'
    elif bmi >= 24:
        msg = f'{bmi}:太胖了，少吃一點'
    else:
        msg = f'{bmi}:標準身材，繼續保持'

    return msg

print(getBMI(80, 180))

# Lambda (匿名函數)
'''
def add(x,y):
    return x + y

lambda 參數1,參數2,...: 表達式
add = lambda x,y: x + y
'''
add = lambda x,y: x + y
print(add(1,2))

# Lambda 應用場景(一)
my_list = ['abd', 'a', 'abcd', 'ab']
# help(my_list.sort)
my_list.sort(key=lambda x: len(x))
print(my_list)

# Lambda 應用場景(二)
my_list1 = [1,2,3,5,7,8,12,78,84,22,123]
# help(filter)
print(list(filter(lambda x: (x%2==1), my_list1)))