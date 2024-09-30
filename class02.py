'''
變量語法: 變量名 = 值
'''
a = 1
b = 2

age, name = 50, 'Vincent'

# 輸出 print()
print(a+b)
# sep 間隔符號: 預設值' '
print(a, b, sep='&')
# end 結束符號: 預設值'\n'
print(a, b, sep='&', end='.')

# print() 參數格式化 : % (舊語法)
print('%s考了%d分' % ('王小明', 80)) # %s: 文字 %d: 符號(數字)
print('%5s考了%3d分' % ('王小明', 80)) # 加 - 靠左
print('圓周率是%.2f' % (3.14159)) # %f: 符點數

# print() 參數格式化 : format()
print('{}考了{}分'.format('王小明', 80)) 
print('{0}考了{1}分'.format('王小明', 80)) # 利用索引值 帶入
print('{:>5}考了{:<3}分'.format('王小明', 80)) # 文字靠左 數字靠右 ^置中 

# print() 參數格式化 : f-strings
name1 = '王小明'
score = 80
print(f'{name1:^5}考了{score:3}分!')

'''
變量類型
1. 數字:
    1. int
    2. float
    3. long
    4. complex (複數)
2. 布爾(bool)
    1. true
    2. false
3. string (字符串)
4. list (列表) -> []
5. Tuple (元組) -> ()
6. dict (字典) -> {key: value}
7. Set (集合) -> {}

8. datetime 型態 需匯入模組
'''
name = '王小明'
age = 18
height = 178.5

print(type(name))
print(type(age))
print(type(height))

'''
1. 變數名稱一定要為字母 or _ 開頭
2. 大小寫有區別
'''

# 字符串 (str)
str1 = 'hello world !'
str2 = "hello world !"

# 字符串
str3 = '陳小明的外號"笨蛋"'
# str3 = '陳小明的外號\'笨蛋\''
print(str3)

# 字串索引
str4 = 'python'
print(str4[0])

# 字串切片
'''
語法: [開始:結束:步長] 

1. 步長默認為1 可以不用打
2. 包頭不包尾
'''
print(str4[2:5])
print(str4[:5])
print(str4[2:-1])

# 小技巧: Ctrl + shift + L or Ctrl + D
# 小技巧: Alt + 上/下

# 字串 查找、修改
'''
查找:
    1. find: mystr.find(str, start=0, end=len(mystr))
    2. index: mystr.index(str, start=0, end=len(mystr))
    3. count: mystr.count(str1, start=0, end=len(mystr))
'''

mystr1 = 'hellow world'
print(mystr1.find('world'))
print(mystr1.index('world'))
print(mystr1.count('o'))

'''
修改:
    1. replace: mystr.replace(str1, str2, mystr.count(str1))
'''
print(mystr1.replace('o', 'b'))

# 字串 拼接 拆分
'''
split: mystr.split(str="", 次數)
'''

str6 = 'hello world ha ha ha ha'
print(str6.split(' '))

# 字串 拼接
'''
join: mystr.join(str)
'''
str7 = '+'
li = ['my', 'name', 'is', 'V']

print(str7.join(li))

'''
其他:
1. capitalize() -> 大寫
2. title() -> 首字母大寫
3. startwith(str) -> 檢查字串是否str開頭 -> true/false 
'''

# 輸入: input() -> 很少用
scr = input('請輸入一個值:')
print(f'您的成績為{scr}')

# 字串相加問題
scr1 = input('國文成績')
scr2 = input('英文成績')
print(f'您的成績為{scr1 + scr2}')

# 型態轉換
scr1 = int(input('國文成績'))
scr2 = int(input('英文成績'))
print(f'您的成績為{scr1 + scr2}')

