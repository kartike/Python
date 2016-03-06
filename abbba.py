def primes(n): 
	if n==2: return [2]
	elif n<2: return []
	s=range(3,n+1,2)
	mroot = n ** 0.5
	half=(n+1)/2-1
	i=0
	m=3
	while m <= mroot:
		if s[i]:
			j=(m*m-3)/2
			s[j]=0
			while j<half:
				s[j]=0
				j+=m
		i=i+1
		m=2*i+3
	return [2]+[x for x in s if x]

y = int(raw_input())
for i in range (y):
    z = int(raw_input())
    a = primes(z)
    b = []
    for zz in a:
        if(z%zz==0):
            b.append(zz)
    #b.append(for zz in a[] if z%zz==0)
    print max(b)
