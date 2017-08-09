def average(intlist):
	if (len(intlist))>0:
		return sum(intlist)/float(len(intlist))
	return 0
n=int(raw_input("Please assign the value of n:"))
i=0
intlist=[]
while (i<n):
	m=int(raw_input("Please input a positive integer:"))
	if (m<0):
		print "the input must be a positive integer"
	else:
		intlist.append(m)
		i+=1
avg=average(intlist)
print "You have input %d integers and they are " %(n) ,
print  intlist
print  "Their average is "+str(ave)
