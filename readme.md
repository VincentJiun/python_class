# Python 基礎課程

## 認識Python

1. 程式執行原理:
    - 代碼 -> 機器語言 -> 執行

2. 語言分類
    
    1. 編譯型: 代碼 -> 二進制 -> 執行
        - C、C++、........
        - 優點: 執行效率高
        - 缺點: 可擴展性差、學習困難......

    2. 直譯型: 不須編譯，但在執行前須透過解釋器 -> 機器語言
        - php、 golang、 python ......
        - 優點: 跨平台性優、好學習
        - 缺點: 執行效率低

### 安裝Python 解釋器
- 官網下載 版本:3.10.11 (installer)
- 編輯器: VS Code

### 建立虛擬環境
1. 建立 虛擬環境
```
python -m venv (envname)
```
2. 執行 虛擬環境
```
(envname)/scripts/activate
```
3. 結束 虛擬環境
```
deactivate
```

### git 版本控制
- 開始版本控制
```cmd
git init
```
- 建立不須版控檔案: .gitignore

## Python 註釋

### class01.py
- 單行註釋
- 多行註釋

## 變量(數據儲存)
### class02.py
- 變量語法
- 數據類型
- 字符串
    - 索引、切片

## 列表 list
### class03.py

## 元組 Tuple
### class04.py

## 字典 dictionary
### class05.py

## 集合
### class06.py

## 判斷語句 、 比較運算符、 邏輯運算符
### class07.py

## 函數
### class08.py

1. 溫度轉換
2. BMI 計算機  
$BMI = 體重(kg) / 身高(m) ^2$
3. 成績判斷
4. 奇偶判斷
5. 補充: lambda function

## 迴圈 for / while
### class09.py
1. 範例
2. 九九乘法表

## 模組
### class10.py

## 物件導向 OOP
### class11.py

1. 基本概念: 類別、 物件
2. 三大特性: 封裝、 繼承、 多型

## 專案建立

### 專案架構概念
- 模組: 專案內模組
    - 專案資料夾內需 __init__.py (內容可空白)

### 引用套件 (import)

### 安裝套件 (pip)
```
pip install (模組名稱)
```

## 例外處理
### class12.py

1. try...except 語法

## 檔案處理 Open()
### class13.py

## if __name__ == '__main__:
### class14.py & test.py

## Excel自動化操作 (openpyxl)
### class15.py

## Openpyxl 實作練習
### class16.py
- 參考文件: https://openpyxl.readthedocs.io/en/stable/index.html








 