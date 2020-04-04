S=input()
ans=0
cnt=0
# Sを1文字ずつとる
for i in S:
  if i in ['A','C','G','T']:
    cnt+=1
    ans=max(ans,cnt)
  else: cnt=0
print(ans)