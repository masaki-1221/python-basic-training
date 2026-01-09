# Part5: 関数

---

## 14. 関数の基本

---

### 関数とは

- 処理をまとめて名前を付けたもの
- 一度定義すれば、何度でも呼び出せる

**メリット**
1. 同じ処理を何度も書かなくて済む
2. 処理に名前が付き、コードが読みやすくなる

---

### 関数の定義

- `def` キーワードで定義
- 関数名の後に丸括弧 `()` とコロン `:`
- 処理はインデントを付けて書く

```python
def greet():
    print('こんにちは')
```

---

### 関数の呼び出し

- 関数名と丸括弧 `()` で呼び出す
- **定義しただけでは実行されない**

```python
def greet():
    print('こんにちは')

greet()  # こんにちは
greet()  # こんにちは（何度でも呼べる）
```

---

### 引数

- 関数に渡すデータ
- 丸括弧の中に変数名を書いて受け取る

```python
def greet(name):
    print(f'こんにちは、{name}さん')

greet('田中')  # こんにちは、田中さん
```

---

### 複数の引数

- カンマで区切って複数の引数を受け取れる

```python
def introduce(name, age):
    print(f'{name}さんは{age}歳です')

introduce('山田', 25)  # 山田さんは25歳です
```

---

### 戻り値（return）

- `return` で値を返す
- 返された値は変数に代入したり、直接使える

```python
def add(a, b):
    return a + b

result = add(3, 5)  # 8
print(add(10, 20))  # 30
```

---

### returnのポイント

- `return` が実行されると、その時点で関数終了
- `return` がない場合、`None` を返す

```python
def check(x):
    if x > 0:
        return '正の数'
    return '0以下'  # ここまで来たらこちら
```

---

### 複数の戻り値

- カンマで区切って複数の値を返せる
- タプルとして返される

```python
def calc(a, b):
    return a + b, a - b

result = calc(10, 3)  # (13, 7)
sum_val, diff_val = calc(10, 3)  # 分けて受け取り
```

---

### 生成AIコードでの関数

- 処理が関数としてまとまっていることが多い
- 確認ポイント：
  - 何を受け取るか（引数）
  - 何を返すか（戻り値）

---

→ **コーディング実演**

---

## 15. デフォルト引数とDocstring

---

### デフォルト引数

- 引数に初期値を設定できる
- 引数を省略するとデフォルト値が使われる

```python
def greet(name, count=1):
    for _ in range(count):
        print(f'こんにちは、{name}さん')

greet('田中')      # 1回出力
greet('山田', 3)   # 3回出力
```

---

### デフォルト引数の注意点

- デフォルト引数は、通常の引数より**後**に書く

```python
# ✅ OK
def func(a, b=10):
    ...

# ❌ エラー
def func(a=10, b):
    ...
```

---

### キーワード引数

- 引数名を指定して値を渡す
- 順番を変えられる
- どの引数に何を渡すか明確になる

```python
def introduce(name, age, city):
    print(f'{name}、{age}歳、{city}在住')

introduce(age=30, name='田中', city='東京')
```

---

### Docstring

- 関数の説明を書くための文字列
- 関数定義の直後に三重クォート `"""` で書く

```python
def add(a, b):
    """
    2つの数値を足し算する

    Args:
        a: 1つ目の数値
        b: 2つ目の数値

    Returns:
        2つの数値の合計
    """
    return a + b
```

---

### Docstringの内容

- 関数の概要
- 引数の説明（Args）
- 戻り値の説明（Returns）

**生成AIのコードによく含まれる**
→ 関数を理解するヒントになる

---

### Docstringの確認方法

```python
# help関数で確認
help(add)

# Jupyter Notebookでは ? で確認
add?
```

---

### 三重クォートの補足

- Docstring以外にも使える
- 複数行の長い文字列を書く場合に便利

```python
message = """
これは
複数行の
文字列です
"""
```

---

→ **コーディング実演**

---

## 16. 型ヒント

---

### 型ヒントとは

- 変数や関数の引数・戻り値の**型を明示**する機能
- Python 3.5以降で導入
- 最近の生成AIコードでよく見かける

```python
# 型ヒントなし
def add(a, b):
    return a + b

# 型ヒントあり
def add(a: int, b: int) -> int:
    return a + b
```

---

### 引数の型ヒント

- 引数名の後に `:` と型名を書く

```python
def greet(name: str, age: int):
    print(f'{name}さんは{age}歳です')
```

**name は str型、age は int型であることを示す**

---

### 戻り値の型ヒント

- 括弧の後に `->` と型名を書く

```python
def add(a: int, b: int) -> int:
    return a + b

def say_hello(name: str) -> None:
    print(f'こんにちは、{name}さん')
```

---

### よく使う型

| 型 | 意味 | 例 |
|----|------|-----|
| `int` | 整数 | `count: int = 0` |
| `float` | 小数 | `price: float = 100.5` |
| `str` | 文字列 | `name: str = 'Mike'` |
| `bool` | 真偽値 | `flag: bool = True` |
| `list` | リスト | `numbers: list` |
| `dict` | 辞書 | `user: dict` |

---

### リストの中身の型

```python
# 整数のリスト
def sum_numbers(numbers: list[int]) -> int:
    return sum(numbers)

# 辞書のキーと値の型
def get_user(users: dict[str, int]) -> int:
    ...
```

**`list[int]` = 整数のリスト**

---

### 型ヒントの注意点

- 型ヒントは**強制ではない**
- 間違った型を渡してもエラーにならない

```python
def add(a: int, b: int) -> int:
    return a + b

# 文字列を渡しても動く
result = add('Hello', 'World')  # 'HelloWorld'
```

**プログラマーへのヒントであり、実行時チェックではない**

---

### 生成AIコードでの型ヒント

- 最近のAI生成コードには型ヒントが多い
- 読み方：「この引数にはこの型を渡してほしい」
- 関数の使い方を理解するヒントになる

---

→ **コーディング実演**

---

## Part5 まとめ

- **関数**: 処理をまとめて名前を付けたもの
- **def**: 関数を定義するキーワード
- **引数**: 関数に渡すデータ
- **return**: 値を返す（戻り値）
- **デフォルト引数**: 省略可能な引数
- **Docstring**: 関数の説明文
- **型ヒント**: 引数・戻り値の型を明示

---

## 次回予告

**Part6: モジュールとライブラリ**
- import文
- 組み込み関数と標準ライブラリ
- サードパーティライブラリ
