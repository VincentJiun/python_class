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




