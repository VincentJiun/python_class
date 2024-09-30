# 集合set {}
'''
1. 集合有'唯一性',若後續有出現相同元素時，會被覆蓋
2. 創建集合
    1. {}
    2. set()
3. 用途: 存儲大量數據，且確保數據內容不重複
'''
set1 = {1,2,3,4,5,6}
print(set1)
# 集合具有無序性

s = {}
print(type(s))

# set() 創建
s1 = set()
print(type(s1))

# 唯一性:
list1 = ['a', 'b', 'c', 'd', 'e', 'a', 'c', 'd']
s2 = set(list1)
print(s2)

# 操作: 交集、 連集....
set2 = {7,8,9,2,3,5}

# 交集: 共有的元素 & 、 intersection
print(set1 & set2)
print(set1.intersection(set2))


# | union
print(set1 | set2)
print(set1.union(set2))

# 差集 - different
print(set1 - set2)
print(set1.difference(set2))

# 補集 ^ 
print(set1 ^ set2)
print(set1.symmetric_difference(set2))

# 查 in / not in
print('a' in set1)
print('a' not in set1)

# 增 add
set1.add('m')
print(set1)
'''
新增時只能添加不可變的值，不能添加變數
'''

# 刪 pop 刪除任一個元素 
set1.pop()
print(set1)

# 刪 remove 刪除指定元素
set1.remove('m')
print(set1)

# clear 清空
set1.clear()
print(set1)


