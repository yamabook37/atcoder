# 入力操作　ちょっとめんどい系

'''
#整数を2次元リストに格納する場合
# リスト名=[list(map(int,input().split())) for ダミー変数 in range(入力行数)]
Lists = [list(map(int, input().split())) for i in range(2)]
print(Lists)
print("end")

# 整数を2次元リストに格納する場合
# リスト名=[]でリストを用意し、for ダミー変数 in range(入力行数):でループ処理し、
# リスト名.append(list(map(int,input().split())))
Row = int(input()) # まず何列かを入力させる
List = []
for i in range(Row):
    List.append(list(map(int,input().split())))
    # append メソッドはリストに値を追加する
print(List)
'''

# 整数と文字列を複数の別々のリストに格納する場合
# リスト名=[]で複数のリストを用意し、for ダミー変数 in range(入力行数):でループ処理する
# そのループ処理の中で変数名A,変数名B=input().split()で入力データを受け取り、
# リスト名.append(データ)でリストにデータを追加する
Row = int(input())
Num = []
Alp = []
for i in range(Row):
    n, a = input().split()
    Num.append(int(n))
    Alp.append(a)
print(Num)
print(Alp)