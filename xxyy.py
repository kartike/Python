y = int(raw_input())

for j in range(y):
    sum = 0 
    k = int(raw_input())
    for i in range (k):
        if(i%3==0):
            sum = sum+i
            continue
        if(i%5==0):
            sum = sum+i
            continue
    print sum
