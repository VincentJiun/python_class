# 列表 list

li1 = ['小明', '小王', '小華', 'V']

# 索引取值
print(li1[0])

# 增
'''
append(添加數據)
extend(list)
insert(位置, str)
'''
li1.append('騰')
print(li1)

li2 = ['X', 'Y', 'Z']
li1.extend(li2)
print(li1)

li1.insert(1, 'A')
print(li1)

# 刪
'''
del
pop
remove
'''

# del:
del li1[1]
print(li1)

# pop: 刪除最後一個元素
li1.pop()
print(li1)

# remove: 刪除指定數據
li1.remove('騰')
print(li1)

# 查
'''
index
count
in -> true/false
not in
'''
# in
print('V' in li1)

# not in
print('V' not in li1)

# 改
'''
索引修改
'''
# 索引修改: 索引必須存在 (會報錯)
li1[3] = 'VV'
print(li1)