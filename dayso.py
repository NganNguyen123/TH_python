a=[]
n=int(input("nhap n:"))

for b in range (0,n):
	a.append(b)
print ("day so")
for c in range (0,n):
	print (a[c])
print("tinh tong chan")
tong=0
for c in a:
	if (c%2==0):
		tong+=c
print (tong)

