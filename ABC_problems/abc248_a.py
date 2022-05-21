S=input()

flag=[True for i in range(10)]
for i in range(9):
	flag[int(S[i])]=False
    #登場したものをFalse
for i in range(10):
	if(flag[i]): #Trueが残り
		print(i)