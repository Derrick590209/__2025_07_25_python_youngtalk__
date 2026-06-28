＃＃　老師上課的圖
！[實體名稱](./實體名稱.png)
! [實體名稱2](./圖二.png)
# `argparse` 模組與 `ArgumentParser` 物件

## 什麼是 `argparse`？

`argparse` 是 Python 的**內建模組（module）**。

它的用途只有一個：

> **讓程式可以接受使用者從命令列（Command Line）輸入的參數。**

例如：

```bash
python test.py hello
```

其中：

```
hello
```

就是一個**命令列參數（Argument）**。

而 `argparse` 就是負責把這些參數讀進來。

---

# 什麼是 `ArgumentParser`？

`ArgumentParser` 是 `argparse` 模組裡面的一個**類別（Class）**。

當你建立它之後，就會得到一個 **ArgumentParser 物件（Object）**。

例如：

```python
import argparse

parser = argparse.ArgumentParser()
```

這一行做了兩件事情：

1. 使用 `ArgumentParser` 類別
2. 建立一個物件，名字叫做 `parser`

就像：

```python
a = list()
```

建立了一個 `list` 物件。

再例如：

```python
s = str()
```

建立了一個字串物件。

所以：

```python
parser = argparse.ArgumentParser()
```

就是建立一個 **ArgumentParser 物件**。

---

# 為什麼需要這個物件？

因為它會幫我們做很多事情，例如：

- 新增參數
- 檢查參數
- 自動產生說明（Help）
- 顯示錯誤訊息
- 幫你解析輸入

因此程式流程通常都是：

```text
建立 parser
      │
      ▼
加入參數（add_argument）
      │
      ▼
解析（parse_args）
      │
      ▼
得到使用者輸入
```

---

# 第一步：建立 Parser

```python
import argparse

parser = argparse.ArgumentParser()
```

目前它只是建立好而已。

還沒有任何功能。

---

# 第二步：加入參數

例如：

```python
parser.add_argument("name")
```

代表：

> 我要接受一個叫做 `name` 的參數。

---

例如執行：

```bash
python test.py Tom
```

那麼：

```
Tom
```

就會放到：

```
name
```

這個參數裡。

---

# 第三步：解析參數

```python
args = parser.parse_args()
```

這一步非常重要。

它會去讀：

```bash
python test.py Tom
```

然後產生：

```
args
```

裡面的資料。

最後：

```python
print(args.name)
```

就會輸出：

```
Tom
```

---

# 完整程式

```python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("name")

args = parser.parse_args()

print(args.name)
```

執行：

```bash
python test.py Tom
```

輸出：

```
Tom
```

---

# `ArgumentParser` 物件到底做了哪些事情？

它就像一位**櫃檯人員**。

假設很多人來報名。

沒有櫃檯：

```text
使用者
   │
   ▼
程式
```

程式根本不知道輸入的是什麼。

---

有 `ArgumentParser`：

```text
使用者
      │
      ▼
ArgumentParser
      │
      ▼
整理完成
      │
      ▼
你的程式
```

它幫你：

- ✔ 接收資料
- ✔ 檢查資料
- ✔ 告訴使用者哪裡錯
- ✔ 幫你整理好

---

# `ArgumentParser` 常用的方法

建立好 parser：

```python
parser = argparse.ArgumentParser()
```

之後可以呼叫許多方法。

---

## `add_argument()`

新增一個參數。

```python
parser.add_argument()
```

---

## `parse_args()`

開始解析命令列輸入。

```python
parser.parse_args()
```

---

## `print_help()`

顯示說明文件。

```python
parser.print_help()
```

例如：

```text
usage: test.py [-h] name

positional arguments:
  name

options:
  -h, --help
```

---

# 為什麼叫做 `ArgumentParser`？

拆開來看：

## Argument

意思就是：

> **參數**

例如：

```bash
python test.py Tom
```

其中：

```
Tom
```

就是一個 Argument。

---

## Parser

意思就是：

> **解析器**

它會把：

```
Tom
```

解析成：

```python
args.name
```

因此：

```
ArgumentParser
```

就是：

> **命令列參數解析器。**

---

# 它是一個物件，所以有自己的方法

例如：

```python
parser = argparse.ArgumentParser()
```

建立完成後，可以呼叫：

```python
parser.add_argument()
```

```python
parser.parse_args()
```

```python
parser.print_help()
```

這些都是 **ArgumentParser 物件的方法（Method）**。

---

# 和之前學過的物件做比較

例如：

```python
s = "hello"

s.upper()
```

這裡：

- `s` 是 `str` 物件
- `upper()` 是 `str` 物件的方法

同樣地：

```python
parser = argparse.ArgumentParser()

parser.add_argument()
```

這裡：

- `parser` 是 `ArgumentParser` 物件
- `add_argument()` 是 `ArgumentParser` 物件的方法

---

# 類別、物件、方法之間的關係

```text
argparse
│
├── 是模組（module）
│
└── ArgumentParser
      │
      └── 是類別（class）
             │
             └── 建立物件（object）
                     │
                     ├── add_argument()
                     ├── parse_args()
                     ├── print_help()
                     └── ...
```

---

# 整體觀念總結

- `argparse` 是**模組（module）**。
- `ArgumentParser` 是 `argparse` 模組中的**類別（class）**。
- `parser = argparse.ArgumentParser()` 會建立一個 **ArgumentParser 物件（object）**。
- 這個 `parser` 物件負責**定義、檢查、解析命令列參數**。
- 建立好 `parser` 後，最常使用的兩個方法是：
  - `parser.add_argument()`：定義程式接受哪些參數。
  - `parser.parse_args()`：讀取並解析使用者實際輸入的參數。

---

# 一個容易理解的比喻

把 `ArgumentParser` 想成一份表單：

| 動作 | 對應功能 |
|------|----------|
| `ArgumentParser()` | 建立一張空白表單 |
| `add_argument()` | 在表單上新增欄位（例如姓名、年齡） |
| `parse_args()` | 讀取使用者填寫的內容，整理成程式可以直接使用的資料 |

因此整個流程就是：

```text
建立表單
    │
    ▼
新增欄位
    │
    ▼
使用者填寫
    │
    ▼
整理資料
    │
    ▼
程式開始使用資料
```

---

# 一句話記住

> **`ArgumentParser` 是 `argparse` 模組中的一個類別，用來建立一個負責「接收、檢查、解析命令列參數」的物件。**
