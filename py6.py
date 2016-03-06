n1 = raw_input()
n2 = raw_input()

num = raw_input()
ly = list(num)
leny = len(num)  

finl = ['0']*int(n1)  # output binary with all 0s

finl[0] = num[0] #first done
finl[int(n1)-1] = num[leny-1] #last done

for ii in range(int(n1)-int(n2)+1):
    sum = 0 
    sum = int(finl[ii])+int(finl[ii+1])
    if(sum%2!=0):
        finl[ii+1] ='0'
    else:
        finl[ii+1] = '1'

z = ''.join(finl)
print z
