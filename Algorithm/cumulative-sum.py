# for 累積和　プロコン
    # よね，河村，末益けんの先輩などが参加

# けんちょんさんの記事の例題をpythonでといた方
    #https://upura.hatenablog.com/entry/2019/04/01/212701

# 累積和の実装
A = [] #list [a0 aN-1)

B = [0] + A #list [s0 sN) はじめ0だからこう書いた
B = list(accumulate(B)) # 累積和の定義式そのもの accumulate()=[a0, a0+a1, a0+a1+a2, ,,,]のリスト
