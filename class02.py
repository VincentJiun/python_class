'''
變量語法: 變量名 = 值
'''
a = 1
b = 2

age, name = 50, 'Vincent'

print(a+b)

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

