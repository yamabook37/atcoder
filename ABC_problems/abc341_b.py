def calculate_max_currency(N, A, exchanges):
    for i in range(N - 1):
        while(1):
            #print(A)
            S, T = exchanges[i]  # 国iの通貨をSi単位以上持っているなら、国(i+1)の通貨をTi単位だけ獲得できる
            if A[i] >= S: #使える
                #1回ずつだと間に合わないので使える回数分まとめて計算
                times = A[i]//S
                A[i] = A[i]- S*times
                A[i+1] = A[i+1] + T*times
            else:
                break
    return A[-1]

n=int(input())
a = list(map(int, input().split()))
ex=[]
ex = [tuple(map(int, input().strip().split())) for _ in range(n - 1)]
print(calculate_max_currency(n, a, ex))
