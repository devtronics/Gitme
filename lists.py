n= [[1, 2, 3], [4,5,6,7,8,9]]


def flatten(lists)
    results = []
	for numbers in lists:
		for item in numbers:
			results.append(item)
	return results

# Always ensure to indent by 4 spaces

def flatten(lists):
    results = []
    for numbers in lists:
        for item in numbers:
            results.append(item)
    return results


print flatten(n)


