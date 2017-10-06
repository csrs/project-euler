i = 1
sum = 0
while i < 9:
	if (i % 3 == 0) or (i % 5 == 0):
		sum += i
	i += 1
print(sum)

# a = 0
# while a < 5:
#     a += 1 # Same as a = a + 1 
#     print (a)