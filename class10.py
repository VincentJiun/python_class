# 模組
# 使用模組 from/ import/ as
# 亂數模組
import random as r

num = r.randint(1, 6)
print(num)

# 時間模組
import time

# 補充 help()
# help(time.sleep)

# time.time
t = time.time() # time stemp
# print(t)

def count_time():
    start = time.time()
    print(f'開始時間:{start}')
    for i in range(0, 100):
        time.sleep(0.001)
    end = time.time()
    print(f'結束時間:{end}')

    print(f'使用時間:{end-start}')

count_time()

# time.ctime()
now =  time.ctime()
print(now)

# localtime()
print(time.localtime())
print(time.localtime().tm_year)

# 檔案操作模組 os
'''
getcwd(): 取得目前工作目錄
remove('檔案名稱'): 刪除檔案
mkdir('目錄名稱'): 建立目錄 -> mkdirs('第一層/第二層'): 建立多層目錄
rmdir('目錄名稱'): 刪除目錄
path: 
    exists(): 判斷是否存在 目錄/檔案
    abspath(): 絕對路徑位置
    basename(): 路徑後的檔名
    getsize(): 檔案大小
    join(): 添加目錄/檔案路徑
'''
import os

print(os.getcwd())

if  os.path.exists('class09.py'):
    print('存在')
else:
    print('不存在')
