#find ehe cube root of perfect cube
x = int(raw_input('Enter an integer : '))
ans = 0
while ans**3 < abs(x) :
	ans = ans + 1
if ans**3!=abs(x):
	print(str(x) + ' is not a perfect cube')
else :
	if x < 0 :
		ans = -ans
	print('cube root of '+ str(x) + ' is ' + str(ans))