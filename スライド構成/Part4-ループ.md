# Part4: ループ

---

## 11. for文とrange

---

### for文とは

- 同じ処理を**繰り返す**仕組み
- リストや文字列の要素を**1つずつ処理**

```python
for 変数 in 繰り返す対象:
    処理
```

---

### for文の基本

```python
fruits = ['apple', 'banana', 'orange']

for fruit in fruits:
    print(fruit)
```

**出力:**
```
apple
banana
orange
```

---

### range関数

- 指定した回数だけ繰り返す

| 書き方 | 意味 | 生成される数 |
|--------|------|--------------|
| `range(5)` | 0から4まで | 0, 1, 2, 3, 4 |
| `range(1, 6)` | 1から5まで | 1, 2, 3, 4, 5 |
| `range(0, 10, 2)` | 0から8まで2刻み | 0, 2, 4, 6, 8 |

**終了値は含まれない！**

---

### range関数の使用例

```python
# 5回繰り返す
for i in range(5):
    print(i)   # 0, 1, 2, 3, 4

# 1から5まで
for i in range(1, 6):
    print(i)   # 1, 2, 3, 4, 5
```

---

### enumerate関数

- **インデックス**と**要素**を同時に取得

```python
fruits = ['apple', 'banana', 'orange']

for i, fruit in enumerate(fruits):
    print(f'{i}: {fruit}')
```

**出力:**
```
0: apple
1: banana
2: orange
```

---

### 辞書のループ

```python
user = {'name': '山田', 'age': 25}

# キーだけ
for key in user:
    print(key)

# キーと値を同時に
for key, value in user.items():
    print(f'{key}: {value}')
```

---

### ネスト（入れ子）

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f'{i} x {j} = {i * j}')
```

**注意：ネストすると処理回数が急増！**

---

→ **コーディング実演**

---

## 12. while文

---

### while文とは

- 条件が **True の間** 繰り返す
- 繰り返す回数が決まっていない場合に使う

```python
while 条件:
    処理
```

---

### while文の基本

```python
count = 0

while count < 5:
    print(count)
    count += 1   # カウントを増やす
```

**出力:**
```
0
1
2
3
4
```

---

### 無限ループに注意！

```python
count = 0

while count < 5:
    print(count)
    # count += 1 を忘れると...
    # 永遠に止まらない！
```

**無限ループになったら強制終了が必要**

---

### for文とwhile文の使い分け

| | for文 | while文 |
|---|-------|---------|
| 回数 | **決まっている** | **決まっていない** |
| 例 | リストの全要素を処理 | 条件が満たされるまで |
| 頻度 | よく使う | たまに使う |

---

→ **コーディング実演**

---

## 13. breakとcontinue

---

### ループの流れを制御

| キーワード | 動作 |
|------------|------|
| `break` | ループを**終了** |
| `continue` | 今回だけ**スキップ** |

---

### break

- ループを**途中で終了**させる

```python
fruits = ['apple', 'banana', 'orange']

for fruit in fruits:
    if fruit == 'banana':
        print('見つかった！')
        break   # ここでループ終了
    print(fruit)
```

**出力:**
```
apple
見つかった！
```

---

### continue

- **今回だけスキップ**して次へ

```python
for num in range(1, 6):
    if num == 3:
        continue   # 3はスキップ
    print(num)
```

**出力:**
```
1
2
4
5
```

---

### breakとcontinueの違い

```
break    → ループを抜ける（終了）
continue → 今回だけスキップ（ループは続く）
```

```python
# break
for i in range(5):
    if i == 3:
        break      # 0, 1, 2 で終了

# continue
for i in range(5):
    if i == 3:
        continue   # 0, 1, 2, 4（3だけスキップ）
```

---

### while True + break パターン

```python
count = 0

while True:   # 無限ループ
    print(count)
    count += 1
    if count >= 5:
        break   # 条件を満たしたら終了
```

**生成AIのコードでよく見るパターン！**

---

→ **コーディング実演**

---

## 14. zip関数

---

### zip関数とは

- **複数のリストを同時にループ**
- 対応する要素をまとめて取り出す

```python
names = ['田中', '山田', '佐藤']
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f'{name}さんは{age}歳')
```

---

### zipを使わない場合

```python
names = ['田中', '山田', '佐藤']
ages = [25, 30, 35]

# インデックスを使う（少し複雑）
for i in range(len(names)):
    print(f'{names[i]}さんは{ages[i]}歳')
```

**zipを使った方がシンプル！**

---

### 3つ以上のリストも同時に

```python
names = ['田中', '山田']
ages = [25, 30]
cities = ['東京', '大阪']

for name, age, city in zip(names, ages, cities):
    print(f'{name}: {age}歳, {city}')
```

---

### zipで辞書を作成

```python
keys = ['name', 'age', 'city']
values = ['田中', 25, '東京']

user = dict(zip(keys, values))
# {'name': '田中', 'age': 25, 'city': '東京'}
```

---

→ **コーディング実演**

---

## 15. for-elseとwhile-else

---

### for-elseとは

- `break`せずにループが完了した場合、`else`が実行される
- 「探し物が見つからなかった」を表現

```python
for 変数 in リスト:
    処理
    if 条件:
        break
else:
    # breakしなかった場合に実行
```

---

### for-elseの例

```python
numbers = [1, 3, 5, 7, 9]

for num in numbers:
    if num % 2 == 0:  # 偶数を探す
        print(f'偶数が見つかりました: {num}')
        break
else:
    print('偶数は見つかりませんでした')
```

**breakしなかった = 見つからなかった**

---

### breakした場合

```python
numbers = [1, 3, 4, 7, 9]

for num in numbers:
    if num % 2 == 0:
        print(f'偶数が見つかりました: {num}')
        break   # 4で見つかった！
else:
    print('偶数は見つかりませんでした')  # 実行されない
```

---

### while-else

- while文にも同様にelseを付けられる

```python
count = 0

while count < 3:
    print(count)
    count += 1
else:
    print('正常に完了')  # breakしなかったので実行
```

---

### ポイント

- `else` は「breakしなかった場合」に実行
- 他の言語にはない特殊な機能
- 生成AIのコードで見かけたら注意して読む

---

→ **コーディング実演**

---

## Part4 まとめ

| トピック | ポイント |
|----------|----------|
| for文 | リストや回数を指定して繰り返す |
| range | `range(5)` → 0から4まで |
| enumerate | インデックスと要素を同時に取得 |
| while文 | 条件がTrueの間繰り返す |
| break | ループを終了 |
| continue | 今回だけスキップ |
| zip | 複数リストを同時にループ |
| for-else | breakしなかった場合に実行 |

---

## 次回予告

**Part5: 関数**
- 関数の基本
- 引数と戻り値
- デフォルト引数
- Docstring
