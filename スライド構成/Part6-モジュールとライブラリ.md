# Part6: モジュールとライブラリ

---

## 16. import文

---

### なぜimportが必要か

- Pythonには2種類の機能がある：
  1. **最初から使える**：`print()`, `len()` など
  2. **importして使う**：`datetime`, `os` など

- 生成AIのコードは最初にimport文が並ぶ
- 「このコードで使う機能を読み込んでいます」という意味

---

### importの基本

```python
import datetime

# モジュール名を付けて使う
now = datetime.datetime.now()
print(now)
```

**モジュール名.機能名** の形式で使う

---

### from import

- 特定の機能だけを取り込む
- モジュール名を付けずに使える

```python
from datetime import datetime

# 直接使える
now = datetime.now()
```

---

### 複数の機能をimport

```python
# カンマで区切る
from datetime import datetime, timedelta

today = datetime.now()
tomorrow = today + timedelta(days=1)
```

---

### asによる別名

- 長いモジュール名を短くできる

```python
import pandas as pd
import numpy as np

df = pd.read_csv('data.csv')
```

**pd, np は慣習的に使われる省略名**

---

### import文のパターンまとめ

| 書き方 | 使い方 |
|--------|--------|
| `import datetime` | `datetime.datetime.now()` |
| `from datetime import datetime` | `datetime.now()` |
| `import pandas as pd` | `pd.read_csv()` |

---

### 自作モジュールのimport

- 自分で作ったPythonファイルもimportできる
- 同じフォルダにあるファイルなら、拡張子なしでOK

```python
# my_functions.py をimport
import my_functions

my_functions.greet('田中')
```

---

→ **コーディング実演**

---

## 17. 組み込み関数と標準ライブラリ

---

### 組み込み関数とは

- **importなしで使える関数**
- これまでに使ったもの：
  - `print()`, `len()`, `type()`
  - `int()`, `str()`, `range()`

---

### よく使う組み込み関数

| 関数 | 機能 | 例 |
|------|------|-----|
| `len()` | 長さを返す | `len([1,2,3])` → `3` |
| `max()` | 最大値 | `max([1,5,3])` → `5` |
| `min()` | 最小値 | `min([1,5,3])` → `1` |
| `sum()` | 合計 | `sum([1,2,3])` → `6` |
| `sorted()` | 並び替え | `sorted([3,1,2])` → `[1,2,3]` |
| `abs()` | 絶対値 | `abs(-5)` → `5` |
| `round()` | 四捨五入 | `round(3.14)` → `3` |

---

### 標準ライブラリとは

- **Pythonに最初から付属**
- pip install不要だが、**importは必要**

---

### よく使う標準ライブラリ

| ライブラリ | 用途 |
|------------|------|
| `datetime` | 日付・時刻を扱う |
| `os` | ファイルパス、フォルダ操作 |
| `json` | JSONデータの読み書き |
| `time` | 処理の一時停止、時間計測 |
| `re` | 正規表現で文字列を検索・置換 |

---

### datetime

```python
from datetime import datetime, timedelta

now = datetime.now()
print(now)  # 現在日時

tomorrow = now + timedelta(days=1)
print(tomorrow)  # 明日
```

---

### os

```python
import os

# 現在のフォルダを取得
print(os.getcwd())

# パスを結合
path = os.path.join('folder', 'file.txt')
```

---

### json

```python
import json

# 辞書をJSON文字列に変換
data = {'name': '田中', 'age': 30}
json_str = json.dumps(data)

# JSON文字列を辞書に変換
data = json.loads(json_str)
```

**APIのレスポンス処理でよく使う**

---

### time

```python
import time

print('開始')
time.sleep(2)  # 2秒待機
print('終了')
```

---

→ **コーディング実演**

---

## 18. サードパーティライブラリ

---

### サードパーティライブラリとは

- Pythonに最初から入っていない
- 外部で開発されたライブラリ
- **pip install** でインストールして使う

---

### pip install

コマンドプロンプトで実行：

```bash
pip install pandas
pip install requests
pip install openpyxl
```

**生成AIのコードで見慣れないimportがあったら**
→ pip installが必要かも

---

### よく使うサードパーティライブラリ

| ライブラリ | 用途 |
|------------|------|
| `pandas` | 表形式データの処理（Excel読み込みなど） |
| `openpyxl` | Excelファイルの読み書き |
| `requests` | Webアクセス、API連携 |
| `selenium` / `playwright` | ブラウザ自動操作 |

---

### pandas

```python
import pandas as pd

# Excelファイルを読み込む
df = pd.read_csv('data.csv')

# データを表示
print(df.head())
```

**表形式データの定番ライブラリ**

---

### openpyxl

```python
from openpyxl import load_workbook

# Excelファイルを開く
wb = load_workbook('sample.xlsx')
sheet = wb.active

# セルの値を取得
value = sheet['A1'].value
```

---

### requests

```python
import requests

# Webページを取得
response = requests.get('https://example.com')
print(response.text)
```

**API連携でよく使う**

---

### ライブラリの調べ方

1. **公式ドキュメント**を確認
2. **生成AI**に質問する
3. 生成AIにコードを書いてもらう際に、使用するライブラリを指定する

---

### 仮想環境について

- プロジェクトごとにライブラリを分けたい場合に使う
- 独立したインストール先を作れる
- 詳しくは必要になった際に調べる

---

→ **コーディング実演**

---

## Part6 まとめ

- **import**: 機能を読み込む
- **組み込み関数**: importなしで使える
- **標準ライブラリ**: Python付属、importが必要
- **サードパーティ**: pip installでインストール
- **慣習的な省略**: `pd`, `np` など

---

## 次回予告

**Part7: エラーと補足**
- try-except
- リスト内包表記、三項演算子などの紹介
