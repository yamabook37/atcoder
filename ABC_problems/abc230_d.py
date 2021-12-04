n,d=map(int,input().split())
#2次元リストで入力
Lst=[list(map(int,input().split())) for _ in range(n)]
#壁が存在する区間 [L,R] の組を R に対して昇順にソート
Lst.sort(key=lambda x:x[1])
#print(Lst)

#ソートで得られた順番に壁を見ていき、壁が破壊されていない場合は右端にパンチを放って破壊
ans=0
x=-1
for L,R in Lst:
  #L が x+D−1 以下はすでに壊れている、スキップ
	if(L<=x): continue
  # x=R として [R,R+D−1] にパンチ
	ans+=1
  #右端の位置を破壊できる範囲d分更新, この範囲に右端がある時は同時に破壊されている
	x=R+d-1
print(ans)
