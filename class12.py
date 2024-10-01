# 例外處理
'''
try...except 語法

try: (不能省略)
    可能會發生例外的城市區塊
except: 例外情況一 [as 參數] (不可省略)
    處理例外的程式區塊
except Exception as e:
    處理所有可能發生的例外
else:
    指令正確時執行的程式區塊
finally:
    一定會執行的程式區塊
'''

# 語法測試、練習
try:
    f = open('123.txt', 'r')
except FileNotFoundError:
    print('找不到檔案')
except:
    print('有其他錯誤')
else:
    print('檔案存在')
finally:
    print('關閉檔案')

'''
其他錯誤:
    ValueError: 值錯誤(type error)
    ZeroDivisionError: 除數為0的錯誤
    IOError: 輸入/輸出錯誤
    Exception: 所有錯誤
'''