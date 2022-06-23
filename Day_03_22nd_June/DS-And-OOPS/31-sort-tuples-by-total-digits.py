def digitCount(tup):
    return sum([len(str(val)) for val in tup])

tuplist=[(43343, 1), (2, 4), (12, 40), (1, 23)]
print("Unsorted Tuple List:",str(tuplist))

tuplist.sort(key=digitCount)
print("Sorted Tuple List:",str(tuplist))