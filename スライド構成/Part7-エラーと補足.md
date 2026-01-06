# Part7: エラーと補足

---

## 19. try-except

---

### エラーとは

- プログラム実行中に発生する問題
- 通常、エラーが発生するとプログラムが停止する

```python
# エラーの例
result = 10 / 0  # ZeroDivisionError
```

---

### try-exceptの基本

- エラーが発生しても処理を続けられる
- `try`: エラーが起きる可能性のある処理
- `except`: エラー時の処理

```python
try:
    result = 10 / 0
except:
    print('エラーが発生しました')

print('処理を続行')
```

---

### エラーの種類を指定

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print('0では割れません')
```

特定のエラーだけを処理できる

---

### よく見るエラーの種類

| エラー | 原因 |
|--------|------|
| `ZeroDivisionError` | 0で割り算 |
| `TypeError` | 型が合わない操作 |
| `ValueError` | 値が不正 |
| `KeyError` | 辞書に存在しないキー |
| `FileNotFoundError` | ファイルが見つからない |
| `IndexError` | リストの範囲外 |

---

### 複数のエラーを処理

```python
try:
    value = int(input('数字を入力: '))
    result = 10 / value
except ValueError:
    print('数字を入力してください')
except ZeroDivisionError:
    print('0以外を入力してください')
```

---

### elseとfinally

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print('エラー')
else:
    print('成功')  # エラーなしの場合
finally:
    print('終了')  # 必ず実行
```

---

### finallyの用途

- ファイルを閉じる
- 接続を切断する
- 必ず実行したい後始末の処理

```python
try:
    file = open('data.txt')
    # 処理...
finally:
    file.close()  # 必ず閉じる
```

---

### 生成AIコードでの活用

- ファイル操作
- API呼び出し
- ネットワーク処理

**エラーが起きる可能性がある処理**には
try-exceptがよく使われる

---

→ **コーディング実演**

---

## 20. 紹介編（知っておくと便利な書き方）

---

### この章の目的

- 覚える必要はない
- **見かけたときに分かる**ようにする

生成AIのコードでよく見る書き方を紹介

---

### リスト内包表記

**通常のfor文**

```python
numbers = []
for i in range(5):
    numbers.append(i * 2)
```

**リスト内包表記**（1行で書ける）

```python
numbers = [i * 2 for i in range(5)]
```

---

### リスト内包表記（条件付き）

```python
# 偶数だけのリスト
evens = [i for i in range(10) if i % 2 == 0]
# [0, 2, 4, 6, 8]
```

**形式**: `[式 for 変数 in イテラブル if 条件]`

---

### 三項演算子

**通常のif-else**

```python
if score >= 60:
    result = '合格'
else:
    result = '不合格'
```

**三項演算子**（1行で書ける）

```python
result = '合格' if score >= 60 else '不合格'
```

---

### 三項演算子の形式

```python
Trueの値 if 条件 else Falseの値
```

簡単な条件分岐を1行で書きたい場合に使用

---

### アンパック

- リストやタプルの要素を複数の変数に代入

```python
point = (10, 20)
x, y = point  # x=10, y=20

data = ['田中', 30, '東京']
name, age, city = data
```

---

### アンパック + for文

```python
points = [(1, 2), (3, 4), (5, 6)]

for x, y in points:
    print(f'x={x}, y={y}')
```

---

### ラムダ式

**通常の関数**

```python
def double(x):
    return x * 2
```

**ラムダ式**（1行で書ける）

```python
double = lambda x: x * 2
```

---

### ラムダ式の活用例

```python
# sortedのキーとして使う
users = [('田中', 30), ('山田', 25), ('佐藤', 35)]

# 年齢でソート
sorted_users = sorted(users, key=lambda u: u[1])
```

一時的な簡単な関数を定義する場合に使用

---

→ **コーディング実演**

---

## Part7 まとめ

- **try-except**: エラーを処理して続行
- **リスト内包表記**: リストを1行で作成
- **三項演算子**: if-elseを1行で
- **アンパック**: 複数変数への一括代入
- **ラムダ式**: 簡易的な関数定義

---

## Python基礎研修 完了

---

### 学んだこと

| Part | 内容 |
|------|------|
| Part1 | print, コメント, 数値, 文字列, 変数, 型 |
| Part2 | リスト, 辞書, タプル |
| Part3 | 比較演算子, 論理演算子, None, if文 |
| Part4 | for文, while文, break, continue |
| Part5 | 関数, 引数, 戻り値, Docstring |
| Part6 | import, 組み込み関数, ライブラリ |
| Part7 | try-except, 便利な書き方 |

---

### これからの学習

- 生成AIが作るコードの**7割程度**は読めるはず
- 分からない部分は**生成AIに質問**
- コードを**読む経験**を積んでいく

---

## お疲れ様でした
