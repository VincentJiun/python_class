'''
判斷語句: 如果某'條件滿足'，才做某件事情；條件不滿足，則不能做。

if 表達式:
    執行內容
'''

str1 = '學習python'

if str1 == '學習python':
    print(str1)
elif str1 == '學習java':
    print(str1)
else:
    print('錯誤')

'''
算數運算符: + - * / %(餘) //(商) **(指數) 
'''

'''
比較運算符: > < == >= <= !=
輸出只會為 true / false
'''

'''
邏輯運算符: and / or / not
非0即true
'''
if 123:
    print('非0即True')
'''
複合指定運算子: += -=
'''
x = 1
x += 1
print(x)

y = 1
y -= 1
print(y)