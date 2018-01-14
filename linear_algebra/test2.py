
a = [0, 1, 2, 3, 4]

for i in range(len(a)):
	for j in range(i+1,len(a)):
		print i,j
		if a[i]<a[j]:
			a[i],a[j]=a[j],a[i]

print a