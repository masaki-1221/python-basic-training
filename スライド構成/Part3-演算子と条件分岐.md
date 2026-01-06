# Part3: 演算子と条件分岐

---

## 08. 比較演算子と論理演算子

---

### 比較演算子とは

- 2つの値を比較して **True** または **False** を返す
- 条件分岐で必須！

---

### 比較演算子一覧

| 演算子 | 意味 | 例 | 結果 |
|--------|------|-----|------|
| `==` | 等しい | `5 == 5` | True |
| `!=` | 等しくない | `5 != 3` | True |
| `>` | より大きい | `5 > 3` | True |
| `<` | より小さい | `5 < 3` | False |
| `>=` | 以上 | `5 >= 5` | True |
| `<=` | 以下 | `5 <= 3` | False |

---

### 注意：`=` と `==` の違い

| 記号 | 意味 | 例 |
|------|------|-----|
| `=` | 代入 | `x = 5`（xに5を入れる） |
| `==` | 比較 | `x == 5`（xが5か確認） |

**比較には `==` を使う！**

---

### in演算子

- 値が含まれているか確認

```python
fruits = ['apple', 'banana', 'orange']
'banana' in fruits   # True
'grape' in fruits    # False

text = 'Hello World'
'World' in text      # True
```

---

### not演算子

- True / False を反転

```python
not True    # False
not False   # True

'grape' not in fruits  # True（含まれていない）
```

---

### 論理演算子

| 演算子 | 意味 | 結果がTrueになる条件 |
|--------|------|----------------------|
| `and` | かつ | **両方**ともTrue |
| `or` | または | **どちらか一方**がTrue |

```python
True and True    # True
True and False   # False

True or False    # True
False or False   # False
```

---

### 論理演算子の活用例

```python
age = 25
is_member = True

# 20歳以上 かつ 会員
age >= 20 and is_member   # True

# 18歳未満 または 会員
age < 18 or is_member     # True
```

---

→ **コーディング実演**

---

## 09. None

---

### Noneとは

- 「**何もない**」ことを表す特別な値
- 型は `NoneType`

```python
value = None
print(value)       # None
print(type(value)) # <class 'NoneType'>
```

---

### Noneが使われる場面

1. 変数に値がまだ設定されていない
2. 関数が何も返さない
3. 辞書の `.get()` でキーが存在しない

---

### Noneの判定

- **`is`** を使う（`==` ではなく）

```python
value = None

value is None       # True（Noneである）
value is not None   # False（Noneではない）
```

**`is` を使うのがPythonの作法！**

---

### Noneの活用例

```python
# 辞書のgetメソッド
user = {'name': '山田'}
email = user.get('email')  # None

# Noneチェックしてから処理
if email is not None:
    print(f'メール: {email}')
else:
    print('メールが未設定です')
```

---

→ **コーディング実演**

---

## 10. 条件分岐

---

### if文とは

- 条件によって処理を変える仕組み
- プログラミングの基本中の基本

---

### if文の基本

```python
if 条件:
    条件がTrueの時の処理
```

```python
score = 80

if score >= 60:
    print('合格です')
```

**ポイント：インデント（字下げ）が必須！**

---

### インデントについて

- 半角スペース4つが一般的
- インデントがないとエラー

```python
if score >= 60:
    print('合格です')    # ← インデントあり = if文の中
    print('おめでとう')   # ← インデントあり = if文の中
print('判定終了')        # ← インデントなし = if文の外
```

---

### else

- 条件が **False** の場合の処理

```python
if score >= 60:
    print('合格です')
else:
    print('不合格です')
```

---

### elif

- 複数の条件を順番に確認
- 「else if」の略

```python
if score >= 90:
    print('評価: A')
elif score >= 80:
    print('評価: B')
elif score >= 70:
    print('評価: C')
else:
    print('評価: D')
```

**上から順に確認、最初にTrueになった処理だけ実行**

---

### 複数条件の組み合わせ

```python
age = 25
is_member = True

if age >= 20 and is_member:
    print('割引が適用されます')

if day == '土曜日' or day == '日曜日':
    print('週末です')
```

---

### ネスト（入れ子）

- if文の中にif文を書ける
- ただし深くなると読みにくい

```python
if age >= 18:
    print('成人です')
    if is_student:
        print('学生割引が適用されます')
```

**できるだけシンプルに書くことを心がける！**

---

→ **コーディング実演**

---

## Part3 まとめ

| トピック | ポイント |
|----------|----------|
| 比較演算子 | `==`, `!=`, `>`, `<`, `>=`, `<=` |
| in演算子 | 含まれているか確認 |
| 論理演算子 | `and`（かつ）, `or`（または） |
| None | 「何もない」を表す。`is` で判定 |
| if文 | 条件によって処理を変える |

---

## 次回予告

**Part4: ループ**
- for文とrange
- while文
- break / continue
