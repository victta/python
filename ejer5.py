import os
x=os.listdir('c:\windows\system32')
y=raw_input("introduzca una letra:")
for z in x:
	if z.count(y)>0:
		print z
		print z.count()