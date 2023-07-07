s = input()
ls = sorted(list(set(s)))

half = ""
ov = 0
m = ""

for i in ls:
    a = s.count(i)
    print(a)
    if a % 2 == 0:
        half += i * (a//2)
    elif (ov == 1):
        half = 0
        print("NO SOLUTION")
        break 
    else:
        ov = 1 
        m = i 
        half += i * ((a-1)//2)
if half != 0:
    print(half + m + half[::-1])