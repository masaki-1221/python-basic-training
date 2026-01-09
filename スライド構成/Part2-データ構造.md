# Part2: データ構造

---

## 05. リスト

---

### リストとは

- 複数のデータをまとめて管理できる
- 角括弧 `[]` で囲み、カンマで区切る

```python
fruits = ['apple', 'banana', 'orange']
numbers = [1, 2, 3, 4, 5]
```

---

### リストの特徴

- 異なる型のデータを混在できる
- 順番がある（インデックスでアクセス）
- 後から変更できる

```python
mixed = ['apple', 100, True, 3.14]
```

---

### インデックスとスライス

- 文字列と同じ仕組み
- **位置は0から数える**

```python
fruits = ['apple', 'banana', 'orange']
fruits[0]      # 'apple'
fruits[-1]     # 'orange'
fruits[0:2]    # ['apple', 'banana']
```

| apple | banana | orange |
|-------|--------|--------|
| 0 | 1 | 2 |

---

### 要素の変更

- インデックスを指定して上書き

```python
fruits = ['apple', 'banana', 'orange']
fruits[1] = 'grape'
# → ['apple', 'grape', 'orange']
```

---

### リストのメソッド

| メソッド | 機能 | 例 |
|----------|------|-----|
| `.append(x)` | 末尾に追加 | `fruits.append('grape')` |
| `.insert(i, x)` | 位置iに挿入 | `fruits.insert(1, 'grape')` |
| `.remove(x)` | 値xを削除 | `fruits.remove('banana')` |
| `.pop(i)` | 位置iを取り出して削除 | `fruits.pop(0)` |
| `.sort()` | 並び替え | `numbers.sort()` |

---

### リストの長さ

- `len()` 関数で要素数を取得

```python
fruits = ['apple', 'banana', 'orange']
len(fruits)  # 3
```

**ループ処理でよく使う！**

---

→ **コーディング実演**

---

## 06. 辞書

---

### 辞書とは

- **キーと値のペア**でデータを管理
- 波括弧 `{}` で囲む
- キーと値は `:` で区切る

```python
user = {
    'name': '山田',
    'age': 25,
    'department': '営業部'
}
```

---

### リストとの違い

| | リスト | 辞書 |
|---|--------|------|
| 書き方 | `[要素, 要素]` | `{キー: 値, キー: 値}` |
| アクセス | インデックス（番号） | キー（名前） |
| 例 | `fruits[0]` | `user['name']` |

---

### 値の取得

```python
user = {'name': '山田', 'age': 25}

# 角括弧でアクセス
user['name']   # '山田'
user['email']  # エラー！（キーがない）

# getメソッド（安全）
user.get('name')   # '山田'
user.get('email')  # None（エラーにならない）
user.get('email', '未設定')  # '未設定'（デフォルト値）
```

---

### 値の追加・変更

```python
user = {'name': '山田', 'age': 25}

# 追加（存在しないキー）
user['email'] = 'yamada@example.com'

# 変更（既存のキー）
user['age'] = 26
```

---

### 辞書のメソッド

| メソッド | 機能 | 戻り値 |
|----------|------|--------|
| `.keys()` | 全キーを取得 | `dict_keys(['name', 'age'])` |
| `.values()` | 全値を取得 | `dict_values(['山田', 25])` |
| `.items()` | キーと値のペア | `dict_items([('name', '山田'), ...])` |

**`.items()` はループ処理でよく使う！**

---

### 辞書の活用例

- APIのレスポンス（JSON）
- 設定データ
- ユーザー情報

```python
response = {
    'status': 'success',
    'data': {
        'user_id': 123,
        'username': 'yamada'
    }
}
response['data']['username']  # 'yamada'
```

---

→ **コーディング実演**

---

## 07. タプル

---

### タプルとは

- リストに似ているが、**変更できない**
- 丸括弧 `()` で囲む

```python
point = (10, 20)
colors = ('red', 'green', 'blue')
```

---

### タプルとリストの違い

| | リスト | タプル |
|---|--------|--------|
| 書き方 | `[要素, 要素]` | `(要素, 要素)` |
| 変更 | ✅ できる | ❌ できない |
| 用途 | 変更する可能性があるデータ | 変更されたくないデータ |

```python
# リストは変更OK
my_list = [1, 2, 3]
my_list[0] = 100  # OK

# タプルは変更NG
my_tuple = (1, 2, 3)
my_tuple[0] = 100  # エラー！
```

---

### タプルの用途

1. **関数から複数の値を返す**

```python
def get_position():
    return (10, 20)  # タプルで返す

x, y = get_position()  # 分解して受け取る
```

2. **辞書のitemsメソッドの戻り値**

```python
for key, value in user.items():
    print(f'{key}: {value}')
```

---

→ **コーディング実演**

---

## 08. 集合型（set）

---

### 集合型とは

- **重複のない要素の集まり**
- 波括弧 `{}` で囲む（辞書と似ているがキー:値がない）
- 同じ値は1つだけ

```python
fruits = {'apple', 'banana', 'apple', 'orange'}
# → {'apple', 'banana', 'orange'}（重複が除かれる）
```

---

### 集合型の作成

```python
# 直接作成
colors = {'red', 'green', 'blue'}

# リストから作成（重複削除）
my_list = [1, 2, 2, 3, 3, 3]
unique = set(my_list)  # {1, 2, 3}

# 空の集合（注意！）
empty_set = set()   # 正しい
empty_dict = {}     # これは辞書になる
```

---

### 集合演算

| 演算 | 記号 | 意味 |
|------|------|------|
| 和集合 | `\|` | どちらかに含まれる |
| 積集合 | `&` | 両方に共通 |
| 差集合 | `-` | 一方にだけ含まれる |

```python
a = {1, 2, 3}
b = {3, 4, 5}

a | b  # {1, 2, 3, 4, 5}
a & b  # {3}
a - b  # {1, 2}
```

---

### 集合型の使いどころ

1. **リストの重複を削除**

```python
purchases = ['apple', 'banana', 'apple']
unique_fruits = set(purchases)  # {'apple', 'banana'}
```

2. **共通要素を見つける**

```python
my_friends = {'Alice', 'Bob', 'Charlie'}
your_friends = {'Bob', 'David'}
common = my_friends & your_friends  # {'Bob'}
```

---

→ **コーディング実演**

---

## Part2 まとめ

| データ構造 | 書き方 | 特徴 |
|------------|--------|------|
| リスト | `[要素, 要素]` | 順番あり、変更可能 |
| 辞書 | `{キー: 値}` | キーでアクセス |
| タプル | `(要素, 要素)` | 変更不可 |
| 集合 | `{要素, 要素}` | 重複なし |

---

## 次回予告

**Part3: 演算子と条件分岐**
- 比較演算子・論理演算子
- None
- if / elif / else
