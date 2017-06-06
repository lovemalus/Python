L=['adam', 'LISA', 'barT']
def f(s):
	return s[0].upper()+s[1:].lower()

s = map(f,L)

print s
