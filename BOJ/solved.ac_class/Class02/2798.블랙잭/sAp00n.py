n, m = map(int,input().split())
v = list(map(int, input().split()))
s = list()
for i in range(len(v)) :
    for j in range((i+1), len(v)) :
        for z in range((j+1),len(v)) :
            s.append(sum([v[i],v[j],v[z]]))
s = [i for i in s if i<=m]
if len(s)>0 :
    print(max(s))

