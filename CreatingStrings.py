import itertools
s = input()
l = list(itertools.permutations(s))
ans = []
for i in l:
    ans.append("".join(i))

ans = set(ans)
ans = list(ans)
ans.sort()
print(len(ans))   

for i in ans:
    print(i)