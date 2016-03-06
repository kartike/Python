num = raw_input()
a = list(num)
k = int(raw_input())
for i in range(k):    
    for y in range(len(a)):
        if(a[y]>a[y+1]):
            a = a[:y]+a[y+1:]
            y = y-1
            break
z = ''.join(a)
print z
