def completePair(set1,set2):
	
	count = 0
	for str1 in set1:
		for str2 in set2:
			result = str1 + str2

			# push all alphabets of concatenated
			# string into temporary set
			tmpSet = set([ch for ch in result if (ord(ch)>=ord('a') and ord(ch)<=ord('z'))])
			if len(tmpSet)==26:
				count = count + 1
	print (count)

set1 = ['abcdefgh', 'geeksforgeeks','lmnopqrst', 'abc']
set2 = ['ijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz','defghijklmnopqrstuvwxyz']
completePair(set1,set2)