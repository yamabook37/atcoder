# 2次元リストの扱い 2019/09/13

print("ここから2次元")
# 2次元リストの出力
Lists = [[1,2,3], [4,5,6]]
print(Lists)

# それぞれ出力したい時
for i in Lists:
    print(i)

# 2次元リストの各要素を出力
for List1 in Lists:
# 外のループで for 1次元リスト in 2次元リスト:
    for List in List1:
    # 中のループで for 要素 in 1次元リスト：
        print(List)

print()
# 2次元りすとの各要素をインデックス値で出力
for i in range(len(Lists)):
# for 変数1 in range(2次元リストのながさ)：
    for j in range(len(Lists[i])):
    # for 変数2 in range(1次元リストのながさ)：  
        print(Lists[i][j])

