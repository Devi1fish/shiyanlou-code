for i in range(1,101):
	pd7=0	
	if i%7==0:
		pd7=1
	s =str(i)
	for j in s:
		if j =='7' : pd7=1
	if pd7==0: print(i)

