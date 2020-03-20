# 出力の部

# 標準入力 input(str)関数
# 整数を入力する
n = int(input())
print(n)

# 標準入力から得た文字列を区切りたい場合 input().split("区切り文字")
# split()...空欄なら半角スペースで区切り
st = input().split(",")
print(st)


# 整数を複数の変数に格納
# 変数名A,変数名B=map(int,input().split())
a, b = map(int, input().split())
print(a,b)


# リストに整数を格納する場合
# リスト名=[int(変数名) for 変数名 in input().split()] で格納する，　変数名は同じ文字であること
List = [int(i) for i in input().split()]
print(List)

#リストに文字列を格納する場合
# リスト名=[変数名 for 変数名 in input().split()] で格納する
List = [s for s in input().split()]
print(List)

# リストに整数を格納する，数字入力が改行されているパターンね
# リスト名=[int(input()) for ダミー変数 in range(変数の数)]
Li = [int(input()) for i in range(3)] #今回は３こ
print(Li)


# 入力行数が指定され、リストに整数を格納する
'''
5 ...これが入力行数
0 ...ここから入力みたいな感じの時
1
2
3
4
'''
# まず変数名=int(input())で行数を格納し
# リスト名=[int(input()) for ダミー変数 in range(変数名)]でリストに格納する，for で格納するのは複数行入力の時
Row = int(input())
Num = [int(input()) for i in range(Row)] #指定された行数だけ回す
print(Num)
