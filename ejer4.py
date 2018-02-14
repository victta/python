import os
x=os.listdir('c:\windows\system32')
for y in x:
	if y[-3:]=='exe' or y[-3:]=='bat':
		print y
		
		