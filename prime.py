y = int(raw_input())
for i in range (y):
    z = int(raw_input())
    final = 1
    for t in range(1,z+1):
        if(z%t==0):
            final = final*t
        if(t*t <z):
            final = final*t
    print final
        
