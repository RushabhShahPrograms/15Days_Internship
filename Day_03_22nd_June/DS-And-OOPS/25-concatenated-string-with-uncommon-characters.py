def uncommonConcat(str1, str2):

	set1 = set(str1)
	set2 = set(str2)

	# take intersection of two sets to get list of
	# common characters
	common = list(set1 & set2)

	# separate out characters in each string
	# which are not common in both strings
	result = [ch for ch in str1 if ch not in common] + [ch for ch in str2 if ch not in common]

	print( ''.join(result) )

str1 = 'aacdb'
str2 = 'gafd'
uncommonConcat(str1,str2)