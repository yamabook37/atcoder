# 入力OK
n = int(input())
a = list(map(int,input().split()))

# 辞書に入れたほうがやりやすそう
dic = {}
for i in range(len(a)):
      dic.update([(i,a[i])]) #辞書に 要素，その番号を入れていく
      #print(d)
new_dic = sorted(dic.items(), key=lambda x:x[1]) #今の人数=key でソートしリストに入れる
#print(new_dic)

li = []
for i in range(len(a)):
      li.append(new_dic[i][0] +1) #人数のインデックスを追加，0から始めるからプラスしとく
print(' '.join(map(str, li))) #リストpの数値を文字列に変換する，そして''空白刻みで表示させる

'''
入力例
3
2 3 1
'''