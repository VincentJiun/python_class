# Open() 語法
'''
Open() 模式:
    r: 唯讀模式
    a: 附加寫入
    w: 覆蓋寫入

語法:
    with open('檔名', 模式) as f:
        處理內容

處理函式:
    read(): 讀取文字內容
    readline(): 讀取一行
    readlines(): 將每一行讀取的內容，以串列方式回傳
    write(): 寫入檔案
    close(): 關閉檔案
'''

# 文字檔案讀寫範例
# f = open('file.txt', 'w')
# f.write('123')
# f.close()

# f = open('file.txt', 'a')
# f.write('123')
# f.close()

# f = open('file.txt', 'r')
# print(f.read())
# f.close()

# 一定要記得 關閉檔案

# 另一種寫法 (避免忘記關檔案)
with open('file2.txt', 'a') as f:
    f.write('123\n')
    f.write('abc')




