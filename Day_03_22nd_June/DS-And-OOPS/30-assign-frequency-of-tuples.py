from collections import Counter

test_list=[(4, 1), (3, 3), (4, 1), (5, 7), (3, 3), (4, 1)]

print("The original list is: ",str(test_list))

res=[(key,val) for key, val in Counter(test_list).items()]
print("Frequency Tuple List: ",str(res))