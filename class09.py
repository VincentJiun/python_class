# for 迴圈
'''
for i in range(起始, 結束):
    程式內容
'''

def sum():
    result = 0
    for i in range(1, 11):
        result += i

    return result

print(sum())

'''
for 元素 in list:
    程式內容
'''

list1 = [1,2,3,4,5,6,7,8,9]

def list_sum():
    result = 0
    for i in list1:
        result += i

    return result

print(list_sum())


# while 迴圈

def sum_while():
    total = 0
    i = 1
    while i <= 10:
        total += i
        i+=1

    return total

print(sum_while())

# break 跳出迴圈
'''
for i in range(1, 11):
    if i == 4:
        break
    
    print(i)
'''

# continue 跳過迴圈
'''
for i in range(1, 11):
    if i == 4:
        continue
    
    print(i)
'''

# 九九乘法
def multiple():
    for i in range(1, 10):
        for j in range(1, 10):
            print(f'{i} * {j} = {i*j}')
        
        print('-'*50)

multiple()

for i in range(1, 10, 2):
    print('*' * i)

for i in range(1, 10, 2):
    print((9-i)*' ', end='')
    print('*' * i)

for i in range(1, 10, 2):
    print('{:^9}'.format('*'*i))
