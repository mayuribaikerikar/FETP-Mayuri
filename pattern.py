n = int(input("Input: Enter the number of lines for the design: "))

str = "FORMULAQSOLUTIONS"


for row in range(n-1):
	for col in range(row,n):
		print(' ',end='')
	for col in range(row+1):
		print('* ',end='')
	print()
for row in range(n):
	for col in range(row+1):
		print(' ',end='')
	for col in range(row,n):
		print('* ',end='')
	print()
