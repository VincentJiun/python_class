# 字典 dictionary
'''
特性:
1. 與list類似,可增、刪、查、改, 也可儲存多個數據
2. 無序性: 無法用序列查
3. 唯一性: key必須是唯一值, 後面出現的key值會覆蓋掉之前的鍵值對
'''
dic1 = {'a': 1, 'b': 2, 'c': 3}

# 查
'''
1. dic[key]
2. dic.get(key)
'''
print(dic1['b'])
print(dic1.get('a'))
# 不同: dic[key] 若不存在 會報錯 dic.get(key) -> None

# 增
dic1['f'] = 8
print(dic1)

# 改
dic1['f'] = 10
print(dic1)
'''
1. 增/改時,若key值不存在->增  若存在->改
'''

# 刪
dic1.pop('f')
print(dic1)

# len 函數
print(len(dic1))

# keys 
print(dic1.keys())

# values
print(dic1.values())

# items
print(dic1.items())

# update (合併)
dic2 = {'t':9, 's':10}
dic1.update(dic2)
print(dic1)

# clear (清空)
dic2.clear()
print(dic2)




