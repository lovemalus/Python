# donesum.py
total = 0
s = raw_input('Enter a number (or "done"):')
while s != 'done' :
	num = int(s)
	total = total + num 
	s = raw_input('Enter a number (or "done"):')
print 'The sum is ' + str(total)

# break 跳出循环，continue 跳出本次循环的迭代直接进行下一次迭代。 